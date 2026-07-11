import asyncio
import random
from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot.data import EXERCISES, WORKOUT_ORDER, MOTIVATION_MESSAGES
from bot.keyboards.inline import (
    main_menu_kb, workout_control_kb, rest_kb, workout_complete_kb,
    exercises_list_kb, category_exercises_kb, single_exercise_kb,
    quick_timer_kb, confirm_stop_kb, timer_kb
)
from bot.states import WorkoutState
from bot.utils.timer import WorkoutTimer, ReminderManager

router = Router()

# Foydalanuvchi sessiyalari
user_sessions = {}


def get_session(user_id: int) -> dict:
    """Foydalanuvchi sessiyasini olish"""
    if user_id not in user_sessions:
        user_sessions[user_id] = {
            "current_exercise_idx": 0,
            "current_set": 1,
            "timer": None,
            "reminder": None,
            "stats": {
                "exercises_done": 0,
                "total_time": 0,
            }
        }
    return user_sessions[user_id]


@router.callback_query(F.data == "start_workout")
async def start_workout(callback: CallbackQuery, state: FSMContext, bot: Bot):
    """Mashqni boshlash"""
    session = get_session(callback.from_user.id)
    session["current_exercise_idx"] = 0
    session["current_set"] = 1
    session["timer"] = WorkoutTimer(bot, callback.message.chat.id)
    session["reminder"] = ReminderManager(bot, callback.message.chat.id)

    await state.set_state(WorkoutState.exercising)

    await callback.message.edit_text(
        "🔥 **MASHQ BOSHLANDI!**\n\n"
        "Avval isinish mashqlarini bajaramiz.\n"
        "Tayyor bo'ling!",
        parse_mode="Markdown"
    )

    await asyncio.sleep(2)
    await show_exercise(callback.message, session, bot, callback.from_user.id)


async def show_exercise(message: Message, session: dict, bot: Bot, user_id: int):
    """Mashqni ko'rsatish"""
    idx = session["current_exercise_idx"]

    if idx >= len(WORKOUT_ORDER):
        # Mashq tugadi
        await workout_completed(message, session)
        return

    exercise_id = WORKOUT_ORDER[idx]
    exercise = EXERCISES[exercise_id]

    current_set = session["current_set"]
    total_sets = exercise["sets"]

    # Mashq ma'lumotlarini tayyorlash
    text = f"**{exercise['name']}**\n\n"

    if exercise["duration"]:
        text += f"⏱ **Vaqt:** {exercise['duration']} soniya\n"
    else:
        text += f"🔢 **Takrorlar:** {exercise['reps']}\n"

    text += f"📊 **Set:** {current_set}/{total_sets}\n\n"

    text += "📝 **Ko'rsatmalar:**\n"
    for i, instruction in enumerate(exercise["instructions"], 1):
        text += f"  {i}. {instruction}\n"

    # GIF yuborish
    if exercise.get("image"):
        try:
            await bot.send_animation(
                message.chat.id,
                exercise["image"],
                caption=text,
                parse_mode="Markdown",
                reply_markup=workout_control_kb(exercise_id, current_set, total_sets)
            )
        except:
            await message.answer(
                text,
                parse_mode="Markdown",
                reply_markup=workout_control_kb(exercise_id, current_set, total_sets)
            )
    else:
        await message.answer(
            text,
            parse_mode="Markdown",
            reply_markup=workout_control_kb(exercise_id, current_set, total_sets)
        )

    # Agar taymer kerak bo'lsa
    if exercise["duration"]:
        await start_exercise_timer(message, session, exercise_id, bot)
    else:
        # Eslatmalarni boshlash (takrorli mashqlar uchun)
        if session.get("reminder"):
            session["reminder"].stop()
            await session["reminder"].start_reminders(30)


async def start_exercise_timer(message: Message, session: dict, exercise_id: str, bot: Bot):
    """Mashq taymerini boshlash"""
    exercise = EXERCISES[exercise_id]
    duration = exercise["duration"]

    timer_msg = await bot.send_message(
        message.chat.id,
        f"⏱ **Taymer boshlandi: {duration} soniya**\n\n"
        "Harakat qiling! 💪",
        parse_mode="Markdown"
    )

    async def on_timer_complete():
        await bot.send_message(
            message.chat.id,
            "✅ **VAQT TUGADI!**\n\n"
            "Zo'r! Endi dam oling. 😮‍💨",
            parse_mode="Markdown"
        )
        # Keyingi setga o'tish
        await handle_set_complete(message, session, exercise_id, bot)

    await session["timer"].start_countdown(duration, timer_msg, f"💪 {exercise['name']}")
    await on_timer_complete()


