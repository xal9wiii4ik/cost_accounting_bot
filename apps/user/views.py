import asyncio

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework import status, permissions

from apps.user.models import UserQueue, CustomUser
from apps.user.serializers import UsersQueueModelSerializer, CustomUserModelSerializer
from apps.user.services_views import (
    verification_user,
    add_user_and_remove_from_user_queue
)
from handlers.users.start import add_user


class CustomUserViewSet(mixins.ListModelMixin,
                        GenericViewSet):
    """View for CustomUser"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
    permission_classes = (permissions.IsAdminUser,)


class UsersQueueViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):
    """View Set for UserQueue"""

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
    View for AddUserAndRemoveFromQueue
    """

    def get(self, request, chat_id: int) -> Response:
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop=loop)
        finally:
            add_user_and_remove_from_user_queue(chat_id=chat_id)
            loop.run_until_complete(add_user(chat_id=chat_id))
        return Response(data={'ok': 'User has been added'},
                        status=status.HTTP_201_CREATED)
