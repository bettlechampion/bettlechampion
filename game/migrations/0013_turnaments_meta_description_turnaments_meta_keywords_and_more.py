# Generated by Django 5.0.2 on 2024-09-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_cta'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnaments',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turnaments',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='turnaments',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
