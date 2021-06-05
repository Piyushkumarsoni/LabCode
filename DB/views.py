from django.db.models.fields import EmailField
from django.shortcuts import render
from DB.models import *
from DB.Cprogram import *
#import requests
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django import template
from django.core.exceptions import ObjectDoesNotExist
import random
import sys
import codecs
from json import dumps
from .models import Userreg
from django.contrib.auth.models import User
import re


@csrf_protect

def runcode(request):
    f=open('D:\\SEMESTER\\important\\labcodes\\DB\\question.txt','r')
    ques=f.read()
    f.close()
    if request.method== "POST":
        lang=request.POST['languages']
        code=request.POST['code']
        raw_code={"code":code}
        input_part=request.POST['input_area']
        y=input_part
        def doadd(s):
            s=s.strip()
            return s+"\n"
        input_part = list(map(doadd,input_part.split("\n")))
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        if lang=="C":
            
            output=cprogram(code,input_=input_part)
        elif lang=="C++":
            output=Cpp_program(code,input_=input_part)
        elif lang=="Java":
            output=Java_program(code,input_=input_part)
        elif lang=="Python":
            #output=python_program(code=code,input_=input_part)
            try:
                orig_stdout = sys.stdout
                sys.stdout = open('file.txt', 'w')
                exec(code)
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = open('file.txt', 'r').read()
            except Exception as e:
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = e
        try:
            if output!="Error in code":
                output=output.decode('UTF-8')
            else:
                output="Error in the code"
        except:
            pass
    return render(request,'exam_page.html',{'output':output,'code':raw_code["code"],"input":y,'Question': ques})



def Indexpage(request):
    return render(request,'landingpage.html')


def Studentlogin(request):
    f=open('D:\\SEMESTER\\important\\labcodes\\DB\\question.txt','r')
    ques=f.read()
    f.close()
    if request.method=="POST":
        try:
            Userdetails=Studentreg.objects.get(email=request.POST['email'],PSWD=request.POST['PSWD'])
            
            request.session['email']=Userdetails.email
            return render(request,'exam_page.html',{'Question': ques})
        except ObjectDoesNotExist:
            messages.success(request,"Username/ password Invalid..!")
    return render(request,'studentlogin.html')

def login(request):
    if request.method=="POST":
        try:
            Userdetails=Userreg.objects.get(EMAIL=request.POST['EMAIL'],PSWD=request.POST['PSWD'])
            print("Username=",Userdetails)
            request.session['EMAIL']=Userdetails.EMAIL
            return render(request,'teacher.html',{'data':Userdetails})
        except ObjectDoesNotExist:
            messages.success(request,"Username/ password Invalid..!")
    return render(request,"login.html",)

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
    Userdetails=Userreg.objects.all()
    print("Username=",Userdetails)
    
    return render(request,'teacher.html',{'data':Userdetails})
    



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
    if request.method== "POST":
        question=request.POST['question']
        f=open("file.txt",'w')
        f.write(question)
        f.close()
        print(question)
    return render(request,'questions_paper.html')

def paper(request):
    if request.method=="POST":
         if request.POST.get('papercode') and request.POST.get('question'):
            saverecord=paper_code()
            saverecord.papercode=request.POST.get('papercode')
            saverecord.question=request.POST.get('question')
            saverecord.save()
            return render(request,"question_paper.html")





      
    
    