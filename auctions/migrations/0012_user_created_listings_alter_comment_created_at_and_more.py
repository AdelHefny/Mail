# Generated by Django 5.0.2 on 2024-02-26 13:59

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_comment_created_at_alter_listing_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_listings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 15, 59, 27, 983044)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 26, 15, 59, 27, 983044)),
        ),
    ]