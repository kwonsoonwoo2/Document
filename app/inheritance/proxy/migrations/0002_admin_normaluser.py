# Generated by Django 2.1.2 on 2018-10-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy.user1', models.Model),
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy.user1', models.Model),
        ),
    ]
