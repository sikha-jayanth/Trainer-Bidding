# Generated by Django 3.1.2 on 2020-11-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0011_auto_20201124_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='location',
            field=models.CharField(default='location', max_length=120),
        ),
    ]