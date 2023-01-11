
a=str(input('enter your name:'))
print(a,type(a))
print('my name is',a)
print('my name is '+a)
print('my name is',a,sep='-')
print('my name is',int(a))
print('my name is',float(a))
print('my name is'+' '+str(a))
print('my name is %s'%a)
name=input('enter the name:')
age=int(input('enter the age:'))
per=float(input('enter the percentage:'))
print('my name is',name,'age is',age, \
'and percentage is',per)
print("Your Name is {} and age is {}.\
graduation percentage is {}".format(name,age,per))  
print(f'my name is {name} age is {age} percentage is {per}')
a,b=[eval(x) for x in input('enter two numbers:').split()]#3 2.0
print(a+b)#5.0
a=[int(x) for x in input().split(',')]
print(sum(a)) 
import math
a=[float(o) for o in input().split()]
print(math.prod(a))
a=[8976]
print(len('pooja'))