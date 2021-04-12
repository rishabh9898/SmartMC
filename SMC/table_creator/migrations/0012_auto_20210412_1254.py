# Generated by Django 3.1.6 on 2021-04-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_creator', '0011_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartmc',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='smartmc',
            name='place_in',
        ),
        migrations.RemoveField(
            model_name='smartmc',
            name='receive_by',
        ),
        migrations.AddField(
            model_name='smartmc',
            name='pill_Box1',
            field=models.CharField(blank=True, choices=[('Pill Box-1', 'Pill Box-1')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='smartmc',
            name='pill_Box2',
            field=models.CharField(blank=True, choices=[('Pill Box-2', 'Pill Box-2')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='smartmc',
            name='pill_Box3',
            field=models.CharField(blank=True, choices=[('Pill Box-3', 'Pill Box-3')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='smartmc',
            name='pill_Box4',
            field=models.CharField(blank=True, choices=[('Pill Box-4', 'Pill Box-4')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='smartmc',
            name='total_quantity',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
