# LLegamos al final del trayecto de este modulo y para eso vamos a finalizar con un proyecto bastente interesante, crearemos un programa de canicas llamado maquina de galton
# Interactuando con 3000 cannicas en primer plano sin animasio solo con un grafico de histograma para que quede simplificado
# A sido un camino interesante de verdad y muy divertido, espero llegara a mejores resultados con estas actividades
# Vamos a terminar de la mejor manera posible


import random
import matplotlib.pyplot as plt

def simular_canicas(num_canicas=3000, num_niveles=12):
    contenedores = [0] * (num_niveles + 1)
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(niveles):
            posicion += random.choice([0,1])
        contenedores[posicion] += 1
    return contenedores

def graficar_histograma(contenedores):
    plt.bar(range(len(contenedores)), contenedores)
    plt.xlabel('Contenedores')
    plt.ylabel('Número de canicas')
    plt.title('Distribución de canicas en la máquina de Galton')
    plt.xticks(range(len(contenedores)))
    plt.show()
    
if __name__ == "__main__":
    num_canicas = 3000
    niveles = 12
    contenedores = simular_canicas(num_canicas, niveles)
    graficar_histograma(contenedores)
    
