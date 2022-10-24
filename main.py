"""
-----------------------------------------------------------------
Die ist das Spiel FizzBuzz

Ich teste gleichzeitig das anlegen über GitHub
Information hierzu mache ich in lokalen Infos in Notizen

Das Spiel 
"FizzBuzz" ist ein Gruppen-Wortspiel für Kinder, 
das ihnen etwas über die mathematische Division beibringen soll. 
Die Spieler zählen abwechselnd inkremental, wobei jede 
durch drei teilbare Zahl durch das Wort „Fizz“ und 
jede durch fünf teilbare Zahl durch das Wort „Buzz“ ersetzt wird. 
-----------------------------------------------------------------
"""

# starten des Spiel mit anlegen von Klassen, def´s und Variablen

# Modul Import
import random
import os


# Variablen
weiterspielen = True
ratezahl = 0

# Klassen

# Definitionen
def spielende():
    schleife = True
    while schleife:
        ende = input("\n\nSpiel beenden? (J=Ja / N=Nein): ")
        ende = ende.upper()
        if ende == "N":
            return True
        elif ende == "J":
            print("Okay, Tschau.")
            return False
        else: 
            continue

def fehler1():
    print("""
    ----------
    -> mööp <-
    ----------
    """)

def fehlerfizzbuzz():
    print("""
    --------------------------
    -> ....mööp....FizzBuzz <-
    --------------------------
    """)

def fehlerfizz():
    print("""
    --------------------------
    -> ....mööp....Fizz.... <-
    --------------------------
    """)

def fehlerbuzz():
    print("""
    --------------------------
    -> ....mööp....Buzz.... <-
    --------------------------
    """)

def richtigfizz():
    print("""
    ----------
    -> Fizz <-
    ----------
    """)

def richtigbuzz():
    print("""
    ----------
    -> Buzz <-
    ----------
    """)

def richtigfizbuzz():
    print("""
    --------------
    -> FizzBuzz <-
    --------------
    """)



# Starten der Hauptschleife für die Wiederholung des Spieles
while weiterspielen:
    # Begrüßung und Spielerklärung
    os.system("cls")
    print("""
    ----------------------------------------------------------------
    Hallo, ich bin das Spiel FizzBuzz.
    
    Ich zähle von 1 die Zahlen hoch.
    und du sollst mir sagen ab die Zahl durch 3 oder 5 teilbar ist.
    
    Bei Teilbarkeit durch 3     drücke bitte "F"  + (Enter) für Fizz     
    Bei Teilbarkeit durch 5     drücke bitte "B"  + (Enter) für Buzz     
    Bei Teilbarkeit durch 3+5   drücke bitte "FB" + (Enter) für FizzBuzz 
    
    Wenn die Zahlen nicht durch 3 oder 5 teilbar sind drücke nur (Enter)
    Die Eingabe von E und (Enter) beendet das Spiel.
    
    Genug der Erklärungen, jetzt wird gespielt.
    
    Viel Spaß.
    ----------------------------------------------------------------
    """)
        
    # Starten mit ratezahl = 1
    ratezahl = 0
    zaehlelauf = True
    Zaehler3richtig = 0
    Zaehler5richtig = 0
    Zaehler8richtig = 0
    Zaehler3falsch = 0
    Zaehler5falsch = 0
    Zaehler8falsch = 0

    # Beginn der inkrementation
    while zaehlelauf:
        
        # Ausgabe der ratezahl und Eingabeabfrage "F=Fizz / B=Buzz / Enter=Weiter / E=Ende"
        ratezahl += 1
        usereingabe = input(f"Die Zahl ist {ratezahl}. Deine Antwort? (F/B/FB/E/Enter :")
        usereingabe = usereingabe.upper()
        
        # Auswertung der Eingabe und Steuerung des weiteren Ablauf
        if usereingabe == "F":
            if ratezahl%3 == 0:
                richtigfizz()
                Zaehler3richtig += 1
            else:
                fehler1()
                Zaehler3falsch += 1
            continue
            
        elif usereingabe == "B":
            if ratezahl%5 == 0:
                richtigbuzz()
                Zaehler5richtig += 1
            else:
                fehler1()
                Zaehler5falsch += 1
            continue
                        
        elif usereingabe == "FB":
            if ratezahl%3+ratezahl%5 == 0:
                richtigfizbuzz()
                Zaehler8richtig += 1
            else:
                fehler1()
                Zaehler8falsch += 1
            continue
                        
        elif usereingabe == "E":
            weiterspielen = spielende()
            zaehlelauf = False
            break
        else:
            if ratezahl%3+ratezahl%5 == 0:
                fehlerfizzbuzz()
                
            elif ratezahl%3 == 0:
                fehlerfizz()

            elif ratezahl%5 == 0:
                fehlerbuzz()

            continue

print(f"""
---------------------------------------
Deine Statistik: 
---------------------------------------
richtig Fizz     = {Zaehler3richtig}
richtig Buzz     = {Zaehler5richtig}
richtig FizzBuzz = {Zaehler8richtig}
falsch Fizz      = {Zaehler3richtig}
falsch Buzz      = {Zaehler5richtig}
falsch FizzBuzz  = {Zaehler8richtig}
Zahlenbereich war bis = {ratezahl}
---------------------------------------

""")

