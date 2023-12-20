def salad_till_nykund(choice):
    val = []
    ingredienser = ""
    ingAvail = []
    fuckOfffPython = []
    with open(choice+"ing.txt", "r") as textFile:
        for line in textFile:
            ingtemp = line.strip("\n").split(", ")
            ingAvail.append(ingtemp[0])
    textFile.close()
    

    print("Hej o välkommen till saladsbaren")
    print("Skriv vilka ingerdiense du vill ha.")
    print("Skriv klar när du är nöjd.")

    while ingredienser != "klar":
            ingredienser = input("Ingredienser: ")
            ingredienser.lower()
            fuckOfffPython.append(ingredienser)
            avail = set(ingAvail).intersection(fuckOfffPython)
            if ingredienser == "klar":
                break
            elif len(avail) == 0:
                print("Detta är inte en ingrediens vi erbjuder. Försök igen.")
                avail.clear()
                fuckOfffPython.clear()
                continue
            else:
                val.append(ingredienser)
                avail.clear()
                fuckOfffPython.clear()
    return val
        


def printaKvitto(extraSallad, winner, totSum):
    hjälp = ""
    sug = 0
    with open("kvitto.txt", "w") as kvitto:

        if extraSallad == []:
            kvitto.write("Vald sallad: "+winner[0])
            kvitto.write(" ")
            kvitto.write("Total kostnad: "+winner[1])
        else:
            del extraSallad[-1]
            hjälp = " ".join(extraSallad)
            sug = int(winner[1]) + int(totSum)
            kvitto.write("Vald sallad: "+winner[0])
            kvitto.write(" ")
            kvitto.write("Valda tillbehöver: "+hjälp)
            kvitto.write(" ")
            kvitto.write("Total Kostnad: " + str(sug))


def extra_ing(extraSalad, winner, choice):
    totSum = 0
    extraIng = ""
    val = []
    extraVal = input("Vill du ha något extra till din sallad? ").lower()
    if extraVal == "nej":
        print("OK, här kommer kvittot")
        printaKvitto(extraSalad, winner, winner[2])
    elif extraVal == "ja":
        with open(choice+"ing.txt", "r") as textFile:
            for line in textFile:
                print(line.strip("\n")+"kr")
            while extraIng != "klar":
                extraIng = input("Ingredienser: ")
                extraIng.lower()
                val.append(extraIng)
                with open(choice+"ing.txt", "r") as textFile:
                    for item in textFile:
                        extraVal = item.strip("\n").split(", ")
                        if extraVal[0] == extraIng:
                            help = int(extraVal[1])
                            totSum = help + totSum
                        else:
                            continue
    printaKvitto(val, winner, totSum)

def val_av_sallad(val, choice):
    winner = ["", "", 0]
    addedIng = []
    neededIng = []
    with open(choice+".txt", "r") as textFile:
        for line in textFile:
            Sallader = line.strip("\n").split(", ")
            saladName = Sallader[0]
            saladPrice = Sallader[1]
            sal = set(Sallader).intersection(val)
            if len(sal) == int(Sallader[2]):
                print("Du tänker på", saladName)
                winner[0] = saladName
                winner[1] = saladPrice
                winner[2] = len(sal)
                break
            elif len(sal) < int(Sallader[2]):
                if len(sal) > int(winner[2]):
                    addedIng.clear()
                    neededIng.clear()
                    winner[0] = saladName
                    winner[1] = saladPrice
                    winner[2] = len(sal)
                    del Sallader[:3]
                    neededIng = set(Sallader) ^ set(val)
                    for i in neededIng:
                        addedIng.append(i)
            #elif len(sal) == int(winner[2]):

                
    if len(sal) != int(winner[2]):
        print("Den salladen som mest matchar dinna val är", winner[0], "men då behöva dessa ingredienser läggas till:")
        for item in addedIng:
            print(item)
    print("Denna sallad kommer att kosta", winner[1],"kr")
    textFile.close()
    return winner

class Main:
    print("välj bar 1) salladsbar 1 2) salladsbar 2")
    choice = input()
    extraSalad = []
    val = salad_till_nykund(choice)
    winner = val_av_sallad(val, choice)
    while True:
        chooseSalad = input("Vill du köpa denna sallad? ja/nej: ").lower()
        if chooseSalad == "ja":
            extra_ing(extraSalad, winner, choice)
            break
        elif chooseSalad == "nej":
            val = salad_till_nykund()
            winner = val_av_sallad(val)
        else:
            print("verkar som du skrev in något felaktigt, försök igen.")