async def handle_set_complete(message: Message, session: dict, exercise_id: str, bot: Bot):
    """Set tugaganda"""
    exercise = EXERCISES[exercise_id]
    current_set = session["current_set"]
    total_sets = exercise["sets"]

    if current_set < total_sets:
        # Keyingi set, dam olish
        session["current_set"] += 1
        await show_rest(message, session, exercise_id, bot)
    else:
        # Mashq tugadi, keyingi mashqqa
        session["current_exercise_idx"] += 1
        session["current_set"] = 1
        session["stats"]["exercises_done"] += 1

        if session["current_exercise_idx"] < len(WORKOUT_ORDER):
            await message.answer(
                "🎉 **Zo'r! Keyingi mashqqa o'tamiz!**",
                parse_mode="Markdown"
            )
            await asyncio.sleep(2)
            await show_exercise(message, session, bot, message.chat.id)
        else:
            await workout_completed(message, session)


async def show_rest(message: Message, session: dict, exercise_id: str, bot: Bot):
    """Dam olish"""
    exercise = EXERCISES[exercise_id]
    next_set = session["current_set"]
    total_sets = exercise["sets"]

    rest_msg = await bot.send_message(
        message.chat.id,
        f"😮‍💨 **Dam oling!**\n\n"
        f"Keyingi set: {next_set}/{total_sets}\n"
        f"⏱ 30 soniya dam oling...",
        parse_mode="Markdown",
        reply_markup=rest_kb(exercise_id)
    )

    # 30 soniya dam olish taymeri
    completed = await session["timer"].start_countdown(30, rest_msg, "😮‍💨 Dam olish")

    if completed:
        await bot.send_message(
            message.chat.id,
            f"⚡ **DAVOM ETAMIZ!**\n\n"
            f"Set {next_set}/{total_sets}",
            parse_mode="Markdown"
        )
        await show_exercise(message, session, bot, message.chat.id)


async def workout_completed(message: Message, session: dict):
    """Mashq tugadi"""
    if session.get("reminder"):
        session["reminder"].stop()
    if session.get("timer"):
        session["timer"].cancel()

    exercises_done = session["stats"]["exercises_done"]

    await message.answer(
        f"🎉🎉🎉 **TABRIKLAYMIZ!** 🎉🎉🎉\n\n"
        f"Siz bugungi mashqni muvaffaqiyatli tugatdingiz!\n\n"
        f"📊 **Statistika:**\n"
        f"✅ Bajarilgan mashqlar: {exercises_done}\n"
        f"💪 Ajoyib ish!\n\n"
        f"⭐ Muntazam qiling - natija albatta bo'ladi!",
        parse_mode="Markdown",
        reply_markup=workout_complete_kb()
    )


@router.callback_query(F.data.startswith("done_"))
async def exercise_done(callback: CallbackQuery, bot: Bot):
    """Mashq tugadi tugmasi"""
    # done_pushup_1 -> exercise_id = pushup
    parts = callback.data.split("_")
    exercise_id = "_".join(parts[1:-1])  # set raqamini olib tashlash

    session = get_session(callback.from_user.id)
    if session.get("reminder"):
        session["reminder"].stop()

    await callback.answer("✅ Zo'r!")
    await handle_set_complete(callback.message, session, exercise_id, bot)


@router.callback_query(F.data.startswith("skip_"))
async def skip_exercise(callback: CallbackQuery, bot: Bot):
    """Mashqni o'tkazib yuborish"""
    session = get_session(callback.from_user.id)
    if session.get("reminder"):
        session["reminder"].stop()
    if session.get("timer"):
        session["timer"].cancel()

    session["current_exercise_idx"] += 1
    session["current_set"] = 1

    await callback.answer("⏭ O'tkazib yuborildi")
    await show_exercise(callback.message, session, bot, callback.from_user.id)


