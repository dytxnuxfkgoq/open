"""uj=open("nevbekeres.txt","w",encoding="UTF-8")
szo=""
while szo!="vége":
    szo=input("Kérek egy nevet:")
    if szo!="vége":
        uj.write(szo+"\n")
uj.close()

uj2=open("nevbekeres.txt","w",encoding="UTF-8")
szo=""
while szo!="vége":
    szo=input("Kérek egy nevet:")
    if szo[0] == "A":
        uj2.write(szo+"\n")"""


f=open("szamok.txt",encoding="UTF-8")
list = []
for sor in f:
    list.append(sor.strip())
print(list)

#Összegzés
"""osszeg=0
for i in list:
    osszeg+= int(i)
print(osszeg)
print("átlag:",osszeg/len(list))

db= 0
parososszeg=0
for x in list:
    if x % 2 == 0:
        db += 1
        parososszeg += x
print(parososszeg/db)"""

#eldöntés
van=False
i=0
while not van and i<len(list):
    if list[i]%3==0:
        van=True
    i+=1
if van:
    print("van benne 3a osztható szám","indexe:",i)
else:
    print("nincs benne 3al oszt szam")
    
    
vegyeslista = ["alma",400,"körte",650,500,"narancs"]
szamok = []
gyumolcsok = []
for x in vegyeslista:
    if type(x) == str:
        gyumolcsok.append(x)
    else:
        szamok.append(str(x))

print(szamok)
print(gyumolcsok)

vegyes = open("vegyes.txt","w", encoding="UTF-8")
for sor in vegyeslista:
    vegyes.write(str(sor)+"\n")
print(vegyeslista)    

#minimum keresés a listában
list = [6,4,79,56,42,7,5,43,8]
print(list)
min=list[0]
for i in list:
    if i<min:
        min=i
print("A legkissebb elem:",min)        

#maximum keresés a listában
max=list[0]
for i in list:
    if i>max:
        max=i
print("A legnagyobb elem:",max)

osztalyzat = open("osztalyzatok.txt","r", encoding="UTF-8")
list = []
for sor in osztalyzat:
    list.append(sor.strip()[-1])

osztalyzat.close()    
osszeg=0
db5=0
print(list)
for i in list:
    print(i[-1])
    n=int(i[-1])
    osszeg+=n
    if n==5:
        db5+=1
print("Jegyek átlaga:", osszeg/len(list))    
print("Ennyi darab ötös van:",db5)"""

bevasarlas = open("bevasarlas.txt","r",encoding="UTF-8")
list = []
for sor in bevasarlas:
    list.append(sor.strip().replace("Ft","").replace("ft","").split())
bevasarlas.close()
print(list)    
osszeg = 0
for i in list:
    n=int(i[-1])
    if n>500:
        print(" ".join(i),"drága termék")
    else:
        print(" ".join(i),"normális árú")        
    osszeg+=n
print("Ennyit fizettem:",osszeg)

import random

list = []
for x in range(20):
    x = random.randint(0,30)
    list.append(x)
print(list)    

legkisebb = list[0]
for x in list:
    if x<legkisebb:
        legkisebb = x
print(f"{legkisebb} a legkisebb szám")

legnagyobb = list[0]
for x in list:
    if x>legnagyobb:
        legnagyobb = x
print(f"{legnagyobb} a legnagyobb szám")

otkisebb = 0
otnagyobb = 0
for x in list:
    if x < 15:
        otkisebb+=1
    else:
        otnagyobb+=1
print(f"{otkisebb} tizenotnel kisebb es {otnagyobb} nagyobb van")

for x in range(len(list)):
    print(x,list[x])

f = open("veletlen.txt","w",encoding="UTF-8")
for sor in list:
    x = str(sor)
    f.write(x+"\n")
f.close()

osszeg = 0
for x in list:
    osszeg += x
print(osszeg//len(list))

def prim(a):
    oszto=0
    for x in range(1,a+1):
        if a % x == 0:
            oszto+=1
    if oszto==2:
        return "prim"
    else:
        return "nem prim"

for i in list:
    print(i,prim(i))

nev = input("Kérek egy nevet:")
for x in nev:
    print(x)

f = open("nagybetus.txt","w",encoding="UTF-8")
szo = input("Kérek egy szót:")
for sor in szo:
    f.write(sor.upper()+"\n")   
    

a = open("nagybetus.txt","a",encoding="UTF-8")
varos1 = input("Város 1:")
varos2 = input("Város 2:")
varos3 = input("Város 3:")
varosok=varos1
a.write(varosok)
a.close()
    
z = open("nagybetus.txt","r",encoding="UTF-8")
if "Veszprém" in z or "VESZPRÉM" in z:
    print("van")
else:
    print("nincs")
