from . import models
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import desc,select, update
from .engine_db import engine


async_session = async_sessionmaker(engine)

async def add_user(user_data):
    async with async_session() as session:
        new_user = models.User(
            **user_data
        )
        session.add(new_user)
        await session.commit()

async def check_user_data(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(models.User).where(models.User.telegram_id == tg_id))

        if user is not None:
            return user
        else:
            return None

async def get_wallet(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(models.User).where(models.User.telegram_id == tg_id))

        if user!= None:
            return user.wallet

async def get_jurists_for_user(tg_id):
    async with async_session() as session:
        result = await session.execute(
            select(
                models.JuristName.first_name,
                models.JuristName.email,
                models.JuristName.phone_number
            )
            .join(models.Payment, models.JuristName.id == models.Payment.jurist_id)
            .join(models.User, models.User.id == models.Payment.user_id)
            .where(models.User.telegram_id == tg_id)
        )
        jurists = result.all()
        return jurists

async def set_wallet(tg_id, coin):
    async with async_session() as session:
        user = await session.scalar(select(models.User).where(models.User.telegram_id == tg_id))

        if user!= None:
            user.wallet += coin
        await session.commit()

async def get_user_summary(tg_id):
    async with async_session() as session:
        result = await session.execute(
            select(
                models.User.user_phone,
                models.User.user_mail,
                models.User.wallet,
                models.User.date_register
            ).where(models.User.telegram_id == tg_id)
        )
        user_summary = result.one_or_none()
        return user_summary