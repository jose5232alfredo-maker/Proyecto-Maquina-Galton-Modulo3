# En este proyecto en modulo 3, veremos diversas funciones en espesifico realizaremos un bucle infinito solicitando en espesifico una letra 
# Dando como resultado la letra anterior a esta y la siguiente



def obtener_letra_anterior_siguiente(letra):
    """
    Dada una letra, devuelve la letra anterior y la siguiente en el alfabeto.
    """
    if letra.islower():
        abecedario = "abcdefghijklmnopqrstuvwxyz"
    else:
        abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letra not in abecedario:
        return None, None  # Retorna None si la letra no es valida

    indice = abecedario.index(letra)
    letra_anterior = abecedario[indice - 1] if indice > 0 else None
    letra_siguiente = abecedario[indice + 1] if indice < len(abecedario) - 1 else None

    return letra_anterior, letra_siguiente

print("Bienvenido al programa de letras del abecedario")

while True:
    letra = input("Ingrese una letra del abecedario (o 'salir' para terminar): ").strip()
    
    if letra.lower() == 'salir':
        print("Saliendo del programa.")
        break

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingrese solo una letra válida.")
        continue

    anterior, siguiente = obtener_letra_anterior_siguiente(letra)
    
    if anterior is None and siguiente is None:
        print("La letra ingresada no es válida.")
    else:
        print(f"La letra anterior a '{letra}' es: '{anterior if anterior else 'no hay (es la primera letra del abecedario)'}'")
        print(f"La letra siguiente a '{letra}' es: '{siguiente if siguiente else 'no hay (es la última letra del abecedario)'}'")
print("Gracias por usar el programa de letras del abecedario.")


