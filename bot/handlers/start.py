from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.keyboards.inline import main_menu_kb
from bot.states import WorkoutState

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """Bot boshlanganda"""
    await state.set_state(WorkoutState.idle)

    await message.answer(
        f"💪 **Salom, {message.from_user.full_name}!**\n\n"
        f"Men sizga qomat, yelka, qanot va qorin mashqlarini "
        f"bajarishda yordam beraman.\n\n"
        f"🔥 **Kuniga 15-20 daqiqa** - bu yetarli!\n"
        f"📅 **Haftasiga 5-6 kun** - muntazamlik muhim!\n\n"
        f"⭐ MUNTAZAM QILING - NATIJA ALBATTA BO'LADI!\n\n"
        f"Quyidagi tugmalardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=main_menu_kb()
    )


@router.message(Command("menu"))
async def cmd_menu(message: Message, state: FSMContext):
    """Menyu"""
    await state.set_state(WorkoutState.idle)
    await message.answer(
        "🏋️ **ASOSIY MENYU**\n\n"
        "Tanlang:",
        parse_mode="Markdown",
        reply_markup=main_menu_kb()
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Yordam"""
    await message.answer(
        "ℹ️ **YORDAM**\n\n"
        "**Buyruqlar:**\n"
        "/start - Botni boshlash\n"
        "/menu - Asosiy menyu\n"
        "/help - Yordam\n\n"
        "**Bot haqida:**\n"
        "Bu bot sizga kunlik mashqlarni bajarishda yordam beradi.\n\n"
        "**Mashq tartibi:**\n"
        "1. 🔥 Isinish (3-4 daqiqa)\n"
        "2. 💪 Asosiy mashqlar (15-20 daqiqa)\n"
        "3. 🦾 Bilak mashqlari (8-10 daqiqa)\n"
        "4. 🧘 Cho'zilish (2-3 daqiqa)\n\n"
        "💡 Har kuni mashq qiling - natija albatta bo'ladi!",
        parse_mode="Markdown",
        reply_markup=main_menu_kb()
    )
