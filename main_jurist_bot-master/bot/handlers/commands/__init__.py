from aiogram import Dispatcher
from .main import *


def register_handlers(dp: Dispatcher):
    dp.message.register(start_bot, CommandStart(), IsPrivate())
    dp.message.register(menu, Command('menu'), IsPrivate() )


