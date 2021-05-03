import subprocess
from subprocess import PIPE
def cprogram(code):
    f=open("new.c",'w')
    f.write(code)
    f.close()
    var1="gcc"
    var2="new.c"
    var3="-o"
    var4="out"
    subprocess.run([var1,var2,var3,var4])
    x=subprocess.run("./out",stdout=PIPE)
    return x.stdout

def Cpp_program(code):
    f=open("try.cpp",'w')
    f.write(code)
    f.close()
    var1="g++"
    var2="try.cpp"
    var3="-o"
    var4="out"
    subprocess.run([var1,var2,var3,var4])
    x=subprocess.run("./out",stdout=PIPE)
    return x.stdout


def Java_program(code):
    f=open("Javacode.java",'w')
    f.write(code)
    f.close()
    var1="javac"
    var2="javacode.java"
    var3="java"
    var4= input("Main class name:-")

    subprocess.run([var1,var2])
    subprocess.run([var3,var4])

def python_program(code):
    f=open("testpython.py",'w')
    f.write(code)
    f.close()
    var1="python"
    var2="testpython.py"
    x=subprocess.run([var1,var2],stdout=PIPE)
    return x.stdout


