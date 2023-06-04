from django.contrib import admin
from .models import *

admin.site.register(CourseGeneral)
admin.site.register(AllUserInfo)
admin.site.register(CourseParts)
admin.site.register(CourseSubject)

admin.site.register(CourseLections)
admin.site.register(CourseVideoLections)

admin.site.register(CourseTests)
admin.site.register(UserMessages)
admin.site.register(UserTestResult)
admin.site.register(UserCourseSubscribe)
# Register your models here.
