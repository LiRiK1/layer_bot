from aiogram import Dispatcher, F
from .main import *

index = str(list(menu_buttons.keys()).index('MyLawyers'))

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(send_jurists, F.data == 'menu:' + index)

