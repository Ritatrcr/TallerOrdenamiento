#utilizar los métodos de ordenamiento y búsqueda más eficiente de acuerdo al tipo de dato.

#Punto A: Listar los personajes ordenados alfabeticamente de manera ascendente
"""El método de ordenamiento más eficiente para la lista de nombres de personajes es Quick Sort, 
ya que es eficiente para listas grandes y puede ordenarlas alfabéticamente en O(n log n)."""

#Punto B: Determinar si el personaje Darth Maul está cargado y en que posicion se encuentra
"""
El punto de usar el algoritmo de búsqueda con centinela (centinela) es buscar eficientemente un elemento en una lista sin necesidad de revisar todos los elementos.
Funciona deteniendo la búsqueda tan pronto como se encuentra el elemento deseado, lo que reduce el número de comparaciones necesarias.
En este caso, se utiliza para encontrar la posición de un personaje en una lista de nombres. 
Si el personaje se encuentra en la lista, la función devuelve su posición; de lo contrario, devuelve -1.
Se comparan en mayúsculas para evitar errores y asegurar que la comparación sea insensible a mayúsculas y minúsculas. 
"""


#Punto c  mostrar la información de los personajes antes y después del personaje "Yoda" en la lista `personajes`. 
'''Primero, define una lista de personajes llamada `personajes` y una función llamada `centinela` que busca un valor específico en la lista y 
devuelve su índice. Luego, se utiliza esta función para encontrar la posición de "Yoda" en la lista de personajes.
Para mostrar los personajes antes de "Yoda", se recorre la lista desde el principio hasta la posición de "Yoda" utilizando un bucle `for`. 
Después, se imprime la posición de "Yoda". Finalmente, para mostrar los personajes después de "Yoda", se recorre la 
lista desde la posición siguiente a "Yoda" hasta el final de la lista utilizando otro bucle `for`.
Se utilizaron diferentes métodos de búsqueda en este código debido a la necesidad de encontrar la posición de un valor específico en una lista. 
La función `centinela` implementa un enfoque de búsqueda lineal, que recorre la lista elemento por elemento hasta que encuentra el valor deseado o 
llega al final de la lista. Este enfoque es simple y adecuado para listas pequeñas como la proporcionada en este caso. Sin embargo, 
para listas más grandes o en aplicaciones donde la eficiencia es crítica, podrían utilizarse otros métodos de búsqueda más eficientes, 
como la búsqueda binaria en listas ordenadas. En este caso, dado que la lista no está ordenada y es relativamente pequeña, 
el enfoque de búsqueda lineal es apropiado y sencillo de implementar.
'''

#Punto D: #Listar todos los personajes que empiecen con la letra "L"
"""
El código utiliza una función personajes_con_letra para listar todos los personajes que comienzan con una letra específica. 
En este caso, se listan los personajes que comienzan con la letra "L". 
Esto se logra utilizando una comprensión de lista para filtrar los personajes que tienen la letra inicial deseada"""
