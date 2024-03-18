#Listar los personajes ordenados alfabeticamente de manera ascendente

personajes =["Anakin Skywalker", "Luke Skywalker", "Leia Organa", "Obi-Wan Kenobi", "Han Solo", "Chewbacca", "Darth Vader", "Darth Maul", "Yoda", "Jaba the Hutt", "Boba Fett","R2D2", "C3PO", "Padme Amidala", "Darth Sidious"]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

personajes = ["Anakin Skywalker", "Luke Skywalker", "Leia Organa", "Obi-Wan Kenobi", "Han Solo", "Chewbacca", "Darth Vader", "Darth Maul", "Yoda", "Jaba the Hutt", "Boba Fett", "R2D2", "C3PO", "Padme Amidala", "Darth Sidious"]

sorted_personajes = quick_sort(personajes)
print(sorted_personajes)

"""

Se implementa Quick Sort ya que es eficiente para listas grandes y utiliza menos memoria.
El algoritmo de Quick Sort es un algoritmo de ordenamiento que utiliza la técnica de divide y vencerás para ordenar listas.
El algoritmo funciona de la siguiente manera:
1. Se elige un elemento de la lista al que llamaremos pivote.
2. Se reorganiza la lista de manera que todos los elementos con valores menores al pivote queden a su izquierda y los mayores a su derecha.
3. Los elementos de la lista son ordenados de manera independiente en cada lado del pivote.
4. Finalmente, la lista queda ordenada.
"""