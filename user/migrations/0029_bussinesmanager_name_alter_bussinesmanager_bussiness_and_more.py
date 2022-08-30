# Generated by Django 4.0.6 on 2022-08-30 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_alter_hourscard_finishat_alter_hourscard_startat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussinesmanager',
            name='name',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bussinesmanager',
            name='bussiness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bussines', to='user.bussines'),
        ),
        migrations.AlterField(
            model_name='bussinesmanager',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hourscard',
            name='day',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='hourscard',
            name='finishAt',
            field=models.TimeField(default=True),
        ),
        migrations.AlterField(
            model_name='hourscard',
            name='startAt',
            field=models.TimeField(default=True),
        ),
    ]
