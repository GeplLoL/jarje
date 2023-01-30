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
#10 funktsioonid
  if x.isdigit()==False or int(x) not in range(1,11):
      continue
  x=int(x)
  print()
  text=input("Sisestage tekst, mille alusel soovite tegutseda\n")
  if x==1:
      print("Teksti pikkus - ",len(text)) # .len() показывает длину строки
  elif x==2:
      rep1=input("Mida asendada?\n")
      rep2=input("Millist sümbolit peaksin asendama?\n") 
      arv=input("Mitu korda vahetada?\n")
      while arv.isdigit()==False:
          arv=input("Kirjuta õige arv!\n")
      print("Uus text - ", text.replace(rep1,rep2,int(arv))) # .replace(x,y,i) заменяем x на y, i раз
  elif x==3:
      print("Kontrollige, kas tekst koosneb numbritest: ", text.isdigit()) # .isdigit() проверяем состоит ли строка лишь из цифр
  elif x==4:
      print("Kontrollige, kas tekst koosneb tähtedest: ", text.isalpha()) # .isalpha() проверяем состоит ли строка лишь из букв
  elif x==5:
      print("Kontrollige, kas tekst koosneb väiketähtedest: ", text.islower()) # .isdigit() проверяем состоит ли строка лишь из букв нижнего регистра
  elif x==6:
      print("Kontrollige, kas tekst koosneb suurtähtedest: ", text.isupper()) # .isupper() проверяем состоит ли строка лишь из буква верхнего регистра
  elif x==7:
      print("Kontrollige, kas 1 täht on suur ja ülejäänud on väikesed: ", text.istitle()) # .istitle() проверяем является ли 1 буква верхним регистром,
                                                                                          #а остальные нижним регистром
  elif x==8:
      print("Muutes kõik tähed väikeseks")
      print("Uus text - ", text.lower()) # .lower() делаем все буквы нижним регитром
  elif x==9:
      print("Muutes kõik tähed suurseks")
      print("Uus text - ", text.upper()) # .lower() делаем все буквы верхним регитром
  else:
      print("Tehke esimene täht suur ja ülejäänud väike")
      print("Uus text -", text.title()) # .title() делаем первую букву верхним регистром, а остальные нижним.
  vali=input("Kas soovite veel proovida (jah või ei)?\n").lower()
  while vali not in ["jah","ei"]:
      vali=input("Kirjutage ainult jah või ei\n").lower()
  if vali=="jah":
      continue
  else:
      break
