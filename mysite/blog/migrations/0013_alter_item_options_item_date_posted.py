# Generated by Django 5.1.5 on 2025-02-15 09:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_item_item_status_alter_item_item_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-date_posted',)},
        ),
        migrations.AddField(
            model_name='item',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
