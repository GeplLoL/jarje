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
try:
    student = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
    student.sort()
    for x in range(0,4):
        print(x)
        for i in range(0,4):
            print(i)
            if x!=0!=i and student[x]==student[i]:
                student.pop(i)
    print(student)
except:
    print(x)