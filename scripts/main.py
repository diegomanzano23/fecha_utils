import sys
sys.path.append("C:/Master/fecha_utils/operaciones_fechas/")

import date_calculator
import age_calculator
import isWeekend    
import sum_days


def main():
    print("=================================================")
    print("Bienvenido al programa de operaciones con fechas.")
    print("=================================================")

if __name__ == "__main__":
    main()
    def mostrar_menu():
        print("Seleccione una funcionalidad:")
        print("1. calcular los días entre dos fechas")
        print("2. suamar días a una fecha")
        print("3. saber si una fecha es fin de semana")
        print("4. calcular la edad ")   
        print("5. salir")

    def ejecutar_funcionalidad(opcion):
        if opcion == "1":
            fecha1 = input("Ingrese la primera fecha (DD/MM/YYYY): ")
            fecha2 = input("Ingrese la segunda fecha (DD/MM/YYYY): ")

            if date_calculator.date_true_or_false(fecha1,fecha2 ):
                print("=================================================")
                print(date_calculator.day_between_d1ates(fecha1, fecha2))
                print("=================================================")
           
        elif opcion == "2":
            fecha = input("Ingrese la fecha (DD/MM/YYYY): ")
            dias = int(input("Ingrese la cantidad de días a sumar: "))
            if date_calculator.date_true_or_false(fecha, fecha):
                print("=================================================")
                print(sum_days.sum_days(fecha, dias))
                print("=================================================")
            
        elif opcion == "3":
            fecha = input("Ingrese la fecha (DD/MM/YYYY): ")
            if date_calculator.date_true_or_false(fecha, fecha):
                # Verificar si la fecha es fin de semana
                if isWeekend.is_weekend(fecha):
                     print("=================================================")
                     print("La fecha es fin de semana.")
                     print("=================================================")
                else:
                     print("=================================================")
                     print("La fecha no es fin de semana.")
                     print("=================================================")
            
        elif opcion == "4":
            fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/YYYY): ")
            if date_calculator.date_true_or_false(fecha_nacimiento, fecha_nacimiento):
                edad = age_calculator.calcular_edad(fecha_nacimiento)
                print("=================================================")
                print(f"Su edad es: {edad} años.")
                print("=================================================")
        elif opcion == "5":
            print("Saliendo del programa...")
            return
        else:
            print("Opción no válida.")
            mostrar_menu()

    if __name__ == "__main__":
        mostrar_menu()
        print("=================================================")
        opcion = input("Ingrese una opción: ")
        print("=================================================")
        ejecutar_funcionalidad(opcion)