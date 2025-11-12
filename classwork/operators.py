'''
Python Operators

-------------
'''
#1. Arithmatic operators
a=20
b=10
print("a+b:",a+b) #a+b: 30
print("a-b:",a-b)  #a-b: 10
print("a*b:",a*b)  #a*b: 200
print("a/b:",a/b)   #a/b: 2.0
print("a//b:",a//b)
print("a**b:",a**b)

#2 comparsion operators
c=30
d=40
print('c<d:',c<d)  #c<d: True
print('c>d:',c>d)  #c>d: False
print('c>=d:',c>=d) #c>=d: False
print('c<=d:',c<=d)  #c<=d: True
print('c==d:',c==d)  #c==d: False
print('c!=d:',c!=d)  #c!=d: True

#3. Assignment Operators
'''
var = var op val
var op=val
'''
e=100
e+=100
print('e=100:',e)  #e=100: 200
e-=100
print('e-=100:',e) #e-=100: 100
e*=100
print('e*=100:',e) #e*=100: 10000
e//=100
print('e//=100:',e) #e//=100: 100
e**=10
print('e**=10:',e)  #e**=10: 100000000000000000000
e%=3
print('e%=10:',e)   #e%=10: 1
e/=5
print('e/=5:',e)   #e/=5: 0.2

#4. Logical Operators
'''
F and F = F
F and T = F
T and F = F
T and T = T

T or F or T or ..... = T
F or F or T or ..... = T
F or F or F or ..... = F
T or T or T or ..... = T

F or F = F
F or T = T
T or F = T
T or T = T
'''
x=100
y=50
print("x%20==0 and y%20==0:",x%20==0 and y%20==0) #x%20==0 and y%20==0: False
print("x%20==0 or  y%20==0:",x%20==0 and y%20==0) #x%20==0 or  y%20==0: False
print("not x%20==0:",not x%20==0)                 #not x%20==0: False
print("not y%20==0:",not y%20==0)                 #not y%20==0: True
      
