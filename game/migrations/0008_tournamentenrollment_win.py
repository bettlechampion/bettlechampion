# Generated by Django 5.0.2 on 2024-09-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_delete_userpreferences'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentenrollment',
            name='win',
            field=models.CharField(choices=[('win', 'Win'), ('loss', 'Loss')], default='loss', max_length=4),
        ),
    ]
