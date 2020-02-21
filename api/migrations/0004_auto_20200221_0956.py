# Generated by Django 2.2.10 on 2020-02-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200221_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='api.Product'),
        ),
    ]
