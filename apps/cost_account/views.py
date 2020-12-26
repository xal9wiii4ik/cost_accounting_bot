from rest_framework.viewsets import mixins, GenericViewSet

from apps.cost_account.models import CostAccountHistory
from apps.cost_account.serializers import CostAccountHistoryModelSerializer


class CostAccountHistoryViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                GenericViewSet):
    """View Set для истории расходов"""

    queryset = CostAccountHistory.objects.all()
    serializer_class = CostAccountHistoryModelSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(chat_id=self.request.data['chat_id'])
        return query_set
