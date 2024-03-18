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

Para ordenar alfabéticamente una lista de nombres, un buen método de ordenamiento es el algoritmo de ordenamiento Quick Sort. Aquí están las razones por las que Quick Sort podría ser considerado el mejor para este propósito:

Eficiencia en promedio: Quick Sort tiene un rendimiento muy bueno en promedio y es eficiente para listas grandes. En el caso promedio, tiene una complejidad de tiempo de O(n log n), lo que lo hace adecuado para ordenar listas de nombres.

Eficiente para datos casi ordenados: Si los nombres ya están casi en orden alfabético, Quick Sort tiende a funcionar muy bien, lo que puede ser común en listas de nombres.

Menor uso de memoria: Quick Sort es un algoritmo in-place, lo que significa que no requiere una cantidad significativa de memoria adicional para ordenar la lista. Esto puede ser ventajoso cuando se trabaja con grandes conjuntos de datos.

Implementación simple y compacta: La implementación de Quick Sort puede ser relativamente simple y fácil de entender, lo que facilita su mantenimiento y comprensión."""
