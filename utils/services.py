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
