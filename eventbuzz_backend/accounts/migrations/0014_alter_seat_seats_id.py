# Generated by Django 5.1 on 2024-09-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seats_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
