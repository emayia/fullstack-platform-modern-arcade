# Generated by Django 4.2.18 on 2025-01-16 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0011_user_is_in_game_user_refresh_token_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='refresh_token',
        ),
    ]
