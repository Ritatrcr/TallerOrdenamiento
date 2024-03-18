# Determinar si el personaje "Darth Maul" se encuentra en la lista de personajes. 
#Si se encuentra, imprimir su posición en la lista. Si no se encuentra, imprimir un mensaje que lo indique.
personajes = ["Anakin Skywalker", "Luke Skywalker", "Leia Organa", "Obi-Wan Kenobi", "Han Solo", "Chewbacca", "Darth Vader", "Darth Maul", "Yoda", 
              "Jaba the Hutt", "Boba Fett", "R2D2", "C3PO", "Padme Amidala", "Darth Sidious"]

def centinela(lista, valor):
    posicion = -1  
    i = 0
    while i < len(lista) and posicion == -1:
        if lista[i].upper() == valor:
            posicion = i
        i += 1
    return posicion

# Verificamos si el personaje se encontró antes de imprimir su posición
posicion = centinela(personajes, "DARTH MAUL")
if posicion != -1:
    print("El personaje Darth Maul se encuentra en la posición", posicion + 1)
else:
    print("El personaje Darth Maul no se encuentra en la lista.")


"""
El punto de usar el algoritmo de búsqueda con centinela (centinela) es buscar eficientemente un elemento en una lista sin necesidad de revisar todos los elementos.
Funciona deteniendo la búsqueda tan pronto como se encuentra el elemento deseado, lo que reduce el número de comparaciones necesarias.
En este caso, se utiliza para encontrar la posición de un personaje en una lista de nombres. 
Si el personaje se encuentra en la lista, la función devuelve su posición; de lo contrario, devuelve -1.
Se comparan en mayúsculas para evitar errores y asegurar que la comparación sea insensible a mayúsculas y minúsculas. 

"""
