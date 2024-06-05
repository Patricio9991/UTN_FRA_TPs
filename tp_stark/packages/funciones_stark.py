

def mostrar_un_heroe(un_heroe):

    print(f"{un_heroe["nombre"]:<22}  {un_heroe["identidad"]:<30}   {un_heroe["empresa"]}   {un_heroe["altura"]:6.2f}    {un_heroe["peso"]:6.2f}  {un_heroe["genero"]:<2}      {un_heroe["color_ojos"]:<10}  {un_heroe["color_pelo"]:<20}  {un_heroe["fuerza"]:<6} {un_heroe["inteligencia"]:<10}")

def mostrar_heroes(lista_dict)->None:
    print("                                *****LISTA HEROES******")
    print("nombre                    identidad                       empresa        altura   peso   genero   color_ojos     color_pelo        Fuerza     inteligencia")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(len(lista_dict)):
        mostrar_un_heroe(lista_dict[i])

def valirdar_lista(lista:list)->bool:
    """Valida que se ingrese una lista (aunque este vacia)

    Args:
        lista (list): parametro donde se ingresa la lista

    Raises:
        ValueError: error en caso de que no sea una lista valida

    """

    if not isinstance(lista,list):
        raise ValueError("No se ingreso un dato valido")


def mapear_columna(lista:list,campo:str)->list:
    """Devuelve una lista que contiene la informacion de un campo de un diccionario

    Args:
        lista (list): lista de diccionarios
        campo (str): campo para extraer informacion

    Returns:
        list: columna de la informacion
    """
    valirdar_lista(lista)
    lista_retorno = []
    
    for i in range(len(lista)):
        
        lista_retorno.append(lista[i][campo])

    return lista_retorno

def mapear_lista(proceso,lista:list)->list:
    """mapea una lista segun un determinado criterio

    Args:
        proceso (funcion): funcion criterio
        lista (list): lista para mapear

    Returns:
        list: lista mapeada segun la funcion proceso
    """
    valirdar_lista(lista)
    lista_retorno = []

    for item in lista:
        lista_retorno.append(proceso(item))

    return lista_retorno

def filtrar_lista(filtradora:bool,list:list): #filtrar
    """filtra lista segun criterio

    Args:
        filtradora (bool): devuelve True o False
        list (list): lista a filtrar

    Returns:
        list: lista con appends de los resultados True de la filtradora
    """
    valirdar_lista(list)
    lista_filtrada = []
    for i in range(len(list)):
        if filtradora(list[i]):
            lista_filtrada.append(list[i])

    return lista_filtrada

def swap_items(lista,i,j):
    aux = lista[i]
       
    lista[i] = lista[j] 
    
    lista[j]  = aux

def buscar_maximo_or_minimo(lista,maximo = True):

    valirdar_lista(lista)
    valor_max_or_min = 0
    flag_max_min = True

    for i in range(len(lista)):
        if maximo:
            if flag_max_min or lista[i] > max_or_min:
                flag_max_min = False
                max_or_min = lista[i]
                
        else:
                if flag_max_min or lista[i] < max_or_min:
                    flag_max_min = False
                    max_or_min = lista[i]
                    
            

    return max_or_min
 


def definir_campo(campo):
    if not isinstance(campo,str):
        raise ValueError("Se esperaba un string")
    
    retorno = " "

    match campo:
        case 'n':
            retorno = "nombre"
        case 'i':
            retorno = "identidad"
        case 'e':
            retorno = "empresa"
        case 'a':
            retorno = "altura"
        case 'p':
            retorno = "peso"
        case 'g':
            retorno = "genero"
        case 'co':
            retorno = "color_ojos"
        case 'cp':
            retorno = "color_pelo"
        case 'f':
            retorno = "fuerza"
        case 'int':
            retorno = "inteligencia"
        case _:
            raise ValueError("No se ingreso un campo")

    return retorno

def swap_items(lista,i,j)->None:
    """Hace un swap de elementos de una lista

    Args:
        lista (_type_): lista
        i (_type_): elemento en indice i
        j (_type_): elemento en indice j
    """
    aux = lista[i]
       
    lista[i] = lista[j] 
    
    lista[j]  = aux

def ordenar_heroes(list:list,campo:str = 'n',asc:bool = True)->None:
    """Ordena una lista segun criterios requeridos

    Args:
        list (_type_): una lista valida
        campo (str, optional): default n: ordena por nombre
        asc (bool, optional): Defaults to True: ascendente | False: descendente.
    """
    valirdar_lista(list)
    campo_ordenamiento = definir_campo(campo)
    tam = len(list)


    for i in range(tam - 1):
        for j in range(i+1, tam):
            if list[i][campo_ordenamiento] > list[j][campo_ordenamiento] if asc else list[i][campo_ordenamiento] <list[j][campo_ordenamiento]:
                swap_items(list,i,j)


def new_superheroe(nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia):
    """crea un diccionario con la informacion pasada por parametros

    Returns:
        retorna el diccionario
    """
    nuevo_superheroe = {}
    nuevo_superheroe["nombre"] = nombre
    nuevo_superheroe["identidad"] = identidad
    nuevo_superheroe["empresa"] = empresa
    nuevo_superheroe["altura"] = altura
    nuevo_superheroe["peso"] = peso
    nuevo_superheroe["genero"] = genero
    nuevo_superheroe["color_ojos"] = color_ojos
    nuevo_superheroe["color_pelo"] = color_pelo
    nuevo_superheroe["fuerza"] = fuerza
    nuevo_superheroe["inteligencia"] = inteligencia

    


    return nuevo_superheroe


def castear_heroe(lista):
    valirdar_lista(lista)
    heroes_retorno = []
    for i in range(len(lista)):
        nombre = lista[i]["nombre"]
        identidad = lista[i]["identidad"]
        empresa =lista[i]["empresa"] 
        altura = float(lista[i]["altura"])
        peso = float(lista[i]["peso"])
        genero = lista[i]["genero"] 
        color_ojos = lista[i]["color_ojos"]
        color_pelo = lista[i]["color_pelo"] 
        fuerza = float(lista[i]["fuerza"])
        inteligencia = lista[i]["inteligencia"] 
        heroes_retorno.append(new_superheroe(nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia))
    return heroes_retorno


def mostrar_nombre_heroe(lista:list):
    print("     Nombre de heroes")
    for item in lista:
        print(item)

def mostrar_nombre_altura(lista):
    print("Nombre                        Altura")
    for i in range(len(lista)):
        print(f"{lista[i][0]:<30}{lista[i][1]:<0.5}")

def mostrar_min_max(lista:list[list],min:int,max:int):
    """recorre una lista con elementos de la forma [nombre,altura] e informa maximo y minimo con nombre

    Args:
        lista (): lsita que contiene listas de dos elementos
        min (int): valor minimo de compracion
        max (int): valor maximo de comparacion
    """
    for i in range(len(lista)):
        if lista[i][1] == max:
            print(f"El superheroe mas alto es {lista[i][0]},con {max}") 
    
        if lista[i][1] == min:
            print(f"El superheroe mas bajo es {lista[i][0]},con {min} ") 
   

def filtrar_genero_m_f(lista:list[dict],genero:str = 'M'):
    lista_filtro_aplicado = []   
    match genero:
        case 'M':
            lista_filtro_aplicado = filtrar_lista(lambda a:  a["genero"] == genero  ,lista)
        case 'F':
            lista_filtro_aplicado = filtrar_lista(lambda a:  a["genero"] == genero  ,lista)
        case _:
            raise ValueError("Argumentos invalidos")
    return lista_filtro_aplicado
