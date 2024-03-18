#Mostrar la informacion de los personajes antes y despues de YODA

personajes =["Anakin Skywalker", "Luke Skywalker", "Leia Organa", "Obi-Wan Kenobi", "Han Solo", "Chewbacca", "Darth Vader", "Darth Maul"
             , "Yoda", 
             "Jaba the Hutt", "Boba Fett","R2D2", "C3PO", "Padme Amidala", "Darth Sidious"]

#Funcion def centinela que recibe una lista y una valor de tipo str y devuelve el indice de ese personaje si se encuentra en la lista y si no retorna -1
def centinela(lista, valor):
    posicion = -1  
    i = 0
    while i < len(lista) and posicion == -1:
        if lista[i] == valor:
            posicion = i
        i += 1
    return posicion

#Uso de la funcion def centinela para encontrar un personaje especifico en la lista
posicion_yoda = centinela(personajes,"Yoda")


print("Imprimir personajes antes de yoda")
for i in range(posicion_yoda):
    print(personajes[i])

print("La posicion de Yoda es: " , posicion_yoda)

print("Imprimir personajes despues de yoda")
for i in range(posicion_yoda + 1, len(personajes)):
    print(personajes[i])

