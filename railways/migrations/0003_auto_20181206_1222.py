# Generated by Django 2.1.4 on 2018-12-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0002_ride_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='station',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]