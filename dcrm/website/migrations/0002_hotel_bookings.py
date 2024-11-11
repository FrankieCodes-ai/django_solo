# Generated by Django 5.1.2 on 2024-11-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel_bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_booking_date', models.DateTimeField()),
                ('hotel_date_arrive', models.DateTimeField()),
                ('hotel_date_leave', models.DateTimeField()),
                ('hotel_adults', models.IntegerField(default=0)),
                ('hotel_children', models.IntegerField(default=0)),
                ('hotel_total_cost', models.FloatField(default=0)),
            ],
        ),
    ]