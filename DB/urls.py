"""DB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
admin.site.site_header="LabCode"
admin.site.site_title="Welcome to Admin Dashboard"
admin.site.index_title="welcome to LabCode Admin Panel!"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Indexpage),
    path('registration', views.Userregisteration, name='registration'),
    path('login', views.login, name='login'),
    path('enrollment', views.enrollment, name='enrollment'),
    path('teacher',views.teacher, name='teacher'),
    path('Student_registration', views.Student_registration, name='Student_registration'),
    path('Studentlogin',views.Studentlogin,name='studentlogin'),
    path('logout',views.login,name='logout'),
    path('question_paper',views.question_paper, name='question_paper'),
    path('runcode',views.runcode, name='runcode')
    
]
