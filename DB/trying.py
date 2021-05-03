import subprocess

def cprogram():
    #f=open("D:/SEMESTER/important/labcodes/DB/test.c",'r')
    #f.read()
    var1="gcc"
    var2="test.c"
    var3="-o"
    var4="out"
    subprocess.run([var1,var2,var3,var4])
    subprocess.run("./out")

def Cpp_program(code):
    f=open("D:/SEMESTER/important/labcodes/DB/try.cpp",'w')
    f.write(code)
    var1="g++"
    var2="try.cpp"
    var3="-o"
    var4="out"
    subprocess.run([var1,var2,var3,var4])
    subprocess.run("./out")

def Java_program(code):
    f=open("D:/SEMESTER/important/labcodes/DB/Javacode.java",'w')
    f.write(code)
    var1="javac"
    var2="javacode.java"
    var3="java"
    var4= input("Main class name:-")

    subprocess.run([var1,var2])
    subprocess.run([var3,var4])

def python_program(code):
    f=open("D:/SEMESTER/important/labcodes/DB/testpython.py",'w')
    f.write(code)
    var1="python"
    var2="testpython.py"
    subprocess.run([var1,var2])

if __name__ == "__main__":

    cprogram()