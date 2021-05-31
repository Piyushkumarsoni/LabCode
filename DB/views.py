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
    if request.method== "POST":
        lang=request.POST['languages']
        code=request.POST['code']
        raw_code={"code":code}
        input_part=request.POST['input_area']
        y=input_part
        input_part = list(map(str.strip,input_part.split("\n")))
        print(input_part)
        if len(input_part)==1:
            if input_part[0].strip()=="":
                paraMeter=False
            else:
                paraMeter='{"'+input_part[0]+'"}'
        else:
            paraMeter=str(input_part)
            paraMeter="{"+paraMeter[1:]
            paraMeter=paraMeter[:-1]+"}"
            paraMeter=re.sub(r"(\"|\')",'"',paraMeter)
        print(paraMeter)
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        # print(code)
        # print("\n\n")
        # print(lang) 

        if lang=="C":
            
            # patt=re.compile(r"scanf\(\"%d\",\s*&([a-zA-Z_][a-zA-Z-_]*)\);")
            # matches=patt.finditer(code)
            # for c in matches:
            #     temp = str.maketrans(c.group(0), )
            #     code = code.translate(temp)
            if paraMeter!=False:
                def Convert_Input(match_obj):
                    if match_obj.group(1) is not None:
                        return match_obj.group(1)+"=atoi(GetInput());"
                    return match_obj
                def Convert_InputV2(match_obj):
                    if match_obj.group(1) is not None:
                        return match_obj.group(1)+"=GetInput();"
                    return match_obj
                def Add_Input_and_Function(match_obj):
                    
                    mytext="""

    int position=0;
    char *myarray["""+str(len(input_part))+"""] = """+paraMeter+""";
    char* GetInput()  
    {  
        position++;  
    
        return myarray[position-1];
    }
    """
                    if match_obj.group(1) is not None:
                        return mytext+match_obj.group(1)
                    return match_obj 
                code=re.sub(r"scanf\(\"%d\",\s*&([a-zA-Z_][a-zA-Z-_]*)\);",Convert_Input,code)
                code=re.sub(r"scanf\(\"%s\",\s*&([a-zA-Z_][a-zA-Z-_]*)\);",Convert_InputV2,code)
                code=re.sub(r"(int main\(\)|void main\(\))",Add_Input_and_Function,code)
            # code='#include <stdlib.h>\n'+code
            # print(code)
            output=cprogram(code)
            try:
                output=output.decode('UTF-8')
            except:
                output="error"
            return render(request,'exam_page.html',{'output':output,'code':raw_code["code"],'input':y})

            #print(output)


        elif lang=="C++":
            y=Cpp_program(code)
            y=y.decode('UTF-8')
            content1={
                'output': y
            }
            dataJSON=dumps(content1)
            print(y)
            return render(request,'exam_page.html',{'output':y,'code':code})
            

        elif lang=="Java":
            y=Java_program(code)
            y=y.decode('UTF-8')
            content2={
                'output': y
            }
            dataJSON=dumps(content2)
            print(y)
            return render(request,'exam_page.html',content2,{'code':code})


        elif lang=="Python":
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
            print(output)   
        
    return render(request,'exam_page.html',{'output':output,'input':y,'code':code})




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





      
    
    