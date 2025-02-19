# Generated by Django 5.0.7 on 2024-10-13 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_artistname_rename_song_songartist_artist_song_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artist_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.artistname', unique=True),
        ),
        migrations.AlterField(
            model_name='artistname',
            name='name_of_artist',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
