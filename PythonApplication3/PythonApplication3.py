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


x=["kamen", "bumaga", "nosznitsi"]
win=[("kamen","nosznitsi"),("bumaga","kamen"),("nosznitsi","bumaga")]
xy=0
xy1=0
xy2=0
game =input("robot või player: ")
while game!="robot" and game!="player":
    game =input("robot või player: ")
if game=="robot":
    for i in range(1,4):
        robot = x[randint(0,2)]
        y=input("choose kamen, bumaga, nosznitsi : ")
        while y not in x:
            y=input("choose kamen, bumaga, nosznitsi : ")
        if y == robot:
            print("ni4ja")
            xy+=1
        elif (y,robot) in win:
            print("ti win")
            xy1+=1
        else:
            print("you proigral")
            xy2+=1
    print(f"ni4ja: {xy} , you win: {xy1}, you proigral: {xy2}")
elif game=="player":
    for i in range(1,4):
        print(f"{i} game")
        y=input("Player1 choose kamen, bumaga, nosznitsi : ")
        while y not in x:
            y=input("Player1 choose kamen, bumaga, nosznitsi : ")
        player=input("Player2 choose kamen, bumaga, nosznitsi : ")
        while player not in x:
            player=input("Player2 choose kamen, bumaga, nosznitsi : ")
        if y == player:
            print("ni4ja")
            xy+=1
        elif (y,player) in win:
            print("player 1 win")
            xy1+=1
        else:
            print("player 2 win")
            xy2+=1
    print(f"ni4ja: {xy} , player1 win: {xy1}, player2 win: {xy2}")
