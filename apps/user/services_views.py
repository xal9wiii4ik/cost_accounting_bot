from django.contrib.auth.hashers import make_password
from django_back_end.settings import PASSWORD

from apps.user.models import (
    CustomUser,
    UserQueue,
)


def add_user_and_remove_from_user_queue(chat_id: int) -> None:
    """add user and remove him from queue"""

    user_in_queue = UserQueue.objects.get(chat_id=chat_id)
    CustomUser.objects.create(username=user_in_queue.username,
                              chat_id=user_in_queue.chat_id,
                              first_name=user_in_queue.first_name,
                              last_name=user_in_queue.last_name,
                              password=make_password(password=PASSWORD))
    user_in_queue.delete()


def verification_user(chat_id: int) -> bool:
    """check user in database(if him exist)"""

    user = CustomUser.objects.filter(chat_id=chat_id)
    if len(user) == 1:
        return False
    else:
        return True
