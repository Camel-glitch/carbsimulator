import pandas as pd
import matplotlib.pyplot as plt


def f(row): 
    for c in C : 
        if c in row['french_name'].lower() or c in row['french_tag'].lower() : 
            return c 
    
    return None

dfa = pd.read_csv("aliments.csv")
dfe = pd.read_csv("energie.csv")

C = ['agneau','boeuf','mouton',
     'mollusques et crustacés','poulet','porc','poisson','produits laitiers','oeuf','boissons sans alcool','boisson alcoolisées','chocolat']


dfa_cat = dfa.groupby('cat').mean('CO2') 
dfe_type = dfe.groupby('french_name').mean('CO2') #pour que les lignes soient identifiées au nom de l'énergie

def calculate():

    while True:
        choice = input(
            "Quelle type d'évaluation souhaitez vous faire"\
            "(écrire : hebdomadaire, mensuelle ou annuelle) ?\n"
        )
        if choice in ["hebdomadaire", "mensuelle", "annuelle"]:
            break

        print("Indiquez une réponse dans celles proposées.")

    print("Précisez vos résultats en kg ou en litre pour les liquides\n")
    A = {key :0 for key in C}
    s1 = 0
    #on supposera que 1litre fait 1kg ce qui cohérent puisque la plupart des boissons sont des solutions aqueuses
    for key in A :
        print("Combien de",key,"?")
        x = float(input())*dfa_cat.loc[key,'CO2'] 
        s1 += x 
        A[key] = x
    

    E = {'Electricité':0,'Fioul domestique':0, 'Granulés':0, 'Gaz naturel - 2022' : 0}
    print("Précisez vos résultats en kWh\n")
    s2 = 0 
    for key in E :
        print("Combien de",key,"?")
        x = float(input())*dfe_type.loc[key,'CO2']
        s2 += x 
        E[key] = x

    print("Votre émission",choice,'de CO2 est de',s1,'kg pour les aliments',s2,'kg pour votre consommation énergétique.\n')
    
    bar_carb(A,'aliments','kgCO2','Émission de CO2')
    bar_carb(E,'énergie','kgCO2','Émission de CO2')
    

calculate()