def affiche(n):
    for nombre in range(1, n+1):
        resultat = ""
        if nombre % 3 == 0:
            resultat += "Fizz"
        if nombre % 5 == 0:
            resultat += "Buzz"
        if nombre % 3 == 0 and nombre % 5 == 0:
            resultat += "FrisBee"
        print(resultat or nombre)

affiche(15)  
affiche(100)