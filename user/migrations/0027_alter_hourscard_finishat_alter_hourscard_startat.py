# Generated by Django 4.0.6 on 2022-08-28 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_alter_hourscard_finishat_alter_hourscard_startat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourscard',
            name='finishAt',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 8, 28, 17, 36, 6, 494895)),
        ),
        migrations.AlterField(
            model_name='hourscard',
            name='startAt',
            field=models.TimeField(default=datetime.datetime(2022, 8, 28, 17, 36, 6, 494895)),
        ),
    ]