from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.views import UsersQueueViewSet, AddUserAndRemoveFromQueue
from apps.cost_account.views import CostAccountHistoryViewSet

router = routers.SimpleRouter()
router.register(r'users_queue', UsersQueueViewSet)
router.register(r'cost_history', CostAccountHistoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('add_user_from_queue/<int:chat_id>/', AddUserAndRemoveFromQueue.as_view(), name='add_user_from_queue'),
]

urlpatterns += router.urls
