#Listar todos los personajes que empiecen con la letra "L"
personajes =["Anakin Skywalker", "Luke Skywalker", "Leia Organa", "Obi-Wan Kenobi", "Han Solo", "Chewbacca", "Darth Vader", "Darth Maul", "Yoda", "Jaba the Hutt", "Boba Fett","R2D2", "C3PO", "Padme Amidala", "Darth Sidious"]

def personajes_con_letra(lista, letra):
    personajes_con_letra = [personaje for personaje in lista if personaje[0].upper() == letra]
    return personajes_con_letra

personajes_con_L = personajes_con_letra(personajes, "L")
print("Personajes que empiezan con letra L", personajes_con_L)


"""
Para listar todos los personajes que empiecen con la letra "L" en una lista de nombres, no es necesario un algoritmo de ordenamiento como Quick Sort. 
Se puede simplemente iterar sobre la lista y verificar cada nombre para determinar si comienza con la letra "L"
"""

