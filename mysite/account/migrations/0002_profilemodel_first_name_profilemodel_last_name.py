# Generated by Django 5.0.7 on 2024-09-30 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(null=True),
        ),
    ]