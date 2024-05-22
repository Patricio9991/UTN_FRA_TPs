from os import system

def pause():
    system('pause')

def menu(x = 'x', y = 'y'): #valor por defecto x = 'x'
    system('cls')
    print("Menu opciones calculadora \n Seleccione una opcion: ")
    print(f"a-Ingresar primer valor (A = {x})")
    print(f"b-Ingresar segundo valor (B = {y})")
    print("c-Seleccionar operacion")
    print("d-Salir")

    opcion = input("ingrese una opcion: ")
    
    return opcion

def submenu(primer_valor,segundo_valor):
    system('cls')
    print(f"(A = {primer_valor} | B = {segundo_valor})")
    print("a-Sumar")
    print("b-Restar")
    print("c-Dividir")
    print("d-Multiplicar")
    print("f-Factoreal de A")
    print("g-Factoreal de B")

    operacion = input("Seleccione operacion: ")

    return operacion
    






