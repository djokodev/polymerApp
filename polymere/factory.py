import re

def processing_plant(chaine):
    if not isinstance(chaine, str):
        raise ValueError("Une chaîne de caractere doit être fournie en entrée !!!")
    
    if any(char.isdigit() for char in chaine):
        raise ValueError("La chaîne ne doit pas contenir de chiffres !")
    
    special_characters = r"[^A-Za-z0-9]"
    if re.search(special_characters, chaine):
        raise ValueError("La chaîne ne doit pas contenir des caractères spéciaux ou des espaces")
    
    reactions = {}
    
    for lettre in range(ord('a'), ord('z')+1):
        reactions[chr(lettre) + chr(lettre).upper()] = ''
        reactions[chr(lettre).upper() + chr(lettre)] = ''

    reaction_count = 0 

    while True:
        chaine_modifiee = False

        for reaction, remplacement in reactions.items():
            if reaction in chaine:
                chaine = chaine.replace(reaction, remplacement)
                chaine_modifiee = True
                reaction_count += 1

        if not chaine_modifiee:
            break

    return chaine, reaction_count
