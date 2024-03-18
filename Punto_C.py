#Mostrar la informacion de los personajes antes y despues de YODA

personajes =["Anakin Skywalker", "Luke Skywalker", "Leia Organa", "Obi-Wan Kenobi", "Han Solo", "Chewbacca", "Darth Vader", "Darth Maul"
             , "Yoda", 
             "Jaba the Hutt", "Boba Fett","R2D2", "C3PO", "Padme Amidala", "Darth Sidious"]

def centinela(lista, valor):
    posicion = -1  
    i = 0
    while i < len(lista) and posicion == -1:
        if lista[i] == valor:
            posicion = i
        i += 1
    return posicion

posicion_yoda = centinela(personajes,"Yoda")


print("Imprimir personajes antes de yoda")
for i in range(posicion_yoda):
    print(personajes[i])

print("La posicion de Yoda es: " , posicion_yoda)

print("Imprimir personajes despues de yoda")
for i in range(posicion_yoda + 1, len(personajes)):
    print(personajes[i])

