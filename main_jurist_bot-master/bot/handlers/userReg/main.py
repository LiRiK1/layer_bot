import random
from bot.tools.keyboards import *
from aiogram import types
from bot.tools import database, utils, fsm
from aiogram.fsm.context import FSMContext
from datetime import datetime


async def set_user_name(msg: types.Message, state: FSMContext):
    await state.update_data(name = msg.text)
    await msg.answer(f'Напиши свой номер телефона в формате 7XXXXXXXXXX, что бы юрист смог с тобой экстренно связаться')
    await state.set_state(fsm.UserRegister.user_phone)

async def set_user_phone(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        text = msg.text
        if text.startswith('8'):
            text = '7' + text[1:]
        if len(text) == 11:
            await state.update_data(phone=msg.text)
            await msg.answer(f'Отлично! Введи свою почту')
            await state.set_state(fsm.UserRegister.user_mail)
        else:
            await msg.answer(text=f'Произошла ошибка. Возможно, вы ввели некорректный номер. '
                             f'Попробуйте ещё раз.')
    else:
        await msg.answer(text=f'Произошла ошибка. Возможно, вы ввели некорректный номер. '
                         f'Попробуйте ещё раз.')


async def set_user_mail(msg: types.Message, state:FSMContext):
    check_user_mail = await utils.is_email(msg.text)
    if check_user_mail:
        if await database.check_user_data(msg.from_user.id) == None:
            data = await state.get_data()
            name = data['name']
            phone = data['phone']
            try:
                tg_name = '@' + msg.from_user.username

            except TypeError as b:
                tg_name = 'NoneName'
            do_data = datetime.now().date()
            user_data = {
                'telegram_id': msg.from_user.id,
                'user_name': name,
                'tg_name': tg_name,
                'user_phone': phone,
                'user_mail': msg.text,
                'date_register': do_data
            }
            await database.add_user(user_data)
            await msg.answer(text=f'Вы зарегистрировались в боте!')
            await msg.answer(text=f'Главное меню', reply_markup=inlines.main_menu_btn())
        else:
            await msg.answer(text=f'Главное меню', reply_markup=inlines.main_menu_btn())
    else:
        await msg.answer(text=f'Произошла ошибка. Возможно, вы ввели некорректный адрес электронной почты. '
                         f'Попробуйте ещё раз.')