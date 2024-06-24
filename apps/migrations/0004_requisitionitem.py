# Generated by Django 4.2.10 on 2024-03-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_incomingmaterial_grade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequisitionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('product_code', models.CharField(max_length=100)),
                ('make_brand', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=20)),
                ('pack_size', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('coa_coc_required', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
