from bot.tools.keyboards import *
from aiogram import types
from bot.tools import database, utils
from aiogram.fsm.context import FSMContext



async def personal_account(callback: types.CallbackQuery, state: FSMContext):
    user_summary = await database.get_user_summary(callback.from_user.id)


    message = f'Ваш телефон: {user_summary.user_phone} \n' \
              f'Ваш Email {user_summary.user_mail}\n' \
              f'Ваш баланс {user_summary.wallet}\n' \
              f'Дата регистрации {user_summary.date_register}'

    await utils.send_message(callback, state,text=f'{message}',markup=inlines.back_btn('⬅️ в Меню','back_main_menu'))
    await callback.answer()

async def back_main_menu(callback: types.CallbackQuery, state: FSMContext):
    await utils.send_message(callback, state, text=f'Главное меню', markup=inlines.main_menu_btn())
    await callback.answer()
