# Generated by Django 4.1.1 on 2022-10-06 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_post_released_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 6, 9, 19, 35, 234307)),
        ),
    ]