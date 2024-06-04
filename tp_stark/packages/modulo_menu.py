import os
from os import system

def pause():
    system('pause')

def menu():
    os.system('cls')
    print("--Menu opciones Stark--")
    print("1-Mostrar nombre de cada superheroe")
    print("2-Mostrar nombre y altura de cada superheroe")
    print("3-Ver altura maxima")
    print("4-Ver altura minima")
    print("5-Ver altura promedio")
    print("6-Mostrar nombre del superheroe mas alto y mas bajo")
    print("7-Ver superheroe mas y menos pesado")
    print("8-Ordenar la informacion")
    print("")
    print("9-Salir")

    opcion = input("Ingrese una opcion: ")

    return opcion

def submenu():
    system('cls')
   
    print("n-Ordenar por nombre")
    print("i-Identidad")
    print("e-Empresa")
    print("a-Altura")
    print("p-Peso")
    print("g-genero")
    print("co-color de ojos")
    print("cp-color de pelo")
    print("f-fuerza")
    print("int-inteligencia")


    
