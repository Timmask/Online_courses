from django.conf import settings
from django.db import models
from django.utils import timezone

class Submition:
    correct=False
    question=''
    test_answer=''

class AllUserInfo(models.Model):
    user_pk = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    city=models.CharField(max_length=20,default='None')
    email=models.EmailField()
    phone=models.CharField(max_length=20,default='None')
    user_icon=models.ImageField(upload_to='icons/')
    user_type=models.CharField(max_length=30, default='student')
    def isUserTeacher(self):
        if(self.user_type == 'student'):
            return False
        else:
            return True
    def __str__(self):
        return self.first_name+ ' '+ self.last_name
    class Meta:
        verbose_name = "Қолданушы туралы толық ақпарат"
        verbose_name_plural = "Қолданушылар туралы толық ақпарат"

class CourseGeneral(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    info = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    course_icon = models.ImageField(upload_to='media/', blank=True ,default='qwert',null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Курс туралы толық ақпарат"
        verbose_name_plural = "Курстар туралы толық ақпарат"
class CourseParts(models.Model):
    course_pk=models.ForeignKey(CourseGeneral,on_delete=models.CASCADE)
    part_name=models.CharField(max_length=50)

class CourseSubject(models.Model):
    course_pk=models.ForeignKey(CourseGeneral,on_delete=models.CASCADE)
    subject_name=models.CharField(max_length=50)
    def __str__(self)  :
        return self.subject_name
    class Meta:
        verbose_name = "Тақырып"
        verbose_name_plural = "Тақыраптар"
class CourseLections(models.Model):
    subject_pk=models.ForeignKey(CourseSubject,on_delete=models.CASCADE)
    lection_title=models.CharField(max_length=50)
    lection_text1=models.TextField(default='')
    lection_text2=models.TextField(default='')
    lection_image=models.ImageField(upload_to='media/', blank=True ,default='qwert',null=True)
    def __str__(self) :
        return self.lection_title
    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекциялар"
class CourseVideoLections(models.Model):
    subject_pk=models.ForeignKey(CourseSubject,on_delete=models.CASCADE)
    lection_video=models.FileField(upload_to='videos/',null=True,blank=True)
    lection_title=models.CharField(max_length=50)

    def __str__(self):
        return self.lection_title
    class Meta:
        verbose_name = "Видео лекция"
        verbose_name_plural = "видео лекциялар"
class CourseTests(models.Model):
    course_pk=models.ForeignKey(CourseSubject,on_delete=models.CASCADE)
    test_question=models.TextField()
    test_option1=models.CharField(max_length=30)
    test_option2=models.CharField(max_length=30)
    test_option3=models.CharField(max_length=30)
    test_option4=models.CharField(max_length=30)
    test_answer=models.CharField(max_length=30)
    def __str__(self) :
        return self.test_question
    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесттер"
class UserMessages(models.Model):
    user_sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE , related_name='user_sender')
    user_reciver=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_reciver')
    message_text=models.TextField()
    message_date=models.DateTimeField(default=timezone.now)

    def isCurrerntUserSender(self,curUser):
        if(self.user_sender.pk == curUser.pk):
            return True
        else:
            return False
    class Meta:
        verbose_name = "Хабарлама"
        verbose_name_plural = "Хабарламалар"
class UserTestResult(models.Model):
    user_pk=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    test_pk=models.ForeignKey(CourseSubject,on_delete=models.CASCADE)
    count_of_tests=models.IntegerField()
    count_correct=models.IntegerField()

    def getPercent(self):
        return self.count_correct / self.count_of_tests
    def __str__(self) :
        return self.user_pk + ' '+self.test_pk
    class Meta:
        verbose_name = "Тест нәтижесі"
        verbose_name_plural = "Тест нәтижелері"
class UserCourseSubscribe(models.Model):
    user_pk=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course_pk=models.ForeignKey(CourseGeneral,on_delete=models.CASCADE)
    grades=models.IntegerField(default=0)
    def __str__(self) :
        return self.user_pk+' '+ self.course_pk
    class Meta:
        verbose_name = "Курсқа жазылым"
        verbose_name_plural = "Курстарға жазылым"

