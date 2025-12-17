"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    # TODO: sustituye coma por punto, separa, valida y convierte a enteros
    precio = price_str.replace(",",".").strip()
    partes = precio.split(".")

    if len(partes) != 2:
        raise ValueError("El precio no consta de dos decimales")
    
    euros , centimos = partes

    if len(centimos) != 2 or not euros.isdigit() or not centimos.isdigit():
        raise ValueError("Debe contener exactamente dos decimales numéricos")

    euros = int(euros)
    centimos = int(centimos)
    return (euros, centimos)
    

