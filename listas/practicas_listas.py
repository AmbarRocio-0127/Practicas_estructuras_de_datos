"""
Practica de Listas - Ejemplos
"""
x = [] #Lista vacia
y = [1,2,3,4,5,6] #Lista con valores numéricos iniciales
z = [1, "Hola", 20.5, False] #Lista mezclada con distintos tipos de datos
print(f"\n{x} \n\n{y} \n\n{z}")
"""
Metodos Para Las Listas
"""
lista1 = ["agua","jugo","vino"]
lista1.append("champaña") #append(): Agrega un elemento al final
print("\nLista 1:", lista1)

lista2 = [1,2,3,4]
lista2.extend([5,6,7]) #extend(): Agrega múltiples elementos de otro iterable
print("\nLista 2:", lista2)

lista3 = ["sandía", "uvas"]
lista3.insert(0,"Pera") #insert(): Inserta un elemento en una posición específica
print("\nLista 3: ", lista3)

lista1.remove("agua")
print("\nRemoviendo elementos: ",lista1) #remove(): Elimina por valor

articulos_tecnologicos = ["Laptop", "mouse", "teclado", "enclosure sata"]
articulo4 = articulos_tecnologicos.pop(3) #pop(): limina por índice y devuelve el elemento
print(f"\narticulo 4: {articulo4} \n\nTodos los articulos: {articulos_tecnologicos}")

lista2.clear() #Vacía la lista
print("\n",lista2)

print("\nposicion de la champaña en la lista: ",lista1.index("champaña")) #index(): Busca la posición de un elemento

counter = y.count(5)
print(f"\nlistas: {counter}") # count: Cuenta cuantas veces aparice un elemento repetido

lista_desordenada = [8,5,2,7,4,1,9,6,3]
lista_desordenada.sort()
print("\n",lista_desordenada) #sort: Ordena la lista

lista_desordenada.sort(reverse=True) #Ordena la lista de manera descendente
print("\n",lista_desordenada)

lista_desordenada.reverse() #otra forma adicional de ordenar
print("\n",lista_desordenada)

bebidas = lista1.copy() #copy: Crea una copia de los elementos de otra lista
print(f"\n{lista1} \n\n{bebidas}")