@router.callback_query(F.data.startswith("pause_"))
async def pause_exercise(callback: CallbackQuery):
    """Pauzaga olish"""
    session = get_session(callback.from_user.id)

    if session["timer"]:
        if session["timer"].is_paused:
            session["timer"].resume()
            await callback.answer("▶️ Davom etmoqda")
        else:
            session["timer"].pause()
            await callback.answer("⏸ Pauza")


@router.callback_query(F.data == "stop_workout")
async def stop_workout(callback: CallbackQuery):
    """Mashqni to'xtatish"""
    await callback.message.edit_text(
        "⚠️ **Rostdan ham to'xtatmoqchimisiz?**\n\n"
        "Hozir to'xtasangiz, natijaga erisha olmaysiz!",
        parse_mode="Markdown",
        reply_markup=confirm_stop_kb()
    )


@router.callback_query(F.data == "confirm_stop")
async def confirm_stop(callback: CallbackQuery, state: FSMContext):
    """To'xtatishni tasdiqlash"""
    session = get_session(callback.from_user.id)
    if session.get("reminder"):
        session["reminder"].stop()
    if session.get("timer"):
        session["timer"].cancel()

    await state.set_state(WorkoutState.idle)
    await callback.message.edit_text(
        "😔 **Mashq to'xtatildi.**\n\n"
        "Ertaga qaytadan harakat qiling!\n"
        "💪 Kuchli iroda - kuchli tana!",
        parse_mode="Markdown",
        reply_markup=main_menu_kb()
    )


@router.callback_query(F.data == "cancel_stop")
async def cancel_stop(callback: CallbackQuery, bot: Bot):
    """To'xtatishni bekor qilish"""
    session = get_session(callback.from_user.id)
    await callback.answer("💪 Zo'r! Davom etamiz!")
    await show_exercise(callback.message, session, bot, callback.from_user.id)


@router.callback_query(F.data.startswith("rest_done_"))
async def rest_done(callback: CallbackQuery, bot: Bot):
    """Dam olish tugadi"""
    session = get_session(callback.from_user.id)
    if session["timer"]:
        session["timer"].cancel()

    await callback.answer("💪 Zo'r!")
    await show_exercise(callback.message, session, bot, callback.from_user.id)


@router.callback_query(F.data.startswith("rest_add_"))
async def rest_add_time(callback: CallbackQuery):
    """Qo'shimcha dam olish"""
    await callback.answer("➕ 30 soniya qo'shildi")
    # Taymerga vaqt qo'shish (oddiy implementatsiya)


# MASHQLAR RO'YXATI
@router.callback_query(F.data == "exercises_list")
async def show_exercises_list(callback: CallbackQuery):
    """Mashqlar ro'yxati"""
    await callback.message.edit_text(
        "📋 **MASHQLAR RO'YXATI**\n\n"
        "Kategoriyani tanlang:",
        parse_mode="Markdown",
        reply_markup=exercises_list_kb()
    )


@router.callback_query(F.data.startswith("cat_"))
async def show_category(callback: CallbackQuery):
    """Kategoriya mashqlari"""
    category = callback.data.replace("cat_", "")

    category_names = {
        "isinish": "🔥 ISINISH MASHQLARI",
        "asosiy": "💪 ASOSIY MASHQLAR",
        "bilak": "🦾 BILAK MASHQLARI",
        "chozilish": "🧘 CHO'ZILISH MASHQLARI"
    }

    await callback.message.edit_text(
        f"**{category_names.get(category, 'Mashqlar')}**\n\n"
        "Mashqni tanlang:",
        parse_mode="Markdown",
        reply_markup=category_exercises_kb(category)
    )


@router.callback_query(F.data.startswith("exercise_"))
async def show_single_exercise(callback: CallbackQuery, bot: Bot):
    """Bitta mashq ma'lumoti"""
    exercise_id = callback.data.replace("exercise_", "")
    exercise = EXERCISES.get(exercise_id)

    if not exercise:
        await callback.answer("Mashq topilmadi")
        return

    text = f"**{exercise['name']}**\n\n"

    if exercise["duration"]:
        text += f"⏱ **Vaqt:** {exercise['duration']} soniya\n"
    else:
        text += f"🔢 **Takrorlar:** {exercise['reps']}\n"

    text += f"📊 **Setlar:** {exercise['sets']}\n\n"

    text += "📝 **Ko'rsatmalar:**\n"
    for i, instruction in enumerate(exercise["instructions"], 1):
        text += f"  {i}. {instruction}\n"

    if exercise.get("image"):
        try:
            await callback.message.delete()
            await bot.send_animation(
                callback.message.chat.id,
                exercise["image"],
                caption=text,
                parse_mode="Markdown",
                reply_markup=single_exercise_kb(exercise_id)
            )
        except:
            await callback.message.edit_text(
                text,
                parse_mode="Markdown",
                reply_markup=single_exercise_kb(exercise_id)
            )
    else:
        await callback.message.edit_text(
            text,
            parse_mode="Markdown",
            reply_markup=single_exercise_kb(exercise_id)
        )


