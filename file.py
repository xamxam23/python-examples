import re
lines = tuple(open("data.txt", 'r'))
c = 0
o = 0
list = []
for line in lines:
	line=line.replace(",","").replace(chr(226)+chr(136)+chr(146), "-")
	#for l in line:
	#	print l+" "+str(ord(l))
	c+=1
	#print line
	n = re.search('"-?(0|([1-9][0-9]*))(.[0-9]{1,2})?"', line, re.IGNORECASE)
	if n is not None:
		s = n.group(0)
		s = float(s[1:len(s)-1])
		list+=[s]
		print s
		o+=1
print c-1
print o

list = list[1:-1]
print sum(list)