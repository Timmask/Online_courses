from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from .models import *
class UserRegister(UserCreationForm):
    first_name=forms.CharField(label='First_name',widget=forms.TextInput(attrs={'placeholder':'Аты'}))
    last_name=forms.CharField(label='Last name',widget=forms.TextInput(attrs={'placeholder':'Фамилия'}))
    username=forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'placeholder':'Эл. почта'}))
    password1=forms.CharField(label='password 1',widget=forms.PasswordInput(attrs={'placeholder':'Құпиясөз'}))
    password2=forms.CharField(label='password 1',widget=forms.PasswordInput(attrs={'placeholder':'Құпиясөзді қайта теріңіз'}))

    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']


        
class UserLoginform(AuthenticationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':"Эл. почта" }),error_messages={'required': 'Эл. почта немесе Құпиясөз қате '})

    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':"Құпиясөз"}),error_messages={'required': 'Эл. почта немесе Құпиясөз қате'})

class UserProfileForm(forms.ModelForm):
    user_icon=forms.ImageField(label='img',widget=forms.FileInput(attrs={'style':"display: none;"}))
    class Meta:  
        model = AllUserInfo  
        fields = ['user_icon']  
# add-card
class CourseForm(forms.ModelForm):
    title=forms.CharField(label='Курс атауы',widget=forms.TextInput(attrs={'style':'height: 40px;padding:20px'}))
    info=forms.CharField( label='Курс туралы ақпарат',widget=forms.TextInput(attrs={'style':'height: 200px;width: 100%;'}))
    # course_icon=forms.ImageField(label='Курс суреті',widget=forms.FileInput())
    class Meta:
        model = CourseGeneral
        fields = ['title','info','course_icon']
        

class SubjectForm(forms.ModelForm):
    subject_name=forms.CharField(label='Тақырап аты',widget=forms.TextInput(attrs={'placeholder':"Курсы аты..." }))
    class Meta:  
        model = CourseSubject  
        fields = ['subject_name']  

class LectionForm(forms.ModelForm):
    lection_text1=forms.CharField(label='Лекция 1',widget=forms.TextInput())
    lection_text2=forms.CharField(label='Лекция 2',widget=forms.TextInput())
    # lection_image=forms.ImageField(label='Лекция мысалы',widget=forms.FileInput() )
    class Meta:  
        model = CourseLections  
        fields = ['lection_text1','lection_text2','lection_image']  

class VideoForm(forms.ModelForm):
    # lection_video=forms. (label='Видео лекция')
    class Meta:
        model = CourseVideoLections
        fields=['lection_video']

class CourseTestsForm(forms.ModelForm):
    test_question=forms.CharField(label='Тест сұрағы',widget=forms.TextInput())
    test_option1=forms.CharField(label='1 нұсқа')
    test_option2=forms.CharField(label='2 нұсқа')
    test_option3=forms.CharField(label='3 нұсқа')
    test_option4=forms.CharField(label='4 нұсқа')
    test_answer=forms.CharField(label='дұрыс нұсқа')
    class Meta:
        model = CourseTests
        fields=['test_question','test_option1','test_option2','test_option3','test_option4','test_answer']