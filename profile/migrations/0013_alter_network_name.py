# Generated by Django 3.2.9 on 2022-02-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0012_auto_20220206_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='name',
            field=models.CharField(blank=True, choices=[('YOUTUBE', 'youtube'), ('WHATSAPP', 'whatsapp'), ('FACEBOOK', 'facebook'), ('INSTAGRAM', 'instagram'), ('TWITTER', 'twitter'), (
                'PINTEREST', 'pinterest'), ('SNAPCHAT', 'snapchat'), ('TIKTOK', 'tiktok'), ('DISCORD', 'discord'), ('GITHUB', 'Github')], max_length=10, null=True),
        ),
    ]