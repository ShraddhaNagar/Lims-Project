# Generated by Django 4.2.10 on 2024-03-06 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_requisitionitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisitionitem',
            name='discount',
            field=models.CharField(default='DEFAULT_VALUE', max_length=100),
        ),
        migrations.AlterField(
            model_name='requisitionitem',
            name='quantity',
            field=models.CharField(max_length=100),
        ),
    ]
