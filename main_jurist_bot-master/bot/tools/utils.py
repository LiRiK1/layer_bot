import re
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramAPIError
from .database import *


async def delete_last_message(event: types.Message | types.CallbackQuery, state: FSMContext):
    try:
        last_message_id = await state.get_data()
        try:
            message_id = last_message_id['last_msg_id']
            await event.bot.delete_message(chat_id=event.from_user.id, message_id=message_id)
        except KeyError as e:
            pass

    except TelegramAPIError as e:
        if "Message to delete not found" in str(e):
            print(f"Тип ошибки: {str(e)}")


async def send_message(event: types.Message | types.CallbackQuery, state: FSMContext, text: str,
                       markup: ReplyKeyboardMarkup | InlineKeyboardMarkup = None):
    await delete_last_message(event, state)

    message = await event.bot.send_message(chat_id=event.from_user.id, text=text, reply_markup=markup)
    await state.update_data(last_msg_id = message.message_id)

async def is_email(text):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    text = str(text)
    if re.match(pattern, text):
        return True
    else:
        return False