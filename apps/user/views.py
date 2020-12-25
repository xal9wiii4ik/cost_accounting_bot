from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework import status, permissions

from apps.user.models import UserQueue
from apps.user.serializers import UsersQueueModelSerializer
from apps.user.services_views import verification_user, add_user_and_remove_from_user_queue


class UsersQueueViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    """View Set для модели очереди пользователей"""

    queryset = UserQueue.objects.all()
    serializer_class = UsersQueueModelSerializer
    permission_classes = (permissions.IsAdminUser,)

    def create(self, request, *args, **kwargs) -> Response:
        if verification_user(request.data['chat_id']):
            return super(UsersQueueViewSet, self).create(request, *args, **kwargs)
        else:
            return Response(data={'error': 'User already exist'},
                            status=status.HTTP_400_BAD_REQUEST)


class AddUserAndRemoveFromQueue(APIView):
    """
    Добавление пользователя и удаление его из очереди
    и отправка уведомления
    """

    def get(self, request, chat_id: int) -> Response:
        add_user_and_remove_from_user_queue(chat_id=chat_id)
        return Response(data={'ok': 'User has been added'},
                        status=status.HTTP_201_CREATED)

