import json
import requests

from django_back_end import settings


def get_data_from_request(path: str) -> list:
    """Get data from request"""

    response = requests.get(url=settings.SERVER_HOST.replace('path', path),
                            headers={
                                'Authorization': settings.AUTHORIZATION_TOKEN
                            })
    return json.loads(response._content.decode('utf-8'))


def get_data_from_request_with_chat_id(path: str, chat_id: int) -> list:
    """Get data from request with chat_id"""

    response = requests.get(url=settings.SERVER_HOST.replace('path', path),
                            headers={
                                'Authorization': settings.AUTHORIZATION_TOKEN
                            }, json={'chat_id': chat_id})
    return json.loads(response._content.decode('utf-8'))


def check_user_permission(chat_id: int) -> bool:
    """Check permission of user"""

    users = get_data_from_request(path='users')
    for user in users:
        if chat_id == user['chat_id']:
            return True
    return False
