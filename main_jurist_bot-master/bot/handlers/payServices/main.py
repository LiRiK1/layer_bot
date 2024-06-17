import random
from bot.tools.keyboards import *
from aiogram import types
from bot.tools import database, utils, fsm
from aiogram.fsm.context import FSMContext
from datetime import datetime


async def pay(callback: types.CallbackQuery):
    await callback.bot.send_invoice(
        chat_id=callback.message.chat.id,
        title='Оплата "Юрист-бот"',
        description='Пополнение счета',
        payload='Payment',
        provider_token='381764678:TEST:85979',
        currency='rub',
        prices=[
            types.LabeledPrice(
                label='Юристы',
                amount=50000
            ),
            types.LabeledPrice(
                label='НДС',
                amount=0
            )
        ],
        max_tip_amount=50000,
        suggested_tip_amounts=[1000, 2000],
        start_parameter='nztcoder',
        provider_data=None,
        reply_markup=inlines.main_menu_for_pay(),
        need_name=True,
        need_email=True,
        protect_content=True,
        request_timeout=15
        )
    await callback.answer()

async def pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    if pre_checkout_query.total_amount > 0 and pre_checkout_query.currency == "RUB":
        await pre_checkout_query.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
        await pre_checkout_query.bot.send_message(chat_id=pre_checkout_query.from_user.id,
                               text="Ваша оплата прошла успешно!")
        await pre_checkout_query.bot.send_message(chat_id=pre_checkout_query.from_user.id,
                               text="Главное меню",
                               reply_markup=inlines.main_menu_btn())
        user_coin = int(pre_checkout_query.total_amount)/100

        await database.set_wallet(pre_checkout_query.from_user.id, coin=user_coin)

    else:
        await pre_checkout_query.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=False,
                                            error_message="Вы не оплатили заказ. Пожалуйста, оплатите заказ, прежде чем продолжить.")


async def return_to_main_menu_from_pay(callback:types.CallbackQuery):
    await callback.answer("Вы отменили оплату")
    await callback.message.answer("Ваша оплата отменена", reply_markup=inlines.main_menu_btn())
