# Generated by Django 3.1.3 on 2020-12-14 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_auto_20201214_1643"),
    ]

    operations = [
        migrations.RenameField(
            model_name="watchlist",
            old_name="item",
            new_name="listing",
        ),
    ]
