from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Yordam"), KeyboardButton(text="Ma'lumot")],
        ],
        resize_keyboard=True
    )
