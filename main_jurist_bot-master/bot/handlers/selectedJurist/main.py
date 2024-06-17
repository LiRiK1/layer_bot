import random
from bot.tools.keyboards import *
from aiogram import types
from bot.tools import database, utils, fsm
from aiogram.fsm.context import FSMContext
from datetime import datetime


async def send_jurists(callback: types.CallbackQuery):
    tg_id = callback.from_user.id
    jurists = await database.get_jurists_for_user(tg_id)
    if jurists:
        response_message = "Список юристов:\n\n"
        for jurist in jurists:
            first_name, email, phone_number = jurist
            response_message += f'Имя: {first_name}\nEmail: {email}\nТелефон: {phone_number}\n\n'
        await callback.message.answer(response_message, reply_markup=inlines.back_btn('⬅️ в Меню','back_main_menu'))
    else:
        await callback.message.answer('Юристы не найдены', reply_markup=inlines.back_btn('⬅️ в Меню','back_main_menu'))