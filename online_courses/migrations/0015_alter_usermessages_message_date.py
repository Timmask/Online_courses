# Generated by Django 4.2.1 on 2023-06-06 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_courses', '0014_alter_usermessages_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessages',
            name='message_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
