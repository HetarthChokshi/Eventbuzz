# Generated by Django 5.1 on 2024-09-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_event_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='like_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sport',
            name='votes',
            field=models.CharField(default='0k', max_length=20),
        ),
    ]
