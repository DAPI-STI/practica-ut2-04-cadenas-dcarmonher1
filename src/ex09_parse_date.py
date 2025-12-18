"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    fecha = date_str.strip().split("/")

    if len (fecha) != 3:
        raise ValueError("La fecha debe de estar entre /")
    
    dia, mes, año = fecha

    dia = int(dia)
    mes = int(mes)
    año = int(año)
    
    if not (1 <= dia <= 31):
        raise ValueError("El día debe estar entre 1 y 31")
    
    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12")
    
    if not (1 <= año <= 9999):
        raise ValueError("El año debe estar entre 1 y 9999")

    return (dia, mes, año)