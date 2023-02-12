# Generated by Django 4.1.5 on 2023-02-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_logger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('guest_count', models.IntegerField()),
                ('reservation_time', models.DateField(auto_now=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='logger',
            name='time_log',
            field=models.TimeField(help_text='Enter the current time'),
        ),
    ]
