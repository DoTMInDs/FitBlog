# Generated by Django 5.0.7 on 2024-10-12 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_songartist_artistuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songartist',
            old_name='image',
            new_name='artist_profile',
        ),
    ]
