# En este nuevo proyecto vamos a realizar algo muy similar a la semana anterior, pero con ligeras modificasiones
# Esto quiere decir que emplearemos el uso de listas en un archivo y desde otro vamos a ejcutar las instricciones y extraer

def pedir_entero(mensaje, minimo=1):
    """pide un numero enetro al usuario, repitiendo hasta que sea valido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"debe ser un numero mayor a o igual a {minimo}.")
        except ValueError:
            print("entrada no valida. Escribe un numero entero.")
            
def crear_listas():
    """Crea una lista de listas; el usuario define cuantas y su longuitud:"""
    cantidad = pedir_entero(f"¿cuantas listas desea crear?")
    listas = []
    for i in range(1, cantidad + 1):
        longitud = pedir_entero(f"longitud de la lista {i}:", minimo=1)
        lista = []
        for j in range(1, longitud +1):
            lista.append(pedir_entero(f"lista {i}, elemento {j}:", minimo=-10**9))
        listas.append(lista)
    return listas

def imprimir_listas(listas, mensaje):
    """imprime todas las listas presendidas de un mensaje"""
    print(f"\n---{mensaje}---")
    for i, lista in enumerate(listas, start=1):
        print(f"Lista {i}: {lista}")
        
def eliminar_en_posteriores(listas):
    """Devuelve nuevas listas sin los elementos que aparecen en listas posteriores.
    no modificar las listas originales."""
    resultado = []
    for i, lista in enumerate(listas):
        posteriores = set()
        for otra in listas[i +1:]:
            posteriores.update(otra)
        resultado.append([x for x in lista if x not in posteriores])
    return resultado

