import config
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from bot.tools.database import create_tables

def register_handlers(dp: Dispatcher):
    from .handlers import commands, userReg, personalAccount, payServices, selectedJurist
    commands.register_handlers(dp)
    userReg.register_handlers(dp)
    personalAccount.register_handlers(dp)
    payServices.register_handlers(dp)
    selectedJurist.register_handlers(dp)


async def start_bot():
    bot = Bot(token=config.TOKEN, parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())
    register_handlers(dp)
    await create_tables()
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        print('Lets go, people...')
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

