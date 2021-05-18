from subprocess import Popen, CREATE_NEW_CONSOLE,PIPE,run,check_output
import os

data, temp = os.pipe()
os.write(temp, bytes("5 10\n", "utf-8"))
os.close(temp)
  
var1="gcc"
var2="cp.c"
var3="-o"
var4="./out"
#p=Popen([var1,var2,var3,var4],stdout=PIPE,stdin=PIPE)

s = Popen([var1,var2,var3,var4], stdin = data, shell = True)
run('out.exe')