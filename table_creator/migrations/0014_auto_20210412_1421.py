# Generated by Django 3.1.6 on 2021-04-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_creator', '0013_auto_20210412_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartmc',
            name='pill_Box2',
        ),
        migrations.RemoveField(
            model_name='smartmc',
            name='pill_Box3',
        ),
        migrations.RemoveField(
            model_name='smartmc',
            name='pill_Box4',
        ),
        migrations.AlterField(
            model_name='smartmc',
            name='pill_Box1',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=50, null=True),
        ),
    ]
