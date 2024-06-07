from data_stark import *
from packages.funciones_stark import *
from packages.modulo_menu import *
from desafio_00 import *
from desafio_01 import data_heroes




#Construir un menu

seguir = True

while seguir:
    match elegir_menu_desafio():
        case 'a':
            match menu_00():
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
                case '0':
                    break
                    


        case 'b':
            match menu_01():
                case '1':
                    heroes_m = filtrar_lista(lambda a:  a["genero"] == 'M'  ,data_heroes)
                    mostrar_heroes(heroes_m)
                case '2':
                    heroes_f = filtrar_lista(lambda a:  a["genero"] == 'F'  ,data_heroes)
                    mostrar_heroes(heroes_f)
                case '3':
                    lista_alturas_m = mapear_lista(lambda heroe: heroe["altura"],heroes_m)

                    altura_m_max = reduce_list(lambda ant,act: ant if ant>act else act ,lista_alturas_m)

                    print(altura_m_max)
                case '4':
                    lista_alturas_f = mapear_lista(lambda heroe: heroe["altura"],heroes_f)

                    altura_f_max = reduce_list(lambda ant,act: ant if ant>act else act,lista_alturas_f)

                    print(altura_f_max)
                case '5':
                    altura_m_min =  reduce_list(lambda ant,act : ant if ant<act else act,lista_alturas_m)

                    print(altura_m_min)
                case '6':
                    altura_f_min =  reduce_list(lambda ant,act : ant if ant<act else act,lista_alturas_f)
                    print(altura_f_min)
                case '7':
                    suma_alturas_m = reduce_list(lambda ant,act : ant+act,lista_alturas_m)
                    promedio_altura_m = suma_alturas_m / len(lista_alturas_m)

                    try:
                        mostrar_float(promedio_altura_m)
                    except ValueError as e:
                        print(e)
                case '8':
                    suma_alturas_f = reduce_list(lambda ant,act : ant+act,lista_alturas_f)
                    promedio_altura_f = suma_alturas_f / len(lista_alturas_f)
                    try:
                        mostrar_float(promedio_altura_f)
                    except ValueError as e:
                        print(e)
                case '9':
                    nombre_altura_max_m = filtrar_lista(lambda a: a["altura"] == altura_m_max,heroes_m)
                    nombre_altura_max_f = filtrar_lista(lambda a: a["altura"] == altura_f_max,heroes_f)

                    nombre_altura_min_m = filtrar_lista(lambda a : a["altura"] == altura_m_min ,heroes_m)
                    nombre_altura_min_f = filtrar_lista(lambda a : a["altura"] == altura_f_min ,heroes_f)

                    print("Heroes con mayor altura M F : ")
                    mostrar_valores_asociados_dict(nombre_altura_max_m,"nombre",altura_m_max)
                    mostrar_valores_asociados_dict(nombre_altura_max_f,"nombre",altura_f_max)

                    print("Heroes con menor altura M F : ")
                    mostrar_valores_asociados_dict(nombre_altura_min_m,"nombre",altura_m_min)
                    mostrar_valores_asociados_dict(nombre_altura_min_f,"nombre",altura_f_min)
                case '10':
                    colores_ojos = list(set(mapear_lista(lambda a: a["color_ojos"],data_heroes)))

                    mostrar_campo_buscado(colores_ojos,data_heroes,"color_ojos")
                case '11':
                    colores_de_pelo = list(set(mapear_lista(lambda a: a["color_pelo"],data_heroes)))

                    mostrar_campo_buscado(colores_de_pelo,data_heroes,"color_pelo")
                case '12':
                    for_each_lista(lambda a:  a["inteligencia"] if len(a["inteligencia"]) != 0 else a.update({"inteligencia":"no tiene"}),data_heroes)

                    inteligencia_heroes = list(set(mapear_lista(lambda a: a["inteligencia"], data_heroes)))

                    mostrar_campo_buscado(inteligencia_heroes,data_heroes,"inteligencia")
                case '13':
                    ordenar_heroes(data_heroes,"co")

                    mostrar_heroes(data_heroes)
                case '14':
                    ordenar_heroes(data_heroes,"cp")

                    mostrar_heroes(data_heroes)
                case '15':
                    ordenar_heroes(data_heroes,"int")

                    mostrar_heroes(data_heroes)
                case '0':
                    break
                case _:
                    print("Opcion invalida")
     
        case _:
            print("opcion invalida")
    pause()

print("Fin app stak")











