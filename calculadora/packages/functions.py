
def sumar(x:float,y:float)->float:
    """Suma dos valores

    Args:
        x (float): primer valor
        y (float): segundo valor

    Returns:
        float: devuelve la suma
    """
    return x+y

def resta(x:float,y:float)->float:
    """resta dos valores

    Args:
        x (float): primer valor
        y (float): segundo valor

    Returns:
        float: devuelve la resta
    """
    return x-y

def multiplicacion(x:float,y:float)->float:
    """multiplica dos valores

    Args:
        x (float): primer valor
        y (float): segundo valor

    Returns:
        float: devuelve la multiplica
    """
    return x*y

def dividir(x:float,y:float)->float:
    """divide dos valores

    Args:
        x (float): primer valor
        y (float): segundo valor, debe ser diferente de 0

    Rises:
        ZeroDivisionError cuando el valor 'y' es 0

    Returns:
        float: devuelve la suma
    
    """
    if y == 0:
        raise ZeroDivisionError("La division por 0 no esta definida")
    return x/y

def factorial(x:int)->int:
    """factorial

    Args:
        x (int): devuelve el factorial de un entero natural

    Raises:
        ValueError: ValueError para los numeros enteros negativos

    Returns:
        int: Devuelve el factorial pedido
    """
    if x >= 0:
        if x == 0 or x == 1:
            return 1
        else:
            return x * factorial(x-1)
    
    raise ValueError("El factorial es solo para numeros naturales")











