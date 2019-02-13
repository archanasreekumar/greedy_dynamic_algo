#command to run
#python2 filename.py

import math

print 'enter the first number'
a=input()
print 'enter the second number'
b=input()

a1=a#copying the value of a
b1=b#coying the value of b
n=0

count=0
n1=0
while(a1>0):#loop to find length of a
    x=a1%10
    count+=1
    a1=a1/10
n1=count#length of a

count=0
n2=0
while(b1>0):#loop to find length of b
    x=b1%10
    count+=1
    b1=b1/10
n2=count#length of b

if(n1>n2):#taking the largest length as n
    n=n1
else:
    n=n2
num=0
aR=0
bR=0
bR=0
bL=0
x1=0
x2=0
x3=0
#finding with which number we need to divide a to get aR
num=pow(10,((n1+1)/2))
aR=a%num
aL=a-aR
aL=a/num
num=0
#finding with which number we need to divide a to get bR   
num=pow(10,((n2+1)/2))
bR=b%num
bL=b-bR
bL=b/num 
num=0 
x1=aL*bL
x2=aR*bR
x3=(aL+aR)*(bL+bR)   
#finding the product using the formula
num=x1*pow(10,n)+(x3-x1-x2)*pow(10,(n/2))+x2;
print"Product of "+str(a)+" and "+str(b)+" is "+str(num)



