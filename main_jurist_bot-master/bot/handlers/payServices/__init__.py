from aiogram import Dispatcher, F
from .main import *

index = str(list(menu_buttons.keys()).index('Payment'))

def register_handlers(dp: Dispatcher):
    dp.callback_query.register(pay, F.data == 'menu:' + index)
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.callback_query.register(return_to_main_menu_from_pay, F.data == 'return_to_main_menu_from_pay')

