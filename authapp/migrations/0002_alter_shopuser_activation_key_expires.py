# Generated by Django 3.2.6 on 2021-10-16 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 18, 17, 45, 38, 85451, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]