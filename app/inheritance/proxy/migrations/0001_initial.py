# Generated by Django 2.1.2 on 2018-10-12 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='이름')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
            ],
            options={
                'db_table': 'Inheritance_Proxy_User1',
            },
        ),
    ]