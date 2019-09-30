#!/usr/bin/env python3
from fileinput import input as readstdin
from sys import stdout

gs = {} # Global Store

def opExtractor():
	for line in readstdin():
		tc = 0 # Tab Count
		r = ""
		for i in list(line):
			if i in "	\n":
				tc += 1
				if len(r) > 0 and tc is 3:
					yield r
				r = ""
			else:
				r += i

def instructionExtractor():
	for i in opExtractor():
		yield i.split()[0]

for i in instructionExtractor():
	try:
		gs[i] += 1
	except:
		gs[i] = 1
r = []
for k,v in gs.items():
	ic = 0
	for i in r:
		if i[1] < v:
			r.insert(ic, (k,v))
			break
		ic += 1
	else:
		r.append((k,v))

for k,v in r:
	stdout.write(k + "," + str(v) + "\n")
