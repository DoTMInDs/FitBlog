# Generated by Django 5.1.5 on 2025-01-31 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_artist_artist_song_remove_artist_song_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='song_artist_name',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='artist_name',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='song_genre',
        ),
    ]
