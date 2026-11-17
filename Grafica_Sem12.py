# En esta ultima semana 12 vamos a realizar un proyecto muy ineteresante la verdad uno que me genera curiosidad por el echo de incluir graficos.
# Agregaremos datos de años de ventas de determinado año a uno mas adelante subiendo datos de vente de cada uno.

import matplotlib.pyplot as plt

año_inicial = int(input("Año inicial:"))
año_final = int(input("Año final:"))

años = list(range(año_inicial, año_final + 1))
ventas = []

for año in años:
    venta = float(input(f"Ventas en {año}:"))
    ventas.append(venta)    

plt.plot(años, ventas, marker='o')
plt.title("Ventas por año")
plt.xlabel("Año")
plt.ylabel("Ventas")
plt.xticks(años)
plt.grid(True)
plt.show()

