import json
import requests

from django_back_end import settings


def get_data_from_request(path: str) -> list:
    """Получение данных из запроса"""

    response = requests.get(url=settings.SERVER_HOST.replace('path', path),
                            headers={
                                'Authorization': settings.AUTHORIZATION_TOKEN
                            })
    return json.loads(response._content.decode('utf-8'))


def check_user_permission(chat_id: int) -> bool:
    """Проверка добавлен ли пользователь администратором"""

    users = get_data_from_request(path='users')
    for user in users:
        if chat_id == user['chat_id']:
            return True
    return False
