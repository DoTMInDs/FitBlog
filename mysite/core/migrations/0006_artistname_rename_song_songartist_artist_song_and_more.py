# Generated by Django 5.0.7 on 2024-10-13 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_artistuser_songartist_artist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_artist', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='songartist',
            old_name='song',
            new_name='artist_song',
        ),
        migrations.RemoveField(
            model_name='songartist',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='songartist',
            name='artist_user',
        ),
        migrations.RemoveField(
            model_name='songartist',
            name='genre',
        ),
        migrations.AddField(
            model_name='songartist',
            name='song_genre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_genre', models.CharField(max_length=200, null=True)),
                ('artist_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('artist_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.artistname')),
            ],
            options={
                'ordering': ['-posted_on'],
            },
        ),
        migrations.AddField(
            model_name='songartist',
            name='artist_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.artistname'),
        ),
    ]
