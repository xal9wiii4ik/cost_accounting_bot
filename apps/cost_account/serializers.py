from rest_framework import serializers

from apps.cost_account.models import CostAccountHistory


class CostAccountHistoryModelSerializer(serializers.ModelSerializer):
    """Serializer for CostAccountHistory model"""

    class Meta:
        model = CostAccountHistory
        fields = '__all__'
