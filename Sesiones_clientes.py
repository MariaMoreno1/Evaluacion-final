print("Nombre del estudiante: María de los Ángeles Moreno Franco")
print("Grupo: 213022_800")
print("Programa: Ingeniería de sistemas")
print()

sesiones = [
    [203, 156, 13],
    [324, 214, 21],
    [152, 123, 7],
    [205, 345, 24],
    [234, 22, 2],
    [304, 183, 16]

]

def clasificar_sesiones(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    
    elif duracion < 60 and clics < 3:
        return "Bajo"
    
    else:
        return "Medio"
    
print("Matriz de las sesiones de los clientes")
print(sesiones)
print()

print("Informe final de la clasificación de las sesiones: ")
print()

for sesion in sesiones:
    ID_cliente = sesion[0]
    Duracion = sesion[1]
    Clics = sesion[2]

    clasificacion = clasificar_sesiones(Duracion, Clics)
    print(f"Cliente {ID_cliente}: {clasificacion}")

    

