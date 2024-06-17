from aiogram.filters import Command, CommandStart
from bot.tools.keyboards import *
from aiogram import types
from bot.tools import database, utils, fsm
from aiogram.fsm.context import FSMContext
from bot.filters.check_private import IsPrivate
from bot.filters import base_filter


async def start_bot(msg: types.Message, state:FSMContext):
    new_user = await base_filter.check_new_users(msg.from_user.id)
    if new_user:
        await msg.answer(text=f'Привет! Это юридический бот который поможет вам найти нужного вам '
                              f'юриста в разных отрасл, написать ему можно прямо в боте!')
        await msg.answer(text=f'Давай познакомимся! Как тебя зовут?')
        await state.set_state(fsm.UserRegister.user_name)
    else:
        await msg.answer(text=f'Главное меню', reply_markup=inlines.main_menu_btn())


async def menu(msg: types.Message, state:FSMContext):
    await state.clear()
    await utils.send_message(msg,state,f'Главное меню:',markup=inlines.main_menu_btn())



