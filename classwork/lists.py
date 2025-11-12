Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[]
l=list()
l=[1,2,3,4,5,6]
l=list([1,2,3,4,5])
>>> l'
SyntaxError: incomplete input
>>> l
[1, 2, 3, 4, 5]
>>> l=[[1,2],[3,4],[5,6]]
>>> l=[1,1,1,1,1,1,2]
>>> l
[1, 1, 1, 1, 1, 1, 2]
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2]*5
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
>>> l
[1, 1, 1, 1, 1, 1, 2]
>>> 2 in l
True
>>> 6 in l
False
>>> l=['ajay','krishna','shekar','santhosh','harsha','varun','shiva']
l
['ajay', 'krishna', 'shekar', 'santhosh', 'harsha', 'varun', 'shiva']
l[2]
'shekar'
l[-3]
'harsha'
l[-2]
'varun'
l[-1]
'shiva'
l[1]
'krishna'
l[0]
'ajay'
l[1:3]
['krishna', 'shekar']
l[-1:-4:-1]
['shiva', 'varun', 'harsha']
l[::2]
['ajay', 'shekar', 'harsha', 'shiva']
l[1::2]
['krishna', 'santhosh', 'varun']
l[::-1]
['shiva', 'varun', 'harsha', 'santhosh', 'shekar', 'krishna', 'ajay']
l=[[1,2],[3,4],[5,6]]
l[2]
[5, 6]
l[1]
[3, 4]
l[0]
[1, 2]
l[0][0]
1
l[2][0]
5
l[1][1]
4
l=[10,20,30,40,50]
id(l)
3167687961344
l[1]
20
l[1]=20.3
l
[10, 20.3, 30, 40, 50]
id(l)
3167687961344
l[2]=30+4j
l
[10, 20.3, (30+4j), 40, 50]
l[3]='string'
l
[10, 20.3, (30+4j), 'string', 50]
l
[10, 20.3, (30+4j), 'string', 50]
l.append([1,2,3])
l
[10, 20.3, (30+4j), 'string', 50, [1, 2, 3]]
l.append((10,202,30))
l
[10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30)]
l
[10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30)]
l.append(70)
l.append(80)
l
[10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30), 70, 80]
l.extend([100,90,20,10])
l
[10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.insert(0,10)
l
[10, 10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.insert(5,{1:2,2:4,3:6,4:8})
l
[10, 10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.insert(8,{1,2,3,4})
l
[10, 10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], {1, 2, 3, 4}, (10, 202, 30), 70, 80, 100, 90, 20, 10]
l
[10, 10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], {1, 2, 3, 4}, (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.remove(10)
l
[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], {1, 2, 3, 4}, (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.remove((10, 202, 30))
l
[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], {1, 2, 3, 4}, 70, 80, 100, 90, 20, 10]
l.remove({1, 2, 3, 4})
l
[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 100, 90, 20, 10]
l.remove(100)
l
[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]
l.remove(100)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    l.remove(100)
ValueError: list.remove(x): x not in list
l
[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]
l.pop(2)
(30+4j)
l
[10, 20.3, 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]
l.pop(1)
20.3
l
[10, 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]
l.pop(1)
'string'
l
[10, {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]
l.pop(1)
{1: 2, 2: 4, 3: 6, 4: 8}
l
[10, 50, [1, 2, 3], 70, 80, 90, 20, 10]
l.pop()
10
l
[10, 50, [1, 2, 3], 70, 80, 90, 20]
l.pop()
20
l.pop()
90
l.pop()
80
l
[10, 50, [1, 2, 3], 70]
del l[2]
l
[10, 50, 70]
l.clear()
l
[]
l=[1,2,3,4]
del l
l
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    l
NameError: name 'l' is not defined
l=[1,2,3,4]
l.clear()
l
[]
l=[10,20,30,40,50,60,70,80]
l.index(30)
2
l.index(80)
7
l.index(100)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    l.index(100)
ValueError: 100 is not in list
l
[10, 20, 30, 40, 50, 60, 70, 80]
l.append(10)
l
[10, 20, 30, 40, 50, 60, 70, 80, 10]
l.index(10)
0
l.count(10)
2
l.sort()
l
[10, 10, 20, 30, 40, 50, 60, 70, 80]
l=[8,2,3,4,1,8,3,4]
sorted(l)
[1, 2, 3, 3, 4, 4, 8, 8]
l
[8, 2, 3, 4, 1, 8, 3, 4]
l.sort()
l
[1, 2, 3, 3, 4, 4, 8, 8]
l.sort(reverse=True)
l
[8, 8, 4, 4, 3, 3, 2, 1]
l.reverse()
l
[1, 2, 3, 3, 4, 4, 8, 8]
a=[1,2,3,4,5]
a
[1, 2, 3, 4, 5]
b=a
b
[1, 2, 3, 4, 5]
b.append(6)
b
[1, 2, 3, 4, 5, 6]
a
[1, 2, 3, 4, 5, 6]
c=copy(a)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    c=copy(a)
NameError: name 'copy' is not defined
c=a.copy()
c
[1, 2, 3, 4, 5, 6]
c.append(9)
c
[1, 2, 3, 4, 5, 6, 9]
a
[1, 2, 3, 4, 5, 6]