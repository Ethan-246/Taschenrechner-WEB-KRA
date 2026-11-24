def addieren(a, b):
    return a + b

def multiplication (a,b):
    return a * b 

def Division (a,b):
    return a / b

def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")

    Zahl1 = float(input("Bitte Zahl 1 eingeben:"))
    Zahl2 = float(input("Bitte Zahl 2 eingeben:"))
    match wahl:
        case "1":
            print("Resultat: {}".format(addieren(Zahl1,Zahl2)))
        case "2":
            print("test")
        case "3":
            print("Resultat: {}".format(multiplication(Zahl1,Zahl2)))
        case "4":
             print("Resultat: {}".format(Division(Zahl1,Zahl2)))
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()
