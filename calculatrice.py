#création d'ne calculatrice simple en python
#déclaration de 02 variables
nombre1=input("Entrez le premier nombre: ")
nombre2=input("Entrez le deuxième nombre: ")
#vérification que les entrées sont des nombres entiers
if not nombre1.isnumeric() or  not nombre2.isnumeric():
    print("Erreur: Veuillez entrer des nombres entiers valides.")
    raise SystemExit("Fin de programme")

nombre1=int(nombre1)
nombre2=int(nombre2)
#demande de l'opération à effectuer
operation=input("Choisissez l'opération à effectuer entre ['+','-','*' ou '/' ] :")
#vérification de l'opérateur
if operation not in ['+','-','*','/']:
    print("Erreur: Opérateur invalide.")
    raise SystemExit("Fin de programme")
if operation=="+":
    resultat=nombre1+nombre2
elif operation=="-":
    resultat=nombre1-nombre2 
elif operation=="*":
    resultat=nombre1*nombre2
elif operation=="/":
    if nombre2==0:
        print("La division par zéro n'est pas autorisée.")
        raise SystemExit("Fin de programme")
    else:
        resultat=round(nombre1/nombre2,2)
else:
    print("Opération invalide")
print("Le résultat de l'opération est:",round(resultat,2))
    
              
            