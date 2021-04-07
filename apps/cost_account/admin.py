from django.contrib import admin

from apps.cost_account.models import CostAccountHistory


@admin.register(CostAccountHistory)
class CostAccountHistoryAdmin(admin.ModelAdmin):
    """Display cost account history if admin panel"""

    list_display = ['id', 'chat_id', 'name_spending', 'price_spending', 'date']
