# Generated by Django 2.2.10 on 2020-02-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200221_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='msisdn',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pin',
            field=models.IntegerField(),
        ),
    ]
