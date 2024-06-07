from data_stark import *
from packages.funciones_stark import *


#A Los datos de peso, altura e inteligencia hay que castearlos como float



#B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe

nombre_heroes = mapear_lista(lambda heroe: heroe["nombre"], lista_personajes)


#C Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

altura_heroes = mapear_lista(lambda heroe : float(heroe["altura"]),lista_personajes)


lista_nombre_altura = []
for i in range(len(lista_personajes)):
    lista_nombre_altura.append([nombre_heroes[i],altura_heroes[i]])

#print(lista_nombre_altura)

#D Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
superheroe_mas_alto = buscar_maximo_or_minimo(altura_heroes)


# try:
#     print(f"El superheroe mas alto tiene una  altura de: {superheroe_mas_alto}")
# except ValueError as e:
#     print(e)

#E Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

superheroe_mas_bajo = buscar_maximo_or_minimo(altura_heroes,False)



# try:
#     print(f"El superheroe mas bajo tiene una altura de: {superheroe_mas_bajo}")
# except ValueError as e:
#     print(e)

#F Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)

acumulador_altura = 0

for el in altura_heroes:
    acumulador_altura += altura_heroes[i]

promedio_altura = acumulador_altura / len(altura_heroes)

#print(f"La latura promedio de los superheroes es: {promedio_altura:.2f}")

#G Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)

# for i in range(len(lista_nombre_altura)):
#     if altura_heroes[i] == superheroe_mas_alto:
#         print(f"El superheroe mas alto es {nombre_heroes[i]},con {superheroe_mas_alto} ") 

#     if altura_heroes[i] == superheroe_mas_bajo:
#         print(f"El superheroe mas bajo es {nombre_heroes[i]},con {superheroe_mas_bajo} ") 
    


        

#H  Calcular e informar cual es el superhéroe más y menos pesado.

lista_peso_heroes = mapear_lista(lambda a: float(a["peso"]),lista_personajes)
print(lista_peso_heroes)


maximo_peso = buscar_maximo_or_minimo(lista_peso_heroes)
minimo_peso = buscar_maximo_or_minimo(lista_peso_heroes,False)
nombre_mas_pesado = ""
nombre_menos_pesado = ""

for i in range(len(lista_peso_heroes)):
    if lista_peso_heroes[i] == maximo_peso:
        nombre_mas_pesado = nombre_heroes[i]

    
    if lista_peso_heroes[i] == minimo_peso:
        nombre_menos_pesado = lista_personajes[i]["nombre"]




#I Ordenar el código implementando una función para cada uno de los valores informados.
data_heroes_cast = castear_heroe(lista_personajes)

#ordenar_heroes(data_heroes_cast,"p")