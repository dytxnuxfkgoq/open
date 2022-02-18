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
