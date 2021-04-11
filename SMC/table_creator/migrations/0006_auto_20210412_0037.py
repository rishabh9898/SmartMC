# Generated by Django 3.1.6 on 2021-04-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_creator', '0005_auto_20210411_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartmc',
            name='receive_quantity',
        ),
        migrations.AddField(
            model_name='smartmc',
            name='place_in',
            field=models.CharField(blank=True, choices=[('Pill Box-1', 'Pill Box-2'), ('Pill Box-3', 'Pill Box-4')], max_length=50, null=True),
        ),
    ]
