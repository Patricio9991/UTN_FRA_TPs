from data_stark import *
from packages.funciones_stark import *
from packages.modulo_menu import *
from desafio_00 import *




#Construir un menu

seguir = True

while seguir:
    match elegir_menu_desafio():
        case 'a':
            match menu():
                case '1':
                    mostrar_nombre_heroe(nombre_heroes)
                case '2':
                    mostrar_nombre_altura(lista_nombre_altura)
                case '3':
                
                    print(f"El superheroe mas alto tiene una  altura de: {superheroe_mas_alto}")

                case '4':
                    print(f"El superheroe mas bajo tiene una  altura de: {superheroe_mas_bajo}")

                case '5':
                    print(f"La latura promedio de los superheroes es: {promedio_altura:.2f}")
                case '6':
                    mostrar_min_max(lista_nombre_altura,superheroe_mas_bajo,superheroe_mas_alto)
                case '7':
                    print(f"El superheroe mas pesado es {nombre_mas_pesado} pesa: {maximo_peso} y el menos pesado es {nombre_menos_pesado} y pesa: {minimo_peso}")
                case '8':
                    orden = input("(a) Ascendente| (b) Descendente: ")
                    
                    while orden != 'a' and orden != 'b':
                        print("Ingrese un caracter valido")
                        orden = input("(a) Ascendente| (b) Descendente: ")

                    orden =  False if orden == 'b' else True
                    submenu()
                    
                    campo = input("Seleccione un campo: ")

                    if orden:
                        ordenar_heroes(data_heroes_cast,campo)
                        mostrar_heroes(data_heroes_cast)
                    else:   
                        ordenar_heroes(data_heroes_cast,campo,orden)
                        mostrar_heroes(data_heroes_cast)


        case 'b':
            print("aca va el menu 01")
            pass
        case _:
            print("Opcion invalida")
     

    pause()

print("Fin app stak")











