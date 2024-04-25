# Generated by Django 5.0.4 on 2024-04-25 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dms", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="chattingroom",
            name="users",
            field=models.ManyToManyField(
                related_name="chatting_rooms", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="dms.chattingroom",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="messages",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
