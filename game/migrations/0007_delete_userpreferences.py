# Generated by Django 5.0.2 on 2024-09-12 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_userpreferences'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPreferences',
        ),
    ]
