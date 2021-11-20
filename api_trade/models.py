from django.db import models

class Trade(models.Model):
    trade_types = models.TextChoices('trade_types', 'sell buy')
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(choices=trade_types.choices, max_length=4)
    user_id = models.BigIntegerField()
    symbol = models.CharField(max_length=3)
    shares = models.IntegerField()
    price = models.IntegerField()
    timestamp = models.IntegerField()
