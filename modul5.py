from peel_p50 import peel
names = ["Markus", "Kalle", "Erik"]

for x in names:
    print(x)

names[0] = "Karl-bertil"

for x in names:
    print(x)

amount = len(names)
print(amount)

names.append("Markus")
for x in names:
    print(x)

names.pop(2)
for x in names:
    print(x)
while True:
    for x in names:
        print(x)
    u = True
    x=input("""Lägg till i listan skriv 1
Ta bort från listan skriv 2
Lära dig om peel p50 skriv 3\n""")
    if x == "1":
        y=input("Vad vill du lägga till\n")
        names.append(y)
        for x in names:
            print(x)
    if x == "2":
        z = 0
        for x in names:
            print(z, x)
            z+=1
        if z == 0:
            print("Det finns inget att ta bort i listan")
            continue
        else:
            while u == True:
                try:
                    y=int(input("Vilken vill du ta bort\n"))
                    names.pop(y)
                    u = False
                except:
                    print("Endast nummer under", z)
    if x == "3":
        break
    else:
        print("skriv bara 1, 2 eller 3")
while True:
    knowledge = input("""Vad vill du lära dig om Peel P50
1, motorns storlek
2, produktionsåren
3, topphastigheten
4, vikten
5, storleken av besten
6, priset med jämförelse idag""")
    if knowledge == "1":
        print("Peel P50 hade en motorvolym på", peel["engine"],"\n")
    elif knowledge == "2":
        print("Peel P50 producerades", peel["production"], "\n" )
    elif knowledge == "3":
        print("Peel P50 hade en topphastighet av", peel["speed"], "\n" )
    elif knowledge == "4":
        print("Peel P50 vägde", peel["weight"], "\n" )
    elif knowledge == "5":
        print("Peel P50 hade en storlek på", peel["size"], "\n" )
    elif knowledge == "6":
        print("Peel P50 kostade", peel["price"], "men den har auktionerats ut för £100,000", "\n" )
    else:
        print("Endast nummer 1-6")