# Generated by Django 4.2.1 on 2023-06-06 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_courses', '0013_alter_alluserinfo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessages',
            name='message_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
