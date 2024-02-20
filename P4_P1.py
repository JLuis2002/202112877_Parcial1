import psycopg2
from datetime import datetime

# Conexión a la base de datos
connection = psycopg2.connect(
    host= "localhost",
    user= "postgres",
    password="Rufo2002",
    database="Problema4_Parcial1_0980"
)

def registrar_lectura():
    try:
        libro_id = int(input("Ingrese el ID del libro que ha leído: "))
        fecha_lectura = input("Ingrese la fecha de lectura del libro (en formato YYYY-MM-DD) o presione Enter para usar la fecha actual: ")
        if fecha_lectura:
            fecha_lectura = datetime.strptime(fecha_lectura, "%Y-%m-%d").date()
        else:
            fecha_lectura = datetime.now().date()
        paginas_leidas = int(input("Ingrese el número de páginas que ha leído: "))
        nota = input("Ingrese alguna nota adicional (opcional): ")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO lecturas(libro_id, usuario_id, fecha_lectura, paginas_leidas, nota) VALUES (%s, %s, %s, %s, %s)",
                       (libro_id, usuario_id, fecha_lectura, paginas_leidas, nota))
        connection.commit()
        print("Lectura registrada correctamente.")
    except Exception as ex:
        print("Error al registrar lectura:", ex)

def establecer_meta():
    try:
        fecha_inicio = input("Ingrese la fecha de inicio de la meta (en formato YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin de la meta (en formato YYYY-MM-DD): ")
        paginas_objetivo = int(input("Ingrese el número total de páginas que desea leer durante este período: "))

        cursor = connection.cursor()
        cursor.execute("INSERT INTO metas_lectura(usuario_id, fecha_inicio, fecha_fin, paginas_objetivo, cumplida) VALUES (%s, %s, %s, %s, %s)",
                       (usuario_id, fecha_inicio, fecha_fin, paginas_objetivo, False))
        connection.commit()
        print("Meta de lectura establecida correctamente.")
    except Exception as ex:
        print("Error al establecer meta de lectura:", ex)

def obtener_recomendaciones():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT titulo, autor, genero FROM libros")
        libros = cursor.fetchall()
        if libros:
            print("Recomendaciones:")
            for libro in libros:
                print(f"Título: {libro[0]}, Autor: {libro[1]}, Género: {libro[2]}")
        else:
            print("No hay libros disponibles en este momento.")
    except Exception as ex:
        print("Error al obtener recomendaciones:", ex)

def mostrar_metas():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT fecha_inicio, fecha_fin, paginas_objetivo, cumplida FROM metas_lectura WHERE usuario_id = %s", (usuario_id,))
        metas = cursor.fetchall()
        if metas:
            print("Metas de lectura:")
            for meta in metas:
                fecha_inicio = meta[0].strftime("%Y-%m-%d") if meta[0] else "No definida"
                fecha_fin = meta[1].strftime("%Y-%m-%d") if meta[1] else "No definida"
                cumplida = "Sí" if meta[3] else "No"
                print(f"Fecha de inicio: {fecha_inicio}, Fecha de fin: {fecha_fin}, Páginas objetivo: {meta[2]}, Cumplida: {cumplida}")
        else:
            print("No hay metas de lectura establecidas.")
    except Exception as ex:
        print("Error al obtener metas de lectura:", ex)


def mostrar_lecturas():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT libros.titulo, lecturas.fecha_lectura, lecturas.paginas_leidas, lecturas.nota FROM lecturas INNER JOIN libros ON lecturas.libro_id = libros.id WHERE lecturas.usuario_id = %s", (usuario_id,))
        lecturas = cursor.fetchall()
        if lecturas:
            print("Lecturas realizadas:")
            for lectura in lecturas:
                print(f"Título: {lectura[0]}, Fecha de lectura: {lectura[1]}, Páginas leídas: {lectura[2]}, Nota: {lectura[3]}")
        else:
            print("No hay lecturas registradas.")
    except Exception as ex:
        print("Error al obtener lecturas:", ex)


def menu():
    print("\nSeleccione una opción:")
    print("1. Registrar lectura")
    print("2. Establecer meta de lectura")
    print("3. Ver recomendaciones")
    print("4. Ver metas de lectura")
    print("5. Ver lecturas registradas")
    print("6. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        registrar_lectura()
    elif opcion == "2":
        establecer_meta()
    elif opcion == "3":
        obtener_recomendaciones()
    elif opcion == "4":
        mostrar_metas()
    elif opcion == "5":
        mostrar_lecturas()
    elif opcion == "6":
        print("Saliendo del programa.")
        return False
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
    return True

if __name__ == "__main__":
    print("¡Bienvenido al control de hábitos de lectura!")
    nombre_usuario = input("Por favor, ingrese su nombre: ")
    email_usuario = input("Ingrese su correo electrónico: ")
    
    # Verificar si el usuario ya está registrado
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email_usuario,))
        usuario = cursor.fetchone()
        
        if usuario:
            usuario_id = usuario[0]
        else:
            # Si el usuario no está registrado, registrarlos
            cursor.execute("INSERT INTO usuarios(nombre, email) VALUES (%s, %s) RETURNING id", (nombre_usuario, email_usuario))
            connection.commit()
            usuario_id = cursor.fetchone()[0]
            print("¡Usuario registrado correctamente!")
        
        # Menú de opciones
        continuar = True
        while continuar:
            continuar = menu()
    except Exception as ex:
        print("Error:", ex)

# Cierre de la conexión a la base de datos
connection.close()