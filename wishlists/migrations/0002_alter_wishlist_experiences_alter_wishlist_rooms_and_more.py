# Generated by Django 5.0.4 on 2024-04-25 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiences", "0003_experience_category_alter_experience_host_and_more"),
        ("rooms", "0003_remove_amenity_category_room_category_and_more"),
        ("wishlists", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="experiences",
            field=models.ManyToManyField(
                related_name="wishlists", to="experiences.experience"
            ),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="rooms",
            field=models.ManyToManyField(related_name="wishlists", to="rooms.room"),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wishlists",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]