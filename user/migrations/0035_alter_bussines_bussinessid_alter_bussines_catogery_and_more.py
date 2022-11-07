# Generated by Django 4.1 on 2022-09-23 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_merge_20220923_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussines',
            name='bussinessId',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='catogery',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='locations',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='serviceTime',
            field=models.TextField(max_length=2255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
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