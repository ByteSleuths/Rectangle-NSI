def affiche_rectangle(L, l):
    """
    Affiche un rectangle de longueur L et de largeur l dans la console.
    
    La longueur L correspond au nombre de caractères de la ligne supérieure et inférieure du rectangle (minimum 2).
    La largeur l correspond au nombre de lignes verticales entre la ligne supérieure et inférieure (minimum 2).
    
  
  :param L (int): Longueur du rectangle (supérieur ou égal à 2).
  :param l (int): Largeur du rectangle (supérieur ou égal à 2).
    
    Exemple d'utilisation :
    >>> affiche_rectangle(7, 4)
    +-----+
    |     |
    |     |
    +-----+
    
    >>> affiche_rectangle(12, 2)
    +----------+
    +----------+
    
    """
    if L < 2 or l < 2:
        raise ValueError("Les paramètres L et l doivent être supérieurs ou égaux à 2.")
    
    print("+" + "-" * (L - 2) + "+")
    
    for _ in range(l - 2):
        print("|" + " " * (L - 2) + "|")
    if l > 1:
        print("+" + "-" * (L - 2) + "+")
