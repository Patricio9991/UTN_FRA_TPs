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


def menu_00():
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
    print("0-salir")
    print("")
    

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


def menu_01():

    os.system('cls')
    print("--Menu opciones Stark--")
    print("-Desafio #01-")
    print("1-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    print("2-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print("3-Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("4-Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("5-Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    print("6-Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    print("7-Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    print("8-Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    print("9-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 3 a 8)")
    print("10-Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("11-Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("12-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    print("13-listar todos los superhéroes agrupados por color de ojos.")
    print("14-listar todos los superhéroes agrupados por color de pelo.")
    print("15-Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("0-salir")



    opcion = input("Selecciona una opcion: ")

    return opcion
