import redis

# Conexión a la base de datos Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def agregar_palabra(palabra, significado):
    redis_client.hset("palabras", palabra, significado)
    print("Palabra agregada con éxito.")

def editar_palabra(palabra, nuevo_significado):
    if redis_client.hexists("palabras", palabra):
        redis_client.hset("palabras", palabra, nuevo_significado)
        print("Palabra editada con éxito.")
    else:
        print("Palabra no encontrada.")

def eliminar_palabra(palabra):
    if redis_client.hexists("palabras", palabra):
        redis_client.hdel("palabras", palabra)
        print("Palabra eliminada con éxito.")
    else:
        print("Palabra no encontrada.")

def buscar_palabra(palabra):
    significado = redis_client.hget("palabras", palabra)
    if significado is not None:
        return significado.decode('utf-8')
    else:
        return None

def mostrar_todas_las_palabras():
    palabras = redis_client.hgetall("palabras")
    for palabra, significado in palabras.items():
        print("Palabra:", palabra.decode('utf-8'), "Significado:", significado.decode('utf-8'))

def menu():
    while True:
        print("Menu"
              "\n1- Agregar Palabra"
              "\n2- Editar Palabra"
              "\n3- Mostrar Diccionario"
              "\n4- Eliminar Palabra"
              "\n5- Buscar Palabra"
              "\n6- Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            palabra = input("Ingrese palabra: ")
            significado = input("Ingrese significado: ")
            agregar_palabra(palabra, significado)
        elif opcion == 2:
            palabra = input("Ingrese palabra a modificar: ")
            nuevo_significado = input("Ingrese nuevo significado: ")
            editar_palabra(palabra, nuevo_significado)
        elif opcion == 3:
            mostrar_todas_las_palabras()
        elif opcion == 4:
            palabra = input("Ingrese palabra a eliminar: ")
            eliminar_palabra(palabra)
        elif opcion == 5:
            palabra = input("Ingrese palabra a buscar: ")
            resultado = buscar_palabra(palabra)
            if resultado:
                print("Palabra:", palabra, "Significado:", resultado)
            else:
                print("Palabra no encontrada.")
        elif opcion == 6:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()
