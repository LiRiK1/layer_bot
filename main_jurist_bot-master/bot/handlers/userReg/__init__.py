from aiogram import Dispatcher, F
from .main import *

def register_handlers(dp: Dispatcher):
    dp.message.register(set_user_name, fsm.UserRegister.user_name)
    dp.message.register(set_user_phone, fsm.UserRegister.user_phone)
    dp.message.register(set_user_mail, fsm.UserRegister.user_mail)


