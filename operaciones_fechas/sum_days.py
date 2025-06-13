from datetime import datetime, timedelta

FORMATO="%d/%m/%Y" #constante que define el formato de las fechas

def sumar_dias(fecha_str, num_dias, ):

    date_format1 = datetime.strptime(fecha_str, FORMATO)
    new_date = date_format1 + timedelta(days=num_dias)
    return new_date.strftime(FORMATO)