# Generated by Django 2.1.2 on 2018-10-12 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=80)),
            ],
            options={
                'db_table': 'Inheritance_Multitable_Place',
            },
        ),
        migrations.CreateModel(
            name='Restaurant1',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multi_table.Place1')),
                ('serves_hot_dogs', models.BooleanField(default=False)),
                ('serves_pizza', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Inheritance_Multitable_Restaurant',
            },
            bases=('multi_table.place1',),
        ),
    ]
