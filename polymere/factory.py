
def processing_plant(chaine):
    if not isinstance(chaine, str):
        raise ValueError("Une chaîne de caractere doit être fournie en entrée !!!")
    
    reactions = {}
    
    for lettre in range(ord('a'), ord('z')+1):
        reactions[chr(lettre) + chr(lettre).upper()] = ''
        reactions[chr(lettre).upper() + chr(lettre)] = ''

    while True:
        chaine_modifiee = False

        for reaction, remplacement in reactions.items():
            if reaction in chaine:
                chaine = chaine.replace(reaction, remplacement)
                chaine_modifiee = True

        if not chaine_modifiee:
            break

    return chaine
