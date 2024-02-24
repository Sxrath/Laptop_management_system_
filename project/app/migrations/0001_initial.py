# Generated by Django 4.2.7 on 2023-11-25 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=20, unique=True)),
                ('model', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.condition')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out_time', models.DateTimeField()),
                ('check_in_time', models.DateTimeField(blank=True, null=True)),
                ('is_late', models.BooleanField(default=False)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.laptop')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_time', models.DateTimeField()),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.laptop')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]