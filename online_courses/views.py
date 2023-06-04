from django.shortcuts import render
from .models import *
from .form import *
from django.contrib.auth import login,logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def all_courses(request):
    allCourses=CourseGeneral.objects.all()
    
    if( request.user.is_authenticated ):
        mycourses=UserCourseSubscribe.objects.filter(user_pk=request.user)
        userInfo=get_object_or_404( AllUserInfo,user_pk=request.user)
    else:
        mycourses={}
        userInfo={}
    return render(request, 'online_courses/index.html', {"courses":allCourses,"mycourses":mycourses,"userInfo":userInfo})

def login_page(request):
    if request.method=='POST':
        form=UserLoginform(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)

            return redirect('all_courses')
        else:
            messages.error(request,'Сіз электронды почтаны немесе құпия сөзді қате енгіздіңіз')
            form=UserLoginform()
    else:
        form=UserLoginform()
    
    return render(request,'online_courses/auth.html',{'form':form})
def logout_page(request):
    logout(request)
    return redirect('all_courses')
def register_page(request):
    if request.method=='POST':
        form=UserRegister(data=request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            AllUserInfo.objects.create(user_pk=user,
                                       first_name=user.first_name,
                                       last_name=user.last_name,
                                       email=user.username)
            col=send_mail(
               'Online Courses' ,
               'Добрый день! \n Вы успешно зарегистрированы в системе Online courses! Начните подготовку к ЕНТ с нами! \n С уважением, \nКоманда Online courses.kz',
                'bikesite@mail.ru',
                [str(user.username)],
                fail_silently=True 
            )
            return redirect('all_courses')
        else:
            messages.error(request,'Электронды почта тіркелген немесе құпия сөздер сәйкес келмейді')
            form=UserRegister()
    else:
        form=UserRegister()

    return render(request,'online_courses/register.html',{'form':form})
# gxo927fd986cdcwq8

def user_profile(request):
    info=AllUserInfo.objects.get(user_pk=request.user)
    if request.method == 'POST':  
        form = UserProfileForm(request.POST, request.FILES)  
        if form.is_valid():  
            AllUserInfo.objects.filter(user_pk=request.user).update(user_icon=form.instance.user_icon )
            return redirect('all_courses')
        else:
            form = UserProfileForm()
    else:
        form = UserProfileForm()
    return render(request,'online_courses/user-cabinet.html',{'user_info':info,'form':form})

def course_details(request,pk):
    course=get_object_or_404(CourseGeneral,pk=pk)
    all_subjects=CourseSubject.objects.filter(course_pk=course)
    if( request.user.is_authenticated ):

        subscribe=UserCourseSubscribe.objects.filter(user_pk=request.user.pk,course_pk=course)
        mycourses=UserCourseSubscribe.objects.filter(user_pk=request.user.pk)
        userInfo=AllUserInfo.objects.get(  user_pk=request.user.pk)

    else:
        subscribe={}
        mycourses={}
        userInfo={}
    return render(request,'online_courses/course-details.html',{'course':course ,'all_subjects':all_subjects ,'mycourses':mycourses,'userInfo':userInfo,'subscribe':subscribe})


def add_to_my_courses(request,pk):
    if( not request.user.is_authenticated ):
        return redirect('login')
    course=get_object_or_404(CourseGeneral,pk=pk)
    UserCourseSubscribe.objects.create(user_pk=request.user,course_pk=course)
    return redirect('course_details',pk=pk)

def delete_from_my_courses(request,pk):
    course=get_object_or_404(CourseGeneral,pk=pk)
    UserCourseSubscribe.objects.filter(user_pk=request.user,course_pk=course).delete()
    return redirect('course_details',pk=pk)

def all_chats(request):
    all_users=AllUserInfo.objects.filter().exclude(user_pk=request.user)
    mycourses=UserCourseSubscribe.objects.filter(user_pk=request.user)
    userInfo=get_object_or_404( AllUserInfo,user_pk=request.user)
    return render(request,'online_courses/all-chats.html',{"mycourses":mycourses,"userInfo":userInfo,'all_users':all_users})

def every_chat(request,pk):
    userInfo=get_object_or_404( AllUserInfo,user_pk=request.user.pk).user_pk
    companion_user=get_object_or_404( AllUserInfo,user_pk=pk).user_pk
    mycourses=UserCourseSubscribe.objects.filter(user_pk=request.user)

    return render(request,'online_courses/chat.html',{"current_user":userInfo,"companion_user":companion_user,'mycourses':mycourses})

# def open_full_course(request,pk):
#     all_themes=CourseSubject.objects.filter(course_pk=pk)
#     course=get_object_or_404(CourseGeneral,pk=pk)
#     first_theme=all_themes[0]
#     return render(request ,'online_courses/course-read.html',{'all_themes':all_themes,'course':course,'first':first_theme})

def open_theme_course(request,pk,thempk):
    all_themes=CourseSubject.objects.filter(course_pk=pk)
    course=get_object_or_404(CourseGeneral,pk=pk)
    first_theme=CourseSubject.objects.get(pk=thempk)
    return render(request ,'online_courses/course-read.html',{'all_themes':all_themes,'course':course,'them':first_theme})
 
def course_lection(request,pk,thempk):
    all_themes=CourseSubject.objects.filter(course_pk=pk)
    course=get_object_or_404(CourseGeneral,pk=pk)
    first_theme=CourseSubject.objects.get(pk=thempk)
    lection=CourseLections.objects.get(subject_pk=thempk)
    return render(request ,'online_courses/course-lection.html',{'all_themes':all_themes,'course':course,'them':first_theme,'lection':lection})
 
def course_video(request,pk,thempk):
    all_themes=CourseSubject.objects.filter(course_pk=pk)
    course=get_object_or_404(CourseGeneral,pk=pk)
    first_theme=CourseSubject.objects.get(pk=thempk)
    video=CourseVideoLections.objects.get(subject_pk=thempk)
    return render(request ,'online_courses/course-video.html',{'all_themes':all_themes,'course':course,'them':first_theme,'video':video})
 


def course_test(request,pk,thempk):
    all_themes=CourseSubject.objects.filter(course_pk=pk)
    course=get_object_or_404(CourseGeneral,pk=pk)
    first_theme=CourseSubject.objects.get(pk=thempk)
    mycourses=UserCourseSubscribe.objects.filter(user_pk=request.user)
    userInfo=get_object_or_404( AllUserInfo,user_pk=request.user)
    alltests=CourseTests.objects.filter(course_pk=thempk)
    if request.method == 'POST':
        wrong=0
        correct=0
        total=0
        current_submission=[]
        for q in alltests:
            current=Submition()
            total+=1
            if q.test_answer ==  request.POST.get(q.test_question):
                correct+=1
                current.correct=True
            else:
                current.correct=False
                wrong+=1
            current.question=q.test_question
            current.test_answer=request.POST.get(q.test_question)
            current_submission.append(current)
        result=UserTestResult.objects.filter(user_pk=request.user,test_pk=first_theme)
        if(  len(result) == 0 ):
            result=UserTestResult.objects.create(user_pk=request.user,test_pk=first_theme,count_of_tests=total,count_correct=correct)
            ussub=UserCourseSubscribe.objects.get(user_pk=request.user,course_pk=course)
            UserCourseSubscribe.objects.filter(user_pk=request.user,course_pk=course).update(grades=ussub.grades+correct*5)
        
        return render(request ,'online_courses/test-result.html',{'current_submission':current_submission ,"mycourses":mycourses,'userInfo':userInfo})

    return render(request ,'online_courses/open-test.html',{'all_themes':all_themes,'course':course,'them':first_theme,'alltests':alltests , "mycourses":mycourses,'userInfo':userInfo})

def all_tests(request):
    userInfo=get_object_or_404( AllUserInfo,user_pk=request.user)

    mycourses=UserCourseSubscribe.objects.filter(user_pk=request.user.pk)
    for course in mycourses:
        subjects=CourseSubject.objects.filter(course_pk=course.course_pk)
        course.subject=subjects
    return render(request ,'online_courses/test.html',{"mycourses":mycourses,'userInfo':userInfo})

def teacher_courses(request):
    teacherCourses=CourseGeneral.objects.filter(author=request.user.pk)
    userInfo=AllUserInfo.objects.get(  user_pk=request.user.pk)
    for courses in teacherCourses:
        subscribers=UserCourseSubscribe.objects.filter(course_pk=courses.pk)
        courses.subscribers=subscribers
    return render(request, 'online_courses/teacher-main.html',{'teacherCourses':teacherCourses,'userInfo':userInfo})


def addcourse(request):
    
    if request.method == 'POST':
        courseform = CourseForm(request.POST)
        subjectform=SubjectForm(request.POST)
        lectionform=LectionForm(request.POST,request.FILES)
        videoform=VideoForm(request.POST,request.FILES)
        coursetests=CourseTestsForm(request.POST)
        if courseform.is_valid() and subjectform.is_valid() and lectionform.is_valid() and videoform.is_valid() and coursetests.is_valid():
            course=courseform.save(commit=False)
            course.author=request.user
            course.save()

            subject=subjectform.save(commit=False)
            subject.course_pk=course
            subject.save()

            lection=lectionform.save(commit=False)
            lection.subject_pk=subject
            lection.save()

            video=videoform.save(commit=False)
            video.subject_pk=subject
            video.save()
            
            test=coursetests.save(commit=False)
            test.course_pk=subject
            test.save()
            return redirect('teacher_courses')
        else:
            messages.error(request,'Енгізген ақпарат қате')
            
    else:
        courseform=CourseForm()
        subjectform=SubjectForm()
        lectionform=LectionForm()
        videoform=VideoForm()
        coursetests=CourseTestsForm()

    
    return render(request, 'online_courses/add-course.html',{'subjectform':subjectform,'lectionform':lectionform,'videoform':videoform,'coursetests':coursetests,'courseform':courseform})



def delete_course(request,pk):
    CourseGeneral.objects.get(pk=pk).delete()
    return redirect('teacher_courses')