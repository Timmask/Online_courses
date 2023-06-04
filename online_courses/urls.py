from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.all_courses, name='all_courses'),
    path('authentication/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('authorization/', views.register_page, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('course/<int:pk>', views.course_details, name='course_details'),
    path('addmycourse/<int:pk>', views.add_to_my_courses, name='addmycourses'),
    path('delmycourse/<int:pk>', views.delete_from_my_courses, name='deletemycourses'),
    path('chats/<int:pk>/', views.every_chat, name='chat'),
    path('allchats/', views.all_chats, name='all_chats'),
    path('course/<int:pk>/theme/<int:thempk>', views.open_theme_course, name='full_course'),
    path('course/<int:pk>/theme/<int:thempk>/lection', views.course_lection, name='course_lection'),
    path('course/<int:pk>/theme/<int:thempk>/videolections', views.course_video, name='course_video'),
    path('course/<int:pk>/theme/<int:thempk>/test', views.course_test, name='course_test'),
    path('alltests/',views.all_tests,name='all_tests'),
    path('teacherscourses/',views.teacher_courses,name='teacher_courses'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('deletecourse/<int:pk>/',views.delete_course,name='deletecourse'),
    


    
]