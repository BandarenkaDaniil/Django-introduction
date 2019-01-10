# Generated by Django 2.1.4 on 2019-01-10 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railways', '0004_auto_20190110_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='arrival_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_routes', to='railways.Station'),
        ),
        migrations.AlterField(
            model_name='route',
            name='departure_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcoming_routes', to='railways.Station'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='railways.Ride'),
        ),
        migrations.AlterField(
            model_name='track',
            name='arrival_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_tracks', to='railways.Station'),
        ),
        migrations.AlterField(
            model_name='track',
            name='departure_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcoming_tracks', to='railways.Station'),
        ),
        migrations.AlterField(
            model_name='train',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trains', to='railways.Route'),
        ),
    ]
