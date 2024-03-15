import os
import shutil

from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from account.models import CustomFileSystemStorage, User


# ファイルアップロード時にユーザーIDをフォルダ名として使用する
def user_directory_path(instance, filename):
    return f'item_images/item_{instance.id}/{filename}'

# 出品する商品テーブル
class Item(models.Model):
    item_title = models.CharField(max_length=100)
    item_explain = models.TextField()
    item_category = models.CharField(max_length=100)
    item_condition = models.CharField(max_length=100)
    item_price = models.IntegerField(validators=[MinValueValidator(50), MaxValueValidator(9999999)])
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True, storage=CustomFileSystemStorage())
    likes = models.IntegerField(default=0, blank=True, null=True)
    LikeUsers = models.ManyToManyField(User, related_name='user', blank=True)
    is_bought = models.BooleanField(default=False, blank=True)


    def __str__(self):
        return self.item_title
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.item_image
            self.item_image = None
            super().save(*args, **kwargs)
            self.item_image = saved_image
            if "force_insert" in kwargs:
                kwargs.pop("force_insert")
        super().save(*args, **kwargs)
    
    
'''class Like(models.Model):
    item_id = '''








