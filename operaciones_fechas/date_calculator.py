from datetime import datetime

FORMATO="%d/%m/%Y" #constante que define el formato de las fechas


# devuelve el numero de días entre dos fechas
# comprueba cual de las dos fechas es mayor y devuelve la diferencia
def day_between_dates(date1:str ,date2:str):
    retorno = 0
    date_format1 =datetime.strptime(date1, FORMATO)
    date_format2 = datetime.strptime(date2, FORMATO)
    if date_format1 > date_format2:
        retorno = (date_format1 - date_format2).days
    else:
        retorno = (date_format2 - date_format1).days    
    return retorno

# comprueba si el formato de las fechas es correcto
# devuelve un booleano de acuerdo a si las fechas son correctas o no
def date_true_or_false(date1:str, date2:str):
    retorno = False
    try:
        date_format1 = datetime.strptime(date1, FORMATO)
        date_format2 = datetime.strptime(date2, FORMATO)
        retorno = True
    except ValueError:  
        retorno = False
    return retorno  