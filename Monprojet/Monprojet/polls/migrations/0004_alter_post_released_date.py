# Generated by Django 4.1.1 on 2022-10-04 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 12, 3, 53, 9217)),
        ),
    ]