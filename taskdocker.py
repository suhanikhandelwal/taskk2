#!/usr/bin/python3

print("content-type: text/html")
print()


import subprocess as sp
import cgi

form=cgi.FieldStorage()
#name=input("Enter the name of os: ")

name=form.getvalue("name")
image=form.getvalue("image") 
cmd= "sudo docker run -d -i -t --name {0} {1}".format(name,image)
output= sp.getstatusoutput(cmd)

status=output[0]
out=output[1]


if status==0:
 print("os launched by name {}".format(name))

else:
 print("error : {}".format(out))
