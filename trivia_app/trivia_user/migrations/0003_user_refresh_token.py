# Generated by Django 4.0.6 on 2022-07-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_user', '0002_alter_user_options_user_date_joined_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
