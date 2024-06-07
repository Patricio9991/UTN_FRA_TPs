from data_stark import *
from packages.funciones_stark import *


data_heroes = castear_heroe(lista_personajes)
#A Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

heroes_m = filtrar_lista(lambda a:  a["genero"] == 'M'  ,data_heroes)

#mostrar_heroes(heroes_m)
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

heroes_f = filtrar_lista(lambda a:  a["genero"] == 'F'  ,data_heroes)
#mostrar_heroes(heroes_f)

#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

lista_alturas_m = mapear_lista(lambda heroe: heroe["altura"],heroes_m)

altura_m_max = reduce_list(lambda ant,act: ant if ant>act else act ,lista_alturas_m)

#print(altura_m_max)

#D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

lista_alturas_f = mapear_lista(lambda heroe: heroe["altura"],heroes_f)
#print(lista_alturas_f)

altura_f_max = reduce_list(lambda ant,act: ant if ant>act else act,lista_alturas_f)

#print(altura_f_max)

#E Recorrer la lista y determinar cuál es el superhéroe más bajo de género M

altura_m_min =  reduce_list(lambda ant,act : ant if ant<act else act,lista_alturas_m)

#print(altura_m_min)

#E Recorrer la lista y determinar cuál es el superhéroe más bajo de género F

altura_f_min =  reduce_list(lambda ant,act : ant if ant<act else act,lista_alturas_f)

#G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M

suma_alturas_m = reduce_list(lambda ant,act : ant+act,lista_alturas_m)
promedio_altura_m = suma_alturas_m / len(lista_alturas_m)

# try:
#     mostrar_float(promedio_altura_m)
# except ValueError as e:
#     print(e)

#H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F

suma_alturas_f = reduce_list(lambda ant,act : ant+act,lista_alturas_f)
promedio_altura_f = suma_alturas_f / len(lista_alturas_f)
# try:
#     mostrar_float(promedio_altura_f)
# except ValueError as e:
#     print(e)

#I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)

nombre_altura_max_m = filtrar_lista(lambda a: a["altura"] == altura_m_max,heroes_m)
nombre_altura_max_f = filtrar_lista(lambda a: a["altura"] == altura_f_max,heroes_f)

nombre_altura_min_m = filtrar_lista(lambda a : a["altura"] == altura_m_min ,heroes_m)
nombre_altura_min_f = filtrar_lista(lambda a : a["altura"] == altura_f_min ,heroes_f)

# print(nombre_altura_min_m)
# print(nombre_altura_min_f)


# print("Heroes con mayor altura M F : ")
# mostrar_valores_asociados_dict(nombre_altura_max_m,"nombre",altura_m_max)
# mostrar_valores_asociados_dict(nombre_altura_max_f,"nombre",altura_f_max)

# print("Heroes con menor altura M F : ")
# mostrar_valores_asociados_dict(nombre_altura_min_m,"nombre",altura_m_min)
# mostrar_valores_asociados_dict(nombre_altura_min_f,"nombre",altura_f_min)


#D Determinar cuántos superhéroes tienen cada tipo de color de ojos.

# colores_ojos = list(set(mapear_lista(lambda a: a["color_ojos"],data_heroes)))

# mostrar_campo_buscado(colores_ojos,data_heroes,"color_ojos")

# # K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

# colores_de_pelo = list(set(mapear_lista(lambda a: a["color_pelo"],data_heroes)))

# mostrar_campo_buscado(colores_de_pelo,data_heroes,"color_pelo")


# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).


for_each_lista(lambda a:  a["inteligencia"] if len(a["inteligencia"]) != 0 else a.update({"inteligencia":"no tiene"}),data_heroes)

inteligencia_heroes = list(set(mapear_lista(lambda a: a["inteligencia"], data_heroes)))

# mostrar_campo_buscado(inteligencia_heroes,data_heroes,"inteligencia")

# M Listar todos los superhéroes agrupados por color de ojos.

# ordenar_heroes(data_heroes,"co")

# mostrar_heroes(data_heroes)

# # N Listar todos los superhéroes agrupados por color de pelo

# ordenar_heroes(data_heroes,"cp")

# mostrar_heroes(data_heroes)

# O Listar todos los superhéroes agrupados por tipo de inteligencia

# ordenar_heroes(data_heroes,"int")

# mostrar_heroes(data_heroes)
