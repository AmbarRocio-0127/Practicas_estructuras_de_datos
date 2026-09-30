"""Crear un diccionario vacio"""
datos1 = {}
datos2 = dict()

"""Ejemplo asignando valores"""
datos1["nombre"] = "Andrea"
datos1["edad"] = 30
print("\n",datos1)

#Sintaxis Fundamental: diccionario[clave] = valor
persona = {
    "nombre": "Paula",
    "edad": 28,
    "pais": "RD"
}
telefono = persona.get("telefono")
print(telefono) #KeyError

"""Agregando y modificando valores"""
persona["edad"] = 26
print("\n",persona)
"""Si "edad" no existe, se agrega. Si "edad" ya existe, se modifica."""

"""Eliminando Valores"""
del persona["pais"] #si se elimina una clave que no existe se genera un KeyError

"""Midiendo los valores que este tiene"""
print("\n",len(persona))

"""Comprobar si existe una clave"""
print("\nnombre" in persona) #Devuelve True
print("\nnombre" in persona) #Devuelve False

"""Ejemplo en validaciones"""
if "edad" in persona:
    print("\nLa edad existe")
    
"""keys() obtiene las llaves"""
print("\n",persona.keys())

"""values() permite obtener los valores"""
print("\n",persona.values())

"""Tambien se pueden convertir en lista (al extraer los valores)"""
valores = list(persona.values())

"""Recorrer las los diccionarios de distintas formas"""
for elemento in persona: #Aqui python recorre las claves
    print(elemento)
    
for clave in persona.keys():#aqui recorre las claves explicitamente
    print(clave)
    
for valor in persona.values():#aqui recorre los valores explicitamente
    print(valor)
    
for clave, valor in persona.items():
    print(clave, valor)#aqui recorre clave y valor simultaneamente
    
for clave, valor in persona.items():#igual que la anterior pero mas legible
    print(f"{clave}: {valor}")

"""Ejemplo con valores iniciales"""
traductor = {
    'amarillo':'yellow',
    'rojo':'red',
    'verde':'green',
    'negro':'black',
    'marron':'brown'
}
print("\n",traductor)
print("\n",len(traductor))

