import requests

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from django_back_end import settings


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message) -> None:
    """Команда /start"""

    data = {
        'chat_id': message.from_user.id,
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name
    }
    if data['username'] == None:
        data['username'] = 'debil with out username'
    response = requests.post(url=settings.SERVER_HOST.replace('path', 'users_queue'),
                             json=data, headers=settings.HEADERS, params=None)
    if response.status_code == 201:
        await message.answer(f'Привет! Вы оставили заявку на добавление ко мне)'
                             f'Администратор в скором времени рассмотрит вашу заявку!')
    else:
        await message.answer(f'Привет! Sorry something was wrong')


async def add_user(chat_id: int) -> None:
    await dp.bot.send_message(chat_id=chat_id, text='Администратор добавил вас '
                                                    'приносим извинения за ожидание')
