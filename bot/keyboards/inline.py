from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.data import EXERCISES, WORKOUT_ORDER


def main_menu_kb():
    """Asosiy menyu"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏋️ MASHQNI BOSHLASH", callback_data="start_workout")],
        [InlineKeyboardButton(text="📋 Mashqlar ro'yxati", callback_data="exercises_list")],
        [InlineKeyboardButton(text="⏱ Tezkor taymer", callback_data="quick_timer")],
        [InlineKeyboardButton(text="📊 Statistika", callback_data="stats")],
    ])


def workout_control_kb(exercise_id: str, set_num: int, total_sets: int):
    """Mashq nazorat tugmalari"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ TAYYOR!", callback_data=f"done_{exercise_id}_{set_num}")],
        [
            InlineKeyboardButton(text="⏸ Pauza", callback_data=f"pause_{exercise_id}"),
            InlineKeyboardButton(text="⏭ Keyingi", callback_data=f"skip_{exercise_id}")
        ],
        [InlineKeyboardButton(text="🛑 To'xtatish", callback_data="stop_workout")],
    ])


def timer_kb(seconds: int, exercise_id: str):
    """Taymer tugmalari"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"⏱ {seconds} soniya boshlandi...", callback_data="timer_info")],
        [
            InlineKeyboardButton(text="⏸ Pauza", callback_data=f"timer_pause_{exercise_id}"),
            InlineKeyboardButton(text="⏭ O'tkazib yuborish", callback_data=f"timer_skip_{exercise_id}")
        ],
    ])


def rest_kb(exercise_id: str):
    """Dam olish tugmalari"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Tayyor! Davom etamiz!", callback_data=f"rest_done_{exercise_id}")],
        [InlineKeyboardButton(text="➕ 30s qo'shish", callback_data=f"rest_add_{exercise_id}")],
    ])


def exercises_list_kb():
    """Mashqlar ro'yxati"""
    builder = InlineKeyboardBuilder()

    categories = {
        "isinish": "🔥 ISINISH",
        "asosiy": "💪 ASOSIY",
        "bilak": "🦾 BILAK",
        "chozilish": "🧘 CHO'ZILISH"
    }

    for cat_id, cat_name in categories.items():
        builder.row(InlineKeyboardButton(text=cat_name, callback_data=f"cat_{cat_id}"))

    builder.row(InlineKeyboardButton(text="🔙 Orqaga", callback_data="main_menu"))
    return builder.as_markup()


def category_exercises_kb(category: str):
    """Kategoriya mashqlari"""
    builder = InlineKeyboardBuilder()

    for ex_id, ex_data in EXERCISES.items():
        if ex_data["category"] == category:
            builder.row(InlineKeyboardButton(
                text=ex_data["name"],
                callback_data=f"exercise_{ex_id}"
            ))

    builder.row(InlineKeyboardButton(text="🔙 Orqaga", callback_data="exercises_list"))
    return builder.as_markup()


def single_exercise_kb(exercise_id: str):
    """Bitta mashq uchun"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="▶️ Shu mashqni boshlash", callback_data=f"single_{exercise_id}")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data=f"cat_{EXERCISES[exercise_id]['category']}")],
    ])


def quick_timer_kb():
    """Tezkor taymer"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="30s", callback_data="qtimer_30"),
            InlineKeyboardButton(text="45s", callback_data="qtimer_45"),
            InlineKeyboardButton(text="60s", callback_data="qtimer_60"),
        ],
        [
            InlineKeyboardButton(text="90s", callback_data="qtimer_90"),
            InlineKeyboardButton(text="2 daqiqa", callback_data="qtimer_120"),
            InlineKeyboardButton(text="3 daqiqa", callback_data="qtimer_180"),
        ],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="main_menu")],
    ])


def confirm_stop_kb():
    """To'xtatishni tasdiqlash"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Ha, to'xtatish", callback_data="confirm_stop"),
            InlineKeyboardButton(text="❌ Yo'q, davom etish", callback_data="cancel_stop"),
        ],
    ])


def workout_complete_kb():
    """Mashq tugaganda"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Yana boshlash", callback_data="start_workout")],
        [InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="main_menu")],
    ])
