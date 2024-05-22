from packages.functions import * 
from packages.menu_modulos import *

flag_num1 = False
flag_num2 = False

num1 = 'x'
num2 = 'y'

while True:
    try:
        match menu(num1,num2):
            case 'a':
                num1 = int(input("Ingrese el primer valor: "))
                flag_num1 = True
                
                
            case 'b':
                if flag_num1:
                    num2 = int(input("Ingrese el segundo numero: "))
                    flag_num2 = True
                    
            case 'c':
                if flag_num1 and flag_num2 :
                    match(submenu(num1,num2)):
                        case 'a': 
                            resultado = sumar(num1,num2)  
                            print(f"La suma es {resultado}")
                        case 'b':
                            resultado = resta(num1,num2)
                            print(f"La resta es {resultado}")
                        case 'c':
                            try:
                                resultado = dividir(num1,num2)
                                print(f"La division es {resultado}")
                            except ZeroDivisionError as e:
                                print(e)
                        case 'd':
                            resultado = multiplicacion(num1,num2)
                            print(f"La multiplicacion es {resultado}")
                        case 'f':
                            try:
                                resultado = factorial(num1)
                                print(f"El factorial es {resultado}")
                            except ValueError as e:
                                print(e)
                        case 'g':
                            try:
                                resultado = factorial(num2)
                                print(f"El factorial es {resultado}")
                            except ValueError as e:
                                print(e)
                else:
                    print("Necesito valores para operar")
            case 'd':
                break

    except ValueError:
        print("Debe ingresar numeros dentro de cada opcion")


    pause()
    
print("Fin del programa")
