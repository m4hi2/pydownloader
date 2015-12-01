#!/usr/bin/python3

import subprocess, shlex

print("File with download link lists: ", end="")
filename = input()

try:
	with open(filename) as data:
		for line in data:
			command = "wget -c {}".format(line)
			_command = shlex.split(command)
			subprocess.Popen(_command)
except IOError as ioerr:
	print("File Error: " + str(ioerr))
