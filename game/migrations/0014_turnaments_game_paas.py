# Generated by Django 5.0.2 on 2024-09-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_turnaments_meta_description_turnaments_meta_keywords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnaments',
            name='game_paas',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
