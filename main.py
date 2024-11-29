#### Imports et définition des variables globales
"""importation des modules"""
import sys

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument
     selon un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    caractere = [s[0]]
    occurence = [1]
    i = 0
    for k in range(1, len(s)):
        if s[k] == caractere[i]:
            occurence[i] += 1
        else:
            i += 1
            caractere += s[k]
            occurence.append(1)
    liste = []
    for k in range(i + 1):
        liste.append((caractere[k], occurence[k]))
    return liste


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée
     en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    sys.setrecursionlimit(1100)
    if s == "":
        return []
    # recherche nombre de caractères identiques au premier
    char = s[0]
    count = 1
    while count < len(s) and s[count] == char:
        count += 1
    # appel récursif
    return [(char, count)] + artcode_r(s[count:])
#### Fonction principale


def main():
    """programme principal"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
