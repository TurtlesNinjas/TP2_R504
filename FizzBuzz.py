def affiche():

    for nombre in range(1, 101):
        resultat = ""

        if nombre % 3 == 0:
            resultat += "Fizz"
        if nombre % 5 == 0:
            resultat += "Buzz"
        print(resultat or nombre)
affiche()
