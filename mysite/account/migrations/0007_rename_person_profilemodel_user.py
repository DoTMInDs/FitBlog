# Generated by Django 5.0.7 on 2024-09-30 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_profilemodel_user_profilemodel_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='person',
            new_name='user',
        ),
    ]
