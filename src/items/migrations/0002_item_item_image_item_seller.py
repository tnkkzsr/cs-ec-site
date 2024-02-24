# Generated by Django 4.2.10 on 2024-02-23 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import items.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(blank=True, null=True, storage=items.models.CustomFileSystemStorage(), upload_to=items.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]