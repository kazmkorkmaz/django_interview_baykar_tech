# Generated by Django 4.2.8 on 2023-12-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykar_tech_uav_rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='d', unique=True),
            preserve_default=False,
        ),
    ]
