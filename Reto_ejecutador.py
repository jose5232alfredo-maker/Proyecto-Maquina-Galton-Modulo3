# En este program avamos a agregar los comando o mejor dicho las intrucciones para ejecutar nuestra actividad
# De la lista en el reto semanal, ambos de la semana 11

import m_retosemanal as m

def main():
    listas = m.crear_listas()
    m.imprimir_listas(listas, "Listas originales:")
    
    filtradas = m.eliminar_en_posteriores(listas)
    m.imprimir_listas(
        filtradas,
        "listas tras la eliminacion de elemntos que se repetian posterirmente en las listas posteriores"
    )

if __name__=="__main__":
    main()
    
