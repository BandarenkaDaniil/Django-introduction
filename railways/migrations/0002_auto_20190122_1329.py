# Generated by Django 2.1.4 on 2019-01-22 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('railways', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('amount', models.PositiveIntegerField()),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='railways.Ride')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
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
            model_name='track',
            name='arrival_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_tracks', to='railways.Station'),
        ),
        migrations.AlterField(
            model_name='track',
            name='departure_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcoming_tracks', to='railways.Station'),
        ),
        migrations.AddField(
            model_name='train',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trains', to='railways.Route'),
        ),
        migrations.AddField(
            model_name='ride',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides', to='railways.Route'),
        ),
    ]
