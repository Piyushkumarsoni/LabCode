from django.shortcuts import render
from DB.models import *
from DB.Cprogram import *
#import requests
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django import template
from django.core.exceptions import ObjectDoesNotExist
import random
import codecs
from json import dumps
from .models import Userreg

@csrf_protect


def runcode(request):
    if request.method== "POST":
        lang=request.POST['languages']
        code=request.POST['code']
        input_part=request.POST['input_area']
        y=input_part
        input_part = input_part.replace("\n"," ").split(" ")
        print(code)
        print("\n\n")
        print(lang)
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        if lang=="C":
            y=cprogram(code)
            output=y.decode('UTF-8')
            
            print(output)

        elif lang=="C++":
            Cpp_program(code)
        elif lang=="Java":
            Java_program(code)
        elif lang=="Python":
            python_program(code)
    return render(request,'exam_page.html',{'output':output,'code':code })




def Indexpage(request):
    return render(request,'landingpage.html')


def Studentlogin(request):
    if request.method=="POST":
        try:
            Userdetails=Studentreg.objects.get(email=request.POST['email'],PSWD=request.POST['PSWD'])
            
            request.session['email']=Userdetails.email
            return render(request,'exam_page.html')
        except ObjectDoesNotExist:
            messages.success(request,"Username/ password Invalid..!")
    return render(request,'studentlogin.html')

def login(request):
    
    if request.method=="POST":
        try:
            Userdetails=Userreg.objects.get(EMAIL=request.POST['EMAIL'],PSWD=request.POST['PSWD'])
            print("USername=",Userdetails)
            request.session['EMAIL']=Userdetails.EMAIL
            data_list= Userreg.objects.all()
            print(data_list)
            return render(request,'teacher.html')
        except ObjectDoesNotExist:
            messages.success(request,"Username/ password Invalid..!")
    return render(request,'login.html')

def Userregisteration(request):
    if request.method=='POST':
        if request.POST.get('FNAME') and request.POST.get('LNAME') and request.POST.get('EMAIL') and request.POST.get('MOBILE_NO') and request.POST.get('PSWD'):
            saverecord=Userreg()
            saverecord.FNAME=request.POST.get('FNAME')
            saverecord.LNAME=request.POST.get('LNAME')
            saverecord.EMAIL=request.POST.get('EMAIL')
            saverecord.MOBILE_NO=request.POST.get('MOBILE_NO')
            saverecord.PSWD=request.POST.get('PSWD')
            saverecord.save()
            messages.success(request,"New User Registration Details Saved Successfully..!")
            return render(request,"registration.html")
    else:
            return render(request,"registration.html")

def enrollment(request):
    return render(request,'enrollment.html')

def teacher(request):
    if request.method=='POST':
        Userdetails=Userreg.objects.get(EMAIL=request.POST['EMAIL'])
        print(Userdetails)
    return render(request, 'teacher.html')
def Tprofile(request):
    data_list= Userreg.objects.all()
    print(data_list)
    return render(request,'teacher.html')



def Student_registration(request):
    if request.method=='POST':
        if request.POST.get('email') and request.POST.get('mobile_no'):
            saverecord=Studentreg()
            saverecord.email=request.POST.get('email')
            saverecord.mobile_no=request.POST.get('mobile_no')
            saverecord.F_name=request.POST.get('F_name')
            saverecord.L_name=request.POST.get('L_name')
            saverecord.PSWD=generate()
            saverecord.status_id="not Appeared"
            saverecord.room_id=5
            saverecord.student_id=random.randint(0,100)
            saverecord.save()
            messages.success(request,"New User Registration Details Saved Successfully..!")
            return render(request,"student_registration.html")
    else:
            return render(request,"student_registration.html")

def generate():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVW"
    passlen = 6
    p =  "".join(random.sample(s,passlen ))
    return p

def question_paper(request):
    return render(request,'questions_paper.html')







      
    
    