from os import symlink,mkdir
import os
import subprocess
from subprocess import PIPE,run
import tempfile
import shutil
import uuid
base="D:\\SEMESTER\\important\\labcodes\\TempFile1\\"
def cprogram(code,input_=[]):
    f=open("new.c",'w')
    mydir=base+str(uuid.uuid1())
    mkdir(mydir)
    var2=mydir+"\\cpp.c"
    f=open(var2,'w')
    f.write(code)
    f.close()
    var1="gcc"
    #var2="new.c"
    var3="-o"
    var4=mydir+"\\out.exe"
    subprocess.run([var1,var2,var3,var4])
    #x=subprocess.run(mydir+"\\out",stdout=PIPE)
    try:

        arg=""
        for i in input_:
            arg+=i
        print(mydir+"\\out.exe")
        x=run(mydir+"\\out.exe", stdout=PIPE,
            input=arg, encoding='ascii')
        shutil.rmtree(mydir)
        return x.stdout
    except:
        return "Error in code"


def Cpp_program(code,input_=[]):
    mydir=base+str(uuid.uuid1())
    mkdir(mydir)
    var2=mydir+"\\cpp.cpp"
    f=open(var2,"w")
    # f=open(var2,'w')
    f.write(code)
    f.close()
    var1="g++"
    #var2="try.cpp"
    var3="-o"
    var4=mydir+"\\out.exe"
    subprocess.run([var1,var2,var3,var4])
    #x=subprocess.run(mydir+"\\out",stdout=PIPE)
    arg=""
    for i in input_:
        arg+=i
    x=run(mydir+"\\out.exe", stdout=PIPE,
        input=arg, encoding='ascii')
    shutil.rmtree(mydir)
    return x.stdout
#
def Java_program(code,input_=[]):
    # mydir=tempfile.mkdtemp(prefix="tempdir")
    mydir=base+str(uuid.uuid1())
    mkdir(mydir)
    var2=mydir+"\\Javacode.java"
    #os.chdir(mydir)
    f=open(var2,"w")
    #(f,var2)=tempfile.mkstemp(prefix="Javacode",suffix=".java")
    print(code)
    f=open(var2,'w')
    f.write(code)
    f.close()
    var1="javac"
    var2="Javacode.java"
    var3="java"
    var4= "\"Javacode\""
    y=subprocess.run([var1,var2],stdout=PIPE)
    #subprocess.run([var3,var4],stdout=PIPE,stderr=PIPE)
    # if y.returncode ==0:
    #     y=""
    # else:
    #     y=y.stderr.decode("utf-8")
    y=""
    arg=""
    for i in input_:
        arg+=i
    try:
        x=run([var3,var4], stdout=PIPE,
            input=arg, encoding='ascii')
        x=x.stdout
    except:
        x="Error in the code"
    #shutil.rmtree(mydir)
    return x