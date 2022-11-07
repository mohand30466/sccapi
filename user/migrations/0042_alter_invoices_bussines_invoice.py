# Generated by Django 4.0 on 2022-11-07 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_remove_invoices_bussiness_invoices_bussines_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='bussines',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='myInvoices', to='user.bussines'),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceType', models.CharField(max_length=255)),
                ('issueAt', models.DateField(default=True)),
                ('reciverName', models.CharField(max_length=255)),
                ('reciverId', models.CharField(max_length=255)),
                ('reciverEmail', models.CharField(max_length=255)),
                ('invoiceDetail', models.TextField(max_length=255)),
                ('invoiceAmount', models.CharField(max_length=255)),
                ('invoiceTax', models.BooleanField(default=True)),
                ('paymentTill', models.DateField(default=True)),
                ('bussines', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='myInvoice', to='user.bussines')),
            ],
        ),
    ]
