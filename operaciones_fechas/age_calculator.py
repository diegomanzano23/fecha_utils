from datetime import datetime

FORMATO="%d/%m/%Y" #constante que define el formato de las fechas

def calcular_edad(fecha_str):
    """
    Calcula la edad de una persona a partir de su fecha de nacimiento en formato string

    si el dia y el mes de la fecha actual son menores que el día y el mes de la fecha de nacimiento,
    se resta un año a la edad calculada

    """
    fecha_nacimiento = datetime.strptime(fecha_str, FORMATO)
    fecha_actual = datetime.now()
    
    edad = fecha_actual.year - fecha_nacimiento.year
    
    # Ajustar si aún no ha pasado el cumpleaños en el año actual
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return edad
