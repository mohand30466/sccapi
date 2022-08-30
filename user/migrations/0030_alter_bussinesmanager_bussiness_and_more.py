# Generated by Django 4.0.6 on 2022-08-30 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_bussinesmanager_name_alter_bussinesmanager_bussiness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussinesmanager',
            name='bussiness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bussinesManager', to='user.bussines'),
        ),
        migrations.AlterField(
            model_name='bussinesmanager',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bussinesstaff',
            name='bussines',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='busnessStaf', to='user.bussines'),
        ),
    ]
