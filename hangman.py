import random
import time
# Hangman toteutettuna Pythonilla

näkyväSana = []
osumia = 0
virheitä = 0
voitto = False
osuma = False
teksti = ""
josyötetyt = []

def GenerateWord():
    listasanoja = ["VALTAVA", "PYRAMIDI", "HÄIRIINTYÄ", "KORVAT", "PALMU", "ENNEUNI", "VAIHTEISTO", "RAHKAPULLA", "MAGNEETTI", "JOHDOT"]
    random.seed(time.time())
    randomIndex = random.randint(0,len(listasanoja)-1)
    #print(randomIndex, len(listasanoja))
    return listasanoja[randomIndex]

def PrintLogo():
    print("  #   #   #   #   #  ###  #   #   #   #   #  ")
    print("  #   #  # #  ##  # #   # ## ##  # #  ##  #  ")
    print("  ##### ##### # # # #     # # # ##### # # #  ")
    print("  #   # #   # #  ## #  ## #   # #   # #  ##  ")
    print("  #   # #   # #   #  ###  #   # #   # #   #  ")
    
def VisibleWord(visWord, alustus, hitIndex):
    sananPituus = 0
    sananPituus = len(sana)*2
    if alustus:
        i = 0
        while (i < sananPituus):
            if (i%2 == 0):
                visWord.append("_")
            else:
                visWord.append(" ")
            i += 1
    else:
        if hitIndex != -1:
            visWord[hitIndex*2] = sana[hitIndex]
    return visWord


def CheckLetter():
    i = 0
    while i<len(josyötetyt):
        if arvaus == josyötetyt[i]:
            return 1
        i += 1
    return 0

def PrintHangman(errors):
    if errors == 0:
        print("")
        print("")
        print("")
        print("            ",teksti)
        print("")
        print("")
        print("")
        print("")
        print("")
    elif errors == 1:
        print("")
        print("")
        print("")
        print("            ",teksti)
        print("")
        print("")
        print("")
        print("============")
        print("|          |")
    elif errors == 2:
        print("")
        print("  +         ")
        print("  |         ")
        print("  |         ",teksti)
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("============")
        print("|          |")
    elif errors == 3:
        print("")
        print("  +----+    ")
        print("  |         ")
        print("  |         ", teksti)
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("============")
        print("|          |")
    elif errors == 4:
        print("")
        print("  +----+    ")
        print("  |    |    ")
        print("  |         ", teksti)
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("============")
        print("|          |")
    elif errors == 5:
        print("")
        print("  +----+    ")
        print("  |    |    ")
        print("  |    o    ", teksti)
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("============")
        print("|          |")
    elif errors == 6:
        print("")
        print("  +----+    ")
        print("  |    |    ")
        print("  |    o    ", teksti)
        print("  |    |    ")
        print("  |         ")
        print("  |         ")
        print("============")
        print("|          |")
    elif errors == 7:
        print("")
        print("  +----+    ")
        print("  |    |    ")
        print("  |    o    ", teksti)
        print("  |   /|    ")
        print("  |         ")
        print("  |         ")
        print("============")
        print("|          |")
    elif errors == 8:
        print("")
        print("  +----+    ")
        print("  |    |    ")
        print("  |    o    ", teksti)
        print("  |   /|\\  ")
        print("  |         ")
        print("  |         ")
        print("============")
        print("|          |")
    elif errors == 9:
        print("")
        print("  +----+    ")
        print("  |    |    ")
        print("  |    o    ", teksti)
        print("  |   /|\\  ")
        print("  |   /     ")
        print("  |         ")
        print("============")
        print("|          |")
    elif errors == 10:
        print("")
        print("  +----+                  ")
        print("  |    |    HÄVISIT PELIN!")
        print("  |    o    ")
        print("  |   /|\\  <- SINÄ       ")
        print("  |   / \\                ")
        print("  |                       ")
        print("============              ")
        print("|          |              ")

# Vaihe 0: Tulosta Logo
PrintLogo()

# Vaihe 1: Valitse sana luettelosta randomilla
sana = GenerateWord()
#print(sana)

# Vaihe 2: Tulosta _ jokaista merkkiä kohden ja näytä se pelaajalle
näkyväSana = VisibleWord(näkyväSana, True, -1)
for letter in näkyväSana:
    print(letter, end="")
print("")


# Vaihe 3: Tulosta tyhjä kenttä
PrintHangman(virheitä)

# Vaihe 4: Game Loop
while (voitto == False and virheitä < 10):
    # Vaihe 4.1: Pelaaja arvaa kirjaimen
    arvaus = input("Syötä kirjain: ").lower()           # .lower() muuttaa syötetyn merkin pieneksi kirjaimiksi

    # Vaihe 4.2: Verrataan syötettyä kirjainta jo syötettyihin
    merkkiarvo = CheckLetter()
    if merkkiarvo == 1:
        print(f"Syötit saman merkin {arvaus} toistamiseen")

    # Vaihe 4.3: Jos uusi merkki niin lisätään se syötettyihin
    elif merkkiarvo == 0:
        josyötetyt.append(arvaus)

        # Vaihe 4.4: Verrataan syötettyä merkkiä valitun sanan merkkeihin
        # Jos kirjain löytyy niin näytetään se sanassa ja lisätään osumia yhdellä
        i = 0
        while i < len(sana):
            if arvaus == sana[i].lower():
                osuma = True
                osumia += 1
                näkyväSana = VisibleWord(näkyväSana, False, i)
            i += 1

    # Vaihe 4.5: Jos kirjainta ei löydy sanasta niin lisätään virheiden määrää
    if osuma == False:
        näkyväSana = VisibleWord(näkyväSana, False, -1)
        virheitä += 1
    else:
        osuma = False

    # Vaihe 4.6: Jos osumia on yhtä monta kuin sanan pituus, niin voitto
    if osumia == len(sana):
        voitto = True
        teksti = "Voitit Pelin"
    # Vaihe 4.7: Tulostetaan hirsipuun vaihe
    # Jos hirsipuu tulee valmiiksi niin hävisit pelin
    for letter in näkyväSana:
        print(letter, end="")
    print("")
    PrintHangman(virheitä)