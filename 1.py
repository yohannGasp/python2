#!/usr/bin/python3

import sqlite3

con = sqlite3.connect('/home/john/2/db.sqlite3')
c = con.cursor()
c.execute('select * from name')

print('===================================')
for r in c:
	print(r)
print('----------------------------------')
c.close()


f1 = open('/home/john/2/1.py','r')
for l in f1.readlines():
	print(l)
f1.close()


list = ["1","2"]

x1 = 0
while x1 < 2:
	print(list[x1])
	x1 += 1

l1 = ['1','2','3','4','4','1']
l2 = []
l3 = []
for x in l1:
	if x not in l2:
		l2.append(x)
	else:
		l3.append(x)

print(l3)







