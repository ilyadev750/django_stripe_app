# Generated by Django 4.2.7 on 2024-02-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price_id',
            field=models.CharField(max_length=100, null=True, verbose_name='Идентификатор на stripe'),
        ),
    ]
