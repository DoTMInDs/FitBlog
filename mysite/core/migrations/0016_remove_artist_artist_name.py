# Generated by Django 5.0.7 on 2024-10-14 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_artist_song_artist_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='artist_name',
        ),
    ]