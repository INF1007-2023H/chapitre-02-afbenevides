def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat et retourner celle-ci avec le mot-clé return.

    # véfiier si est multiple de 3
    if n % 3 == 0:
        is3multiple = True
    else:
        is3multiple = False

    # véfiier si est multiple de 5
    if n % 5 == 0:
        is5multiple = True
    else:
        is5multiple = False

    # véfiier n est dans quel cas et imprimer le bon output
    if is3multiple and is5multiple:
        resultat ="fizzbuzz"
    elif is3multiple:
        resultat = "fizz"
    elif is5multiple:
        resultat = "buzz"
    else:
        resultat = n

    print(resultat)
    return resultat


if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    fizzBuzz(n)
