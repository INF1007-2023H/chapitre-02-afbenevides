
def decomposer(secondes):
    secInMinutes = 60
    secInHeures = secInMinutes *60
    secInJour = 24 * secInHeures
    secInSemaine = 7 * secInJour
    secInAnnee = 365 *secInJour

    # TODO: Assigner à la variable "annees" le nombre d'années
    reste_annees=secondes % secInAnnee
    annees = (secondes -reste_annees)//secInAnnee
    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    reste_semaines = reste_annees % secInSemaine
    semaines = (reste_annees - reste_semaines)//secInSemaine

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    reste_jours = reste_semaines % secInJour
    jours = (reste_semaines - reste_jours) // secInJour

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    reste_heures = reste_jours % secInHeures
    heures = (reste_jours - reste_heures)// secInHeures

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    reste_minutes = reste_heures % secInMinutes
    minutes = (reste_heures - reste_minutes) // secInMinutes

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = reste_minutes

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)
    print("{:d} années, {:d} semaines, {:d} jours, {:d} heures, {:d} minutes et {:d} secondes".format(annees ,semaines ,jours ,heures ,minutes ,secondes))

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
