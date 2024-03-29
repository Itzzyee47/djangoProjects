# Generated by Django 4.2.4 on 2023-11-03 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itech', '0006_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, default=None, upload_to='post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='ur_details',
            name='coverPhoto',
            field=models.ImageField(blank=True, default=None, upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='ur_details',
            name='proPic',
            field=models.ImageField(blank=True, default=None, upload_to='proPics'),
        ),
        migrations.AlterField(
            model_name='ur_details',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
