#Svaki korak desno upucate zombija, a svaki lijevo covjeka (kada upucas nekog skines mu jedan bod zivota)
#Kada dodje do 0 umire (treba poruka koliko mu je zivota ostalo i poruka da je umro i program da zavrsi)
#Potrebna poruka i u kojem smjeru se kreces.
Zombie = 5 #zivotni bodovi zombija
Human = 5 #zivotni bodovi covjeka
hodanje = input("Gdje zelite ici(d/l): ")
while Human != 0 and Zombie != 0: 
    input(" Pritisni enter da pucas ")
    if hodanje == "d" or hodanje == "desno":
        print(" Bravo, upucali ste zombija ")
        Zombie -= 1
        if Zombie == 0:
            print(" Zombie je mrtav ")
        else:    
            print(" Zombiju je ostalo jos " + str(Zombie) + " zivota ")
    elif hodanje == "l" or hodanje == "lijevo" :
        print(" Bravo, upucali ste covjeka ")
        Human -= 1
        if Human == 0:
            print(" Covjek je mrtav ")
        else:
            print(" Covjeku je ostalo jos " + str(Human) + " zivota ")
            