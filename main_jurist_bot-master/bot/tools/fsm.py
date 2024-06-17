from aiogram.fsm.state import State, StatesGroup

class UserRegister(StatesGroup):
    user_name = State()
    user_phone = State()
    user_mail = State()