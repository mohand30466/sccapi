# Generated by Django 4.0 on 2022-11-07 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_alter_paysleeve_finalamount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actions', models.CharField(max_length=255)),
                ('time', models.DateField(default=True)),
                ('isFinish', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='list', to='user.user')),
            ],
        ),
    ]