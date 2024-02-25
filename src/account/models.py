import os
import shutil
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class CustomFileSystemStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_available_name(self, name, max_length=None):
        # ファイル名の重複を回避するために、ファイル名に一意のIDを付加します
        while self.exists(name):
            name = self.get_alternative_name(name)
        return name

    def _save(self, name, content):
        # ファイルを保存する前にフォルダを作成します
        dirname = os.path.dirname(name)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return super()._save(name, content)




def user_directory_path(instance, filename):
    # ファイルアップロード時にユーザーIDをフォルダ名として使用する
    return f'profile_images/user_{instance.id}/{filename}'

class User(AbstractUser):
    # 追加のフィールドを定義します
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True, storage=CustomFileSystemStorage())
    bio = models.TextField(blank=True, null=True)

class PaymentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_info')
    payment_details = models.CharField(max_length=255)
    # その他の支払い情報のフィールドを追加

    def __str__(self):
        return self.payment_details
    
@receiver(post_delete, sender=User)
def delete_profile_image_folder(sender, instance, **kwargs):
    # ユーザーが削除されたときにプロフィール画像フォルダを削除する関数
    if instance.profile_image:
        folder_path = instance.profile_image.path.rsplit('/', 1)[0]
        shutil.rmtree(folder_path)
        folder_path = f'media/item_images/{instance.id}'
        shutil.rmtree(folder_path, ignore_errors=True)