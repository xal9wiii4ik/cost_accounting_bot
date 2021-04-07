from django.db import models


class CostAccountHistory(models.Model):
    """Cost account history model"""

    chat_id = models.BigIntegerField(verbose_name='Айди чата пользователя')
    name_spending = models.CharField(max_length=90, verbose_name='Имя расхода')
    price_spending = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена расхода')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'id: {id}, chat_id: {self.chat_id}, name spending: {self.name_spending}, ' \
               f'price spending: {self.price_spending}, date: {self.date}'

    class Meta:
        verbose_name = 'История расходов'
        verbose_name_plural = 'Истории расходов'
