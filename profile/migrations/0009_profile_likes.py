# Generated by Django 3.2.9 on 2021-12-30 23:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0008_auto_20211230_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='likes',
            field=models.ManyToManyField(
                blank=True, related_name='profile_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
