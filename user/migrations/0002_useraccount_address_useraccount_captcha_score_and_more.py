# Generated by Django 5.1.1 on 2024-09-23 17:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="address",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Address"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="captcha_score",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="country",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Country"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="has_profile",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="latitude",
            field=models.FloatField(
                blank=True, max_length=50, null=True, verbose_name="Latitude"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="longitude",
            field=models.FloatField(
                blank=True, max_length=50, null=True, verbose_name="Longitude"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="post_code",
            field=models.CharField(
                blank=True, max_length=8, null=True, verbose_name="Post Code"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="useraccount",
            name="town",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Town/City"
            ),
        ),
        migrations.AddField(
            model_name="useraccount",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
