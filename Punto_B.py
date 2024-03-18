# Determinar si el personaje "Darth Maul" se encuentra en la lista de personajes. 
#Si se encuentra, imprimir su posición en la lista. Si no se encuentra, imprimir un mensaje que lo indique.
personajes = ["Anakin Skywalker", "Luke Skywalker", "Leia Organa", "Obi-Wan Kenobi", "Han Solo", "Chewbacca", "Darth Vader", "Darth Maul", "Yoda", 
              "Jaba the Hutt", "Boba Fett", "R2D2", "C3PO", "Padme Amidala", "Darth Sidious"]

def centinela(lista, valor):
    posicion = -1  
    i = 0
    while i < len(lista) and posicion == -1:
        if lista[i] == valor:
            posicion = i
        i += 1
    return posicion

# Verificamos si el personaje se encontró antes de imprimir su posición
posicion = centinela(personajes, "Darth Maul")
if posicion != -1:
    print("El personaje Darth Maul se encuentra en la posición", posicion + 1)
else:
    print("El personaje Darth Maul no se encuentra en la lista.")
