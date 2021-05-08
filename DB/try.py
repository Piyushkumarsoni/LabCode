from subprocess import Popen, CREATE_NEW_CONSOLE,PIPE,run
import os
 
v1="gcc"
v2="cp.c"
v3="-o"
v4="./out"
p=Popen([v1,v2,v3,v4], stdout=PIPE,stdin=PIPE)
x=Popen('out.exe')
x_out=x.communicate(b"5")
#Popen('out.exe', )
