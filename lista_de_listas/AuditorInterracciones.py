""" Reto 1: El Auditor de Interacciones 
Contexto
Tienes la siguiente lista que representa las interacciones de tres publicaciones.

Cada sublista almacena la información en el siguiente orden:
Índice 0: Likes ❤️
Índice 1: Guardados 📌"""

""" Misión
1. Agregar una nueva publicación
Se ha publicado un nuevo post que obtuvo:

80 Likes
15 Guardados"""

interacciones = [
    [50,10],
    [1200, 300],
    [5,1]
]

#agregando nueva publicacion
interacciones.append([80,15])

#metodo para imprimir cada interaccion
def imprimir_interaccion():
        print(f"\n Likes ❤️: {interaccion[0]} \n Guardados 📌: {interaccion[1]}")

#recorriendo las interacciones
for interaccion in interacciones:
    if interaccion[0] > 1000:
        print("\n 🚀¡Post Viral!🚀")
        imprimir_interaccion()
    else:
        print("\n ⚖️ Post con rendimiento normal🍃")
        imprimir_interaccion()
