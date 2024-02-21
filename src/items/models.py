from django.db import models


class Item(models.Model):
    item_title = models.CharField(max_length=100)
    item_explain = models.TextField()
    item_category = models.CharField(max_length=100)
    item_condition = models.CharField(max_length=100)
    item_price = models.IntegerField()
    # seller = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return self.item_title


