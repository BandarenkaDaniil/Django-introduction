# Generated by Django 2.1.4 on 2019-01-10 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0003_auto_20190110_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides', to='railways.Route'),
        ),
    ]