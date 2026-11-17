

# Ahora vamos a desarrollar un listado que emplen funciones, asi como caracteristicas especiles, 
# Estas pueden ser dadas por el usuario, asi como identificasion de una lista y otra


def crear_lista(numero):
    """Pide al usuario la longuitud y los elementos de una lista"""
    while True:
        try:
            longitud = int(input(f"¿cuantos nombres tendra la lista {numero}? "))
            if longitud > 0:
                break
            print("ingrese un numero mayor a 0")
        except ValueError:
            print("ingrese un numero entero valido")
            
    lista = []
    for i in range(longitud):
        nombre = input(f"Nombre {i + 1} de la lista {numero}: ").strip()
        lista.append(nombre)
    return lista

def eliminar_duplicados(lista1, lista2):
    """Devuelve lista1 sin los nombres que tambien esten en la lista2."""
    return [n for n in lista1 if n not in lista2]

lista1 = crear_lista(1)
lista2 = crear_lista(2)

print("\n---Listas originales---")
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

lista1_filtrada = eliminar_duplicados(lista1, lista2)

print("\n---Lista 1 despues de eliminar los nombres que estan en la lista 2---")
print(f"Lista 1 filtrada: {lista1_filtrada}")


