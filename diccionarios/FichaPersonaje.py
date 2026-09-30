# 📝 COPIA ESTE DICCIONARIO INICIAL EN TU EDITOR:
personaje_reto = {
    "nombre": "Ragnar",
    "clase": "Guerrero",
    "vida": 150,
    "habilidades": ["Golpe Heroico", "Torbellino"],
    "oro": 50
}

# === TU MISIÓN ===
# 1. El guerrero visita al maestro de armas y aprende una nueva habilidad: "Grito de Guerra".
#    Agrégala al final de su lista de habilidades usando .append().
personaje_reto["habilidades"].append("Grito de Guerra")
print("\n",personaje_reto["habilidades"][2])

# 2. Un monstruo lo ataca por sorpresa. Muestra en pantalla el segundo ataque 
#    de su lista de habilidades (índice 1) con el formato: "⚔️ Ragnar usa: [Habilidad]".
print(f"\n⚔️  {personaje_reto['nombre']} usa: {personaje_reto['habilidades'][1]}")
# 3. Imprime el diccionario completo modificado para verificar los cambios.
print("\n", personaje_reto)

# 📝 DICCIONARIO INICIAL:
carrito_compras = {
    "Laptop": 800,
    "Mouse": 25,
    "Monitor": 250,
    "Teclado": 45
}

# === MISIÓN ===
# 1. La tienda tiene un error de inflación. Usa un ciclo 'for' con el método .items() 
#    para recorrer el carrito de compras.
# 2. Dentro del ciclo, imprime un mensaje para cada producto que diga:
#    "El artículo [Nombre] cuesta $[Precio]".
for articulo, precio in carrito_compras.items():
    print(f"\nEl artículo {articulo} cuesta {precio}")

# 3. HACKER CHALLENGE (Opcional): El cliente intenta buscar si en su carrito 
#    tiene un artículo llamado "Tarjeta Gráfica". Usa el método .get() para buscarlo. 
#    Si no existe, muestra el mensaje: "❌ Tarjeta Gráfica no está en el carrito".
busqueda_articulo = carrito_compras.get("tarjeta grafica","❌ Tarjeta Gráfica no está en el carrito❌")
print("\n",busqueda_articulo)