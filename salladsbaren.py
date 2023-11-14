#Skriven av Filip Eriksson
#Grupp 38
#
#Beskrivning: Programmet ska kunna hantera en vegetarisk kundorder 
#och matcha kundens önskemål med lämpligast menyalternativ.
#Därefter ska kunden komma till menyn med extra val innan
#denne kan betala och få ett kvitto.
#Kostnad för ingredienserna finns på separat fil
#
#
#
#
#
#
#
#


class Beställning():
    """hanterar användarens input som ett objekt"""

    def __init__(self, ingredienser, ändringar, dressing, pris):
        """definierar attributen på salladen"""

        self.ingredienser = ingredienser
        self.ändringar = ändringar
        self.dressing = dressing
        self.pris = pris


    def __str__(self):
        """skriver en sträng som presenterar salladen"""

        return str(self.ingredienser) + " " + str(self.ändringar) + " " + str(self.dressing) + " " + (str(self.pris))

def användare_fritext(): 
    """låter användaren fritt skriva vad de önskar ha i sin sallad (ändringar() inkluderas även här)"""
        

class Meny():
    """importerar menyn från textfilen meny.txt och jämför användarens input med befintliga alternativ"""

    def __init__(self, nummer, namn, ingredienser, pris):
        self.ingredienser = ingredienser
        self.nummer = nummer
        self.namn = namn
        self.pris = pris

def menyläs():
    #en dictionary kan lagra listor, vilket antagligen hjälper när jag lagrar alla ingredienser i ett menyalternativ bakom en ensam siffra (menyalternativet)

    meny = {}
    with open(r"C:\Users\flprk\Desktop\Workstation\Salladsprojekt\meny.txt", "r", encoding="utf-8") as f:
        for rad in f:
            renad_rad = rad.strip()
            print(renad_rad)

    return meny
menyläs()

        """ def läs_meny(): 
            läser in menyn från en textfil
            file = open("meny.txt", "r", encoding="utf-8")
            menyval = file.readline().strip()
            while menyval:
            lastname = str(file.readline().strip())
            surname = str(file.readline().strip())
            new_student = Student(surname, lastname, personalnumber)
            self.students.append(new_student)
            personalnumber = file.readline().strip()
            file.close()"""
        

    def visa_meny():
        """presenterar valen på menyn för användaren"""

    def matcha_sallad(): 
        """undersöker vilka menyalternativ som matchar användarens önskemål och lagrar dessa i en lista"""

    def föreslå_sallad(): 
        """om inget matchar rakt av finns funktionen för att föreslå närmast matchande alternativ"""


class Tillval():
    """importerar tillval från textfilen tillval.txt och låter användaren välja dressing eller lägga till ingredienser"""

    def läs_ingredienser():
        """läser in ingredienserna och tilläggen från en annan textfil"""

    def visa_tillval(): 
        """efter att ha valt allt annat presenteras tillvalen som kan läggas till"""

    def välj_tillval(): 
        """lägger till tillvalen med sina kostnader om användaren vill ha tillval"""



def välj_alternativ(): 
    """låter användaren välja något av alternativen på menyn eller alternativet för fritext"""

def ändringar(): 
    """låter användaren välja om de vill lägga till eller ta bort ingredienser i sin sallad"""

def beräkna_totalkostnad(): 
    """beräknar totalkostnaden baserat på menyval och/eller enskilda ingredienskostnader samt tillvalskostnad"""

def betala_kvitto():
    """användaren får valet om de vill betala, varpå de får ett kvitto, eller börja om med beställningen"""

def main(): 
    """organiserar resterande funktioner i en logisk följd"""


