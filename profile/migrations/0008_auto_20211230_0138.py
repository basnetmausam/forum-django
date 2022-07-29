# Generated by Django 3.2.9 on 2021-12-30 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0007_alter_network_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='network',
            options={'ordering': [
                'user'], 'verbose_name': 'Network', 'verbose_name_plural': 'Networks'},
        ),
        migrations.AlterField(
            model_name='network',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
