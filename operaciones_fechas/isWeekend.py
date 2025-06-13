from datetime import datetime

FORMATO="%d/%m/%Y" #constante que define el formato de las fechas

def is_weekend(date_str):
    retorno = False
    """
    devuelve un booleano , true si la fecha proporcionada es fin de semna
    caso contrario devuelve false
    devuelve un numero del 0 al 6 empezando por el lunes que es 0 
    """

    day_week = datetime.strptime(date_str, FORMATO)
    if day_week.weekday() >= 5:
        retorno = True  
    else:
        retorno = False
    
    return retorno

