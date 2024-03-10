from django.db import models

from account.models import User
from items.models import Item


# Create your models here.
class Trade(models.Model):
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_user')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='payment_item')
    price = models.IntegerField()