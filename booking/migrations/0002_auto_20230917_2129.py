# Generated by Django 3.2.21 on 2023-09-17 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('table_number', models.IntegerField(default=0, unique=True)),
                ('seats', models.IntegerField(default=2)),
            ],
            options={
                'ordering': ['-seats'],
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table_booked', to='booking.table'),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('booking_date', 'booking_time', 'table')},
        ),
    ]