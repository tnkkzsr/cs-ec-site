# Generated by Django 4.2.11 on 2024-03-08 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0004_item_likeusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_item', to='items.item')),
                ('purchaser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
