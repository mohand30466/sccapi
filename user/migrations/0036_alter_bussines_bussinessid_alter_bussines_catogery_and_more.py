# Generated by Django 4.1 on 2022-09-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0035_alter_bussines_bussinessid_alter_bussines_catogery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussines',
            name='bussinessId',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='catogery',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='locations',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bussines',
            name='serviceTime',
            field=models.TextField(blank=True, max_length=2255),
        ),
    ]