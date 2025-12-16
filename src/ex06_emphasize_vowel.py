"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.

La función debe:

Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.

Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.

Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(phrase: str, vowel: str) -> str:
    """
    Convierte a mayúscula todas las apariciones de vowel en la frase.
    Sugerencia:
    - Comprueba que vowel es un solo carácter y está en "aeiou" (en minúscula).
    - Recorre la frase carácter a carácter y construye una nueva cadena.
    """
    # TODO: validar y transformar
    minuscula = vowel.lower()
    vocal = ("a", "e", "i", "o", "u")
    if len(vowel) != 1:
        raise ValueError("La vocal es más de 1 cáracter")
    
    if minuscula not in vocal:
        raise ValueError("La letra introducida no es una vocal")
    
    frase = ""

    for char in phrase:
        if char.lower() == minuscula:
            frase += char.upper()
        else:
            frase += char
    return frase
