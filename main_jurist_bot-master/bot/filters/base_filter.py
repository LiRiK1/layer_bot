from bot.tools import database, utils


async def check_new_users(user_id):
    if await database.check_user_data(user_id) == None:
        return True
    else:
        return False
