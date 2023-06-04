# Generated by Django 4.2.1 on 2023-06-04 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_courses', '0012_alter_coursegeneral_course_icon_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alluserinfo',
            options={'verbose_name': 'Қолданушы туралы толық ақпарат', 'verbose_name_plural': 'Қолданушылар туралы толық ақпарат'},
        ),
        migrations.AlterModelOptions(
            name='coursegeneral',
            options={'verbose_name': 'Курс туралы толық ақпарат', 'verbose_name_plural': 'Курстар туралы толық ақпарат'},
        ),
        migrations.AlterModelOptions(
            name='courselections',
            options={'verbose_name': 'Лекция', 'verbose_name_plural': 'Лекциялар'},
        ),
        migrations.AlterModelOptions(
            name='coursesubject',
            options={'verbose_name': 'Тақырып', 'verbose_name_plural': 'Тақыраптар'},
        ),
        migrations.AlterModelOptions(
            name='coursetests',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесттер'},
        ),
        migrations.AlterModelOptions(
            name='coursevideolections',
            options={'verbose_name': 'Видео лекция', 'verbose_name_plural': 'видео лекциялар'},
        ),
        migrations.AlterModelOptions(
            name='usercoursesubscribe',
            options={'verbose_name': 'Курсқа жазылым', 'verbose_name_plural': 'Курстарға жазылым'},
        ),
        migrations.AlterModelOptions(
            name='usermessages',
            options={'verbose_name': 'Хабарлама', 'verbose_name_plural': 'Хабарламалар'},
        ),
        migrations.AlterModelOptions(
            name='usertestresult',
            options={'verbose_name': 'Тест нәтижесі', 'verbose_name_plural': 'Тест нәтижелері'},
        ),
    ]