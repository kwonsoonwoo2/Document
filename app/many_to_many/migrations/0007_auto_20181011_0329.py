# Generated by Django 2.1.2 on 2018-10-11 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0006_auto_20181010_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_relations', related_query_name='from_user_relation', to='many_to_many.TwitterUser'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_relations', related_query_name='to_user_relation', to='many_to_many.TwitterUser'),
        ),
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together={('from_user', 'to_user')},
        ),
    ]
