# Generated by Django 4.2.7 on 2023-11-25 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=300)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.laptop')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Studentprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.feedback')),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.laptop')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.reservation')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
