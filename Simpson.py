#Lista Simpson
lista=["bola de nive", "Bart","Lisa","Homero","Marge","Krusty","Rodd","Todd","Ned Flaters", "Moe","Barnie", 
       " Skinew", "Milkhouse", "Nelsay", "Rafa"]

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

def ordena_forma_ascendente(arr):
    return quick_sort(arr)

def ordena_forma_descendente(arr):
    return quick_sort(arr)[::-1]

#def ordenar_desde_personaje_con_letra(arr, letra):

def personaje_pedido_por_consola(arr, nombre):
    if nombre in arr:
        return nombre
    else:
        return "No se encuentra el personaje"

def personaje_por_medio_de_indice(arr, indice):
    if indice < len(arr):
        return arr[indice]
    else:
        return "No se encuentra el personaje"

def innit():
    opcion = menu()
    while opcion != 6:
        if opcion == 1:
            print(ordena_forma_ascendente(lista))
        elif opcion == 2:
            print(ordena_forma_descendente(lista))
        elif opcion == 3:
            letra = input("Digite la letra por la que desea ordenar: ")
            #que hace??
        elif opcion == 4:
            nombre = input("Digite el nombre del personaje que desea buscar: ")
            print(personaje_pedido_por_consola(lista, nombre))
        elif opcion == 5:
            indice = int(input("Digite el indice del personaje que desea buscar: "))
            print(personaje_por_medio_de_indice(lista, indice))
        opcion = menu()
