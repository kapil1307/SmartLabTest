# Generated by Django 3.2.13 on 2022-06-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SL_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='CCA_C_STATUS',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='ITP_C_STATUS',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='UART_C_STATUS',
            field=models.BooleanField(default=True),
        ),
    ]
