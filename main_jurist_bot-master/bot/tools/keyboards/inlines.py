from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .config import *


def main_menu_btn():
    builder = InlineKeyboardBuilder()
    for index, value in enumerate(menu_buttons.values()):
        if value == menu_buttons['Lawyers']:
            builder.row(InlineKeyboardButton(text=f'{value} ', web_app=WebAppInfo(url='https://b517-5-35-81-229.ngrok-free.app')))
        else:
            builder.row(InlineKeyboardButton(text=f'{value} ', callback_data=f'menu:'+str(index)))

    return builder.as_markup()


def back_btn(text: str, callback: str):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text=f'{text}', callback_data= f'{callback}'))
    return builder.as_markup()


def main_menu_for_pay():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=f'Оплатить услуги Юристов', pay=True))
    builder.row(InlineKeyboardButton(text=f'Возврат в главное меню', callback_data='back_main_menu'))

    return builder.as_markup()

