# Generated by Django 4.2.1 on 2023-05-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_courses', '0002_courseparts_coursesubject_usertestresult_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegeneral',
            name='course_icon',
            field=models.ImageField(default='qwert', upload_to=''),
        ),
    ]
