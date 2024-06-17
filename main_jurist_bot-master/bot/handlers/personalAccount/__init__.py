from aiogram import Dispatcher, F
from .main import *

index = str(list(menu_buttons.keys()).index('PersonalCabinet'))

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(personal_account, F.data == 'menu:' + index)
    dp.callback_query.register(back_main_menu, F.data == 'back_main_menu')


