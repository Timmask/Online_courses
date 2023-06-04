# Generated by Django 4.2.1 on 2023-05-30 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online_courses', '0005_alter_coursegeneral_course_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourseSubscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.IntegerField(default=0)),
                ('course_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_courses.coursegeneral')),
                ('user_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]