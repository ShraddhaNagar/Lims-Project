# Generated by Django 4.2.10 on 2024-03-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
