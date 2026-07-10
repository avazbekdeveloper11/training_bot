from aiogram.fsm.state import State, StatesGroup


class WorkoutState(StatesGroup):
    """Mashq holatlari"""
    idle = State()  # Kutish
    warming_up = State()  # Isinish
    exercising = State()  # Mashq qilish
    resting = State()  # Dam olish
    cooling_down = State()  # Sovutish/cho'zilish
    paused = State()  # Pauza