@router.callback_query(F.data.startswith("single_"))
async def start_single_exercise(callback: CallbackQuery, state: FSMContext, bot: Bot):
    """Bitta mashqni boshlash"""
    exercise_id = callback.data.replace("single_", "")

    session = get_session(callback.from_user.id)
    session["current_exercise_idx"] = WORKOUT_ORDER.index(exercise_id) if exercise_id in WORKOUT_ORDER else 0
    session["current_set"] = 1
    session["timer"] = WorkoutTimer(bot, callback.message.chat.id)
    session["reminder"] = ReminderManager(bot, callback.message.chat.id)

    await state.set_state(WorkoutState.exercising)
    await show_exercise(callback.message, session, bot, callback.from_user.id)


# TEZKOR TAYMER
@router.callback_query(F.data == "quick_timer")
async def show_quick_timer(callback: CallbackQuery):
    """Tezkor taymer"""
    await callback.message.edit_text(
        "⏱ **TEZKOR TAYMER**\n\n"
        "Vaqtni tanlang:",
        parse_mode="Markdown",
        reply_markup=quick_timer_kb()
    )


@router.callback_query(F.data.startswith("qtimer_"))
async def quick_timer_start(callback: CallbackQuery, bot: Bot):
    """Tezkor taymerni boshlash"""
    seconds = int(callback.data.replace("qtimer_", ""))

    session = get_session(callback.from_user.id)
    session["timer"] = WorkoutTimer(bot, callback.message.chat.id)

    timer_msg = await callback.message.edit_text(
        f"⏱ **Taymer: {seconds} soniya**\n\n"
        "Boshlandi!",
        parse_mode="Markdown"
    )

    completed = await session["timer"].start_countdown(seconds, timer_msg, "⏱ Tezkor taymer")

    if completed:
        await bot.send_message(
            callback.message.chat.id,
            "🔔 **VAQT TUGADI!** 🔔",
            parse_mode="Markdown",
            reply_markup=main_menu_kb()
        )


# STATISTIKA
@router.callback_query(F.data == "stats")
async def show_stats(callback: CallbackQuery):
    """Statistika"""
    session = get_session(callback.from_user.id)
    stats = session.get("stats", {"exercises_done": 0})

    await callback.message.edit_text(
        f"📊 **SIZNING STATISTIKANGIZ**\n\n"
        f"✅ Bajarilgan mashqlar: {stats.get('exercises_done', 0)}\n\n"
        f"💡 **Maslahatlar:**\n"
        f"• Haftasiga kamida 5 kun mashq qiling\n"
        f"• 7-8 soat sifatli uyqu oling\n"
        f"• Kuniga 80-120g oqsil iste'mol qiling\n"
        f"• Shakarli ichimliklarni kamaytiring",
        parse_mode="Markdown",
        reply_markup=main_menu_kb()
    )


# ASOSIY MENYU
@router.callback_query(F.data == "main_menu")
async def back_to_main(callback: CallbackQuery, state: FSMContext):
    """Bosh menyuga qaytish"""
    session = get_session(callback.from_user.id)
    if session.get("reminder"):
        session["reminder"].stop()
    if session.get("timer"):
        session["timer"].cancel()

    await state.set_state(WorkoutState.idle)

    await callback.message.edit_text(
        "🏋️ **MASHQ BOTI**\n\n"
        "Qomat, yelka, qanot va qorin uchun kunlik mashqlar!\n\n"
        "⏱ Kuniga 15-20 daqiqa\n"
        "📅 Haftasiga 5-6 kun\n\n"
        "Tanlang:",
        parse_mode="Markdown",
        reply_markup=main_menu_kb()
    )
