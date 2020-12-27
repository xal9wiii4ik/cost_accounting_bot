import json
import requests
import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline.approval_spending_keyboard import markup
from states.spending_state import SpendingState
from django_back_end import settings


@dp.message_handler(commands=['add_spending'])
async def add_spending(message: types.Message) -> None:
    """Добавление расхода"""

    await SpendingState.EnterSpending.set()
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text='Enter your spending in belorussian rubles.\n'
                                   'For example: такси 3, мтс 26, etc.')


@dp.message_handler(state=SpendingState.EnterSpending)
async def enter_name_of_spending(message: types.Message, state: FSMContext) -> None:
    """Ввод названия расхода с подтверждением"""

    try:
        price = float(message.text.split()[-1])
    except ValueError:
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text='Error check your message and do restart(/add_spending)')
        await state.reset_state()
    else:
        await state.update_data(
            name=message.text.split()[0],
            price=price
        )
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text=f'You enter name: {message.text.split()[0]} and \n'
                                       f'price: {price}', reply_markup=markup)
        await SpendingState.Approval.set()


@dp.callback_query_handler(text_contains='reset', state=SpendingState.Approval)
async def reset(call: CallbackQuery, state: FSMContext):
    """Если пользователь нажал ресет"""

    await state.reset_state()
    await dp.bot.send_message(chat_id=call.from_user.id,
                              text='You press reset. For restart(/add_spending)')


@dp.callback_query_handler(text_contains='yes', state=SpendingState.Approval)
async def reset(call: CallbackQuery, state: FSMContext):
    """Если пользователь нажал ресет"""

    data = await state.get_data()
    post_data = {
        'chat_id': call.from_user.id,
        'name_spending': data['name'],
        'price_spending': data['price']
    }
    response = requests.post(url=settings.SERVER_HOST.replace('path', 'cost_history'),
                             json=post_data,
                             headers=settings.HEADERS)
    if response.status_code == 201:
        await dp.bot.send_message(chat_id=call.from_user.id,
                                  text=f'Im adding {data["name"]} {data["price"]} to your history.\n'
                                       f'To check all your history enter /my_all_history.\n'
                                       f'To check your history for this month enter /my_history_for_month.\n'
                                       f'Thanks for using me!)')
    else:
        await dp.bot.send_message(chat_id=call.from_user.id,
                                  text='Sorry, something wrong')

    await state.reset_state()


@dp.message_handler(commands=['my_history_for_month'])
async def my_history_for_month(message: types.Message) -> None:
    """Узнать историю за месяц"""

    response = requests.get(url=settings.SERVER_HOST.replace('path', 'cost_history'),
                            headers={
                                'Authorization': settings.AUTHORIZATION_TOKEN
                            }, json={'chat_id': message.from_user.id})
    datas = json.loads(response._content.decode('utf-8'))
    date_now = datetime.datetime.now()
    all_price = 0
    for data in datas:
        date = datetime.datetime.strptime(data['date'], '%Y-%m-%d')
        if date.month == date_now.month:
            all_price += float(data['price_spending'])
            await dp.bot.send_message(chat_id=message.from_user.id,
                                      text=f'{data["date"]}:\n'
                                           f'name: {data["name_spending"]}\n'
                                           f'price: {data["price_spending"]}\n')
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=f'At now you spend {all_price}')


@dp.message_handler(commands=['my_history'])
async def my_history(message: types.Message) -> None:
    """Узнать всю историю"""

    response = requests.get(url=settings.SERVER_HOST.replace('path', 'cost_history'),
                            headers={
                                'Authorization': settings.AUTHORIZATION_TOKEN
                            }, json={'chat_id': message.from_user.id})
    datas = json.loads(response._content.decode('utf-8'))
    for data in datas:
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text=f'{data["date"]}:\n'
                                       f'name: {data["name_spending"]}\n'
                                       f'price: {data["price_spending"]}\n')
