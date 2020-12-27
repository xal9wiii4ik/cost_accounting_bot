from rest_framework import serializers

from apps.user.models import UserQueue, CustomUser


class CustomUserModelSerializer(serializers.ModelSerializer):
    """Model serializer для модели черного списка пользователей"""

    class Meta:
        model = CustomUser
        fields = ['chat_id']


class UsersQueueModelSerializer(serializers.ModelSerializer):
    """Model serializer для модели очереди пользователей"""

    class Meta:
        model = UserQueue
        fields = '__all__'
