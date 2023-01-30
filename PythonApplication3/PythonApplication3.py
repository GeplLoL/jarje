#from random import *
#lis=[]
#1
#for i in range(5):
#    n = input("nimi ")
#    lis.append(n) #lisa lisa
#lis.sort() #lisa sort
#print(lis) 
#print("Last name ",n) #lõpp list
#2
#student = ["Juhan","Kati","Maarja","Mario","Mati"]
#print(student)
#x = int(input("valige nime number "))
#y = str(input("nimi, mille vastu soovite muuta "))
#student.pop(x-1) #lisa pop
#student.insert(x-1,y) #lisa insert
#print(student)
#3
#opilased = ["Juhan","Kati","Mario","Mario","Mati"]
#x = []
#for y in opilased:
#    if y not in x:
#        x.append(y)
#print(x)
#4
#vanus = randint(1,100)
#vanus2 = randint(1,100)
#vanus3 = randint(1,100)
#x=[vanus, vanus2, vanus3]
#print(max(x))
#print(min(x))
#print((vanus+vanus2+vanus3)/3)
#print(vanus+vanus2+vanus3)
#5
#x=[1,2,3]
#y="*"
#for i in range(0,x[0]):
#    print(y, end="")
#print("")
#for i in range(0,x[1]):
#    print(y, end="")
#print("")
#for i in range(0,x[2]):
#    print(y, end="")
#print("")
from random import *
#opilased = ["Juhan","Kati","Mario","Mario","Mati","Juhan"]
#nimi = input("Mis nimi on otsida: ")

#while nimi not in opilased:
#    nimi = input("Mis nimi on otsSida: ")
#x= opilased.count(nimi)
#if x>1:
#    print(opilased.index(nimi,0, 5))
#    opilased.remove(nimi)
#    x-=1
#    if x==1:
#        print(opilased.index(nimi,0, 5)+1)



x=[1,2,3]
kis= input("kinte 4to nibud: (bumaga,nosznitsi,kamen)")
a= x[randint(0,2)]
print(a)
if kis==a:
    print("ni4ja")
