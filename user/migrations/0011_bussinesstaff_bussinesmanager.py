# Generated by Django 4.0.6 on 2022-08-21 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_bussines'),
    ]

    operations = [
        migrations.CreateModel(
            name='BussinesStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('staffId', models.CharField(max_length=255)),
                ('bussines', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='bussines', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BussinesManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bussiness', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='bussines', to='user.bussines')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
