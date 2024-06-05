from data_stark import *
from packages.funciones_stark import *


data_heroes = castear_heroe(lista_personajes)
#A Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

heroes_m = filtrar_genero_m_f(data_heroes)

mostrar_heroes(heroes_m)
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

heroes_f = filtrar_genero_m_f(data_heroes,'F')
mostrar_heroes(heroes_f)