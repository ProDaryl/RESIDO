# Generated by Django 5.1.1 on 2024-09-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_listing_parking_space_listing_photo_10_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='state',
            new_name='region',
        ),
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]