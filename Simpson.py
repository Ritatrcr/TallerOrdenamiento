#Lista Simpson


#Crear Menu 
def menu(): 
    print("1. Ordenar de forma ascendente") 
    print("2. Ordenar de forma descendente")
    print("3. Ordenar desde personaje que inicie con letra ...")
    print("4. Personaje pedido por consola")
    print("5. Sacar personaje por medio de indice digitado en consola")
    print("6. Salir")
    return int(input("Digite la opcion que desea realizar: "))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    
    return quick_sort_desc(left) + middle + quick_sort_desc(right)

def quick_sort_letra(arr, letra):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[0] < letra]
    middle = [x for x in arr if x[0] == letra]
    right = [x for x in arr if x[0] > letra]
    
    return quick_sort_letra(left, letra) + middle + quick_sort_letra(right, letra)

