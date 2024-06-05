import os
from os import system

def pause():
    system('pause')

def elegir_menu_desafio():
    os.system('cls')
    print("TP STARK| Desafio #00 o #01")
    print("")
    print("a)Ver menu desafio #00")
    print("b)Ver menu desafio #01")

    desafio = input("Seleccione menu: ")




    return desafio


def menu():
    os.system('cls')
    print("--Menu opciones Stark--")
    print("-Desafio #00-")
    print("1-Mostrar nombre de cada superheroe")
    print("2-Mostrar nombre y altura de cada superheroe")
    print("3-Ver altura maxima")
    print("4-Ver altura minima")
    print("5-Ver altura promedio")
    print("6-Mostrar nombre del superheroe mas alto y mas bajo")
    print("7-Ver superheroe mas y menos pesado")
    print("8-Ordenar la informacion")
    print("")
    # print("-Desafio #01-")
    # print("A)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe degénero M")


    opcion = input("Ingrese una opcion: ")
    print("")

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


    
