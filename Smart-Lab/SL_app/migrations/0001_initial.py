# Generated by Django 3.2.6 on 2022-02-03 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('use_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'admin',
            },
        ),

        migrations.CreateModel(
            name='LAB',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('DUT_ID', models.CharField(max_length=500)),
                ('SUT_NAME', models.CharField(max_length=500)),
                ('ITP_C_STATUS', models.BooleanField(default='yes')),
                ('DEBUG_SERVER_IP', models.CharField(max_length=500)),
                ('CCA_C_STATUS', models.BooleanField(default='yes')),
                ('TEST_SERVER_IP', models.CharField(max_length=500)),
                ('UART_C_STATUS', models.BooleanField(default='yes')),
                ('TEST_PC_IP', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'lab',
            },
        ),
        migrations.CreateModel(
            name='SL_Master',
            fields=[
                ('ORG_CODE', models.CharField(max_length=500)),
                ('DOMAIN_CODE', models.CharField(max_length=500)),
                ('SUBDOMAIN_CODE', models.CharField(max_length=500)),
                ('PRODUCT_NAME', models.CharField(max_length=500)),
                ('PRODUCT_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('SERIAL_ID', models.CharField(max_length=255, unique=True)),
                ('ISACTIVE', models.BooleanField(default='yes')),
            ],
            options={
                'db_table': 'sl_master',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('use_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='SL_DEVICE_LIST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORG_CODE', models.CharField(max_length=400)),
                ('DOMAIN_CODE', models.CharField(max_length=400)),
                ('SUBDOMAIN_CODE', models.CharField(max_length=400)),
                ('SERIAL_ID', models.CharField(max_length=255, unique=True)),
                ('STATUS', models.BooleanField(default=True)),
                ('ISACTIVE', models.BooleanField(default=True)),
                ('SPECIFICATION', models.CharField(max_length=1000)),
                ('LAB_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SL_app.lab')),
                ('PRODUCT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SL_app.sl_master')),
            ],
            options={
                'db_table': 'sl_device_list',
            },
        ),
    ]
