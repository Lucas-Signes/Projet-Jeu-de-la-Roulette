import random
import time
Th=1000
continuer="oui"
print("***BIENVENUE A LA ROULETTE DU CASINO DE L'EIB ***")
#SAISIR LE NOM DU JOUEUR
def demander_nom():
    Nom=str(input("\nSaisir le nom du joueur: "))
    return Nom
nom=demander_nom()

#NOUVEAU CAPITAL DU JOUEUR
print(nom ,"votre nouveau capital est de:" ,Th, "T")

while Th!=0 and continuer != "non":

#PRESENTATION DE LA MAQUETTE

#LISTE DES QUANTITES
    print("\nPAIR \nIMPAIR \nMANQUE : 1-18 \nPASSE : 19-36 \nROUGE : 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 \nNOIR : 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35\n")

#EXPLICATION DE CHAQUE PARI
    print("Liste des paris :")
    print("*numéro simple (rapporte 36 fois la mise): saisir Num, puis un numéro entre 1 et 36\n*pair (rapporte 2 fois la mise): saisir P impair (rapporte 2 fois la mise) : saisir P\n*impair (rapporte 2 fois la mise) : saisir I")
    print("*manque (numéros de 1 à 18, rapporte 2 fois la mise): saisir M\n*passe (numéros de 19 à 36, rapporte 2 fois la mise) saisir S \n*rouge (rapporte 2 fois la mise): saisir R. \n*noir (rapporte 2 fois la mise): saisir N")
    print("*tiers (rapporte 3 fois la mise): saisir T, puis le numéro du tiers (e.g. T2)\n*colonne (rapporte 3 fois la mise): saisir C, puis le numéro de la colonne (e.g. C3) \n*ligne (rapporte 12 fois la mise): saisir L, puis le numéro de ligne (e.g. L, 7)\n")

    #TIRAGE DU NUMERO AU HASARD
    def tirer_numero():
        n=random.randint(0, 37)
        return n
    n=tirer_numero()

    #FONCTION POUR TROUVER SI N EST PAIR
    def est_pair(n):
        return n%2 == 0

    #FONCTION POUR TROUVER SI N EST IMPAIR
    def est_impair(n):
        return n%2 != 0

    #FONCTION POUR TROUVER SI N EST ROUGE
    def est_rouge(n):
            if n== 1 or n == 3 or  n == 5 or n==7 or n==9 or n==12 or n==14 or n==16 or n==18 or n==19 or n==21 or n==23 or n==25 or n==27 or n==30 or n==32 or n==34 or n==36:
                return True
            else:
                return False
  
    #FONCTION POUR TROUVER SI N EST NOIR
    def est_noir(n):
            if n==2 or n==4 or n==6 or n==8 or n==10 or n==11 or n==13 or n==15 or n==17 or n==20 or n==22 or n==24 or n==26 or n==28 or n==29 or n==31 or n==33 or n==35:
                return True
            else:
                return False
 
    #FONCTION POUR TROUVER SI N EST PASSE
    def est_passe(n):
        return n >= 19  

    #FONCTION POUR TROUVER SI N EST MANQUE
    def est_manque(n):
        return n <= 18

    #FONCTION POUR TROUVER LA LIGNE
    def num_ligne():
        Ln=int(((n-1)//3)+1)
        return Ln
    Ln=num_ligne()

    #FONCTION POUR TROUVER LA COLONNE
    def num_colonne():
        if n%3==1:
            Cn=1
        elif n%3==2:
            Cn=2
        elif n%3==0:
            Cn=3
        return Cn
    Cn=num_colonne()

    #FONCTION POUR TROUVER LE TIER
    def num_tiers():
        if n in range(1,13):
            Tn=1
        elif n in range(13,25):
            Tn=2
        else:
            Tn=3
        return Tn
    Tn=num_tiers()
    
    #DEMANDER AU JOUEUR LEUR PARI
    def demander_pari():
        return input("saisissez votre pari (une saisie invalide entrainera une perte de la mise): ")
    Bet=demander_pari()
    while Bet != "P" and Bet != "I" and Bet != "M" and Bet != "S" and Bet != "R" and Bet != "N" and Bet != "C" and Bet != "T" and Bet != "L" and Bet != "Num":
        Bet = input("saisissez votre pari encore: ")
    if Bet=="L":
        Betl=int(input("Saisissez le ligne: "))
        while Betl not in range(1,13):
                Betl=int(input("Saisissez le ligne: "))
    if Bet=="C":
        Betc=int(input("Saisissez le colonne: "))
        while Betc not in range(1,4):
            Betc=int(input("Saisissez le colonne: "))
    if Bet == "T":
        Bett=int(input("Saisissez le tiers: "))
        while Bett not in range(1,4):
                Bett=int(input("Saisissez le tiers: "))
    if Bet == "Num":
        Betn=int(input("Saisissez le nombre: "))
        while Betn not in range(1,37):
                Betn=int(input("Saisissez un nombre: "))
        
    #DEMANDER AU JOUERU LEUR MISE
    def demander_mise():
        Mise=int(input("\ncombien voulez-vous miser? (mise maximale: 500): "))
        while Mise>500 or Mise<0:
            Mise=int(input("combien voulez-vous miser? Depasser pas la mise maximale: 500: "))
        while Th-Mise<0:
            Mise=int(input("\ncombien voulez-vous miser? (Vous n'avez pas assez de Thune pour ce pari): "))
        return Mise
    Mise=demander_mise()

    #ATTENTE POUR AFFICHER LE RESULTAT
    print("\nAttendez pour votre resultat...")
    time.sleep(4)

    #AFFICHAGE DU TIRAGE
    def afficher_tirage():
        print("\nTirage:",n)
        if est_pair(n):
            print("Pair, ", end="")
        else:
            print("Impair, ", end="")
        if est_rouge(n):
            print("Rouge, ", end="")
        else:
            print("Noir, ", end="")
        if est_passe(n):
            print("Passe")
        else:
            print("Manque")
        print("Ligne:",Ln,", Colonne:", Cn,", Tiers:", Tn,"\n")
    afficher_tirage()
    
    #CALCULATION DU GAIN
    def calculer_gain(n, Bet, Mise):
        Gain = 0
        if Bet==n:
            return Mise*36
        if Bet=="P":
            if est_pair(n):
                return Mise*2
        if Bet=="I":
            if est_impair(n):
                return Mise*2
        if Bet=="M":
            if est_manque(n):
                return Mise*2
        if Bet=="S":
            if est_passe(n):
                return Mise*2
        if Bet=="R":
            if est_rouge(n):
                return Mise*2
        if Bet=="N":
            if est_noir(n):
                return Mise*2
        if Bet==Tn:
            return Mise*3
        if Bet==Cn:
            return Mise*3
        if Bet==Ln:
            return Mise*3
        return Gain
    Gain = calculer_gain(n, Bet, Mise)
    
#AFFICHAGE DU NOUVEAU GAIN SAUF SI N=0
    if n!=0:
        Th=Th-Mise+Gain
    else:
        print("Vous avez perdu\n")
        Th=Th
    print(nom,"votre nouveau capital est de", Th)

    #CONDITION SI VOUS LE JOUEUR A PLUS D'ARGENT
    if Th==0:
        print("\nVous avez perdu car vous n'avez plus de Thune")
        time.sleep(5)
        exit()
        
    #OPTION POUR REJOUER
    continuer=input("\nVoulez vous rejouer ou garder votre mise? (repondez par un 'oui' ou un 'non' sinon la roulette recommencera automatiquement): ")
    if continuer == "oui":
        print("\nContinuer a jouer avec votre capital de", Th)
        if continuer == "non":
            print("Merci pour avoir jouer a la roulette de l'eib! On espere que vous reviendrez")
            time.sleep(3)
            exit()
        