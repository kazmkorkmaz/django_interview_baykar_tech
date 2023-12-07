# Generated by Django 4.2.8 on 2023-12-07 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baykar_tech_uav_rental', '0003_uav_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('uav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykar_tech_uav_rental.uav')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
