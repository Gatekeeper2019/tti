# Generated by Django 2.0.7 on 2019-11-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttipanel', '0005_auto_20191128_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarterly_church_planting_update_form',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
