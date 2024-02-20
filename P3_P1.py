import psycopg2
from datetime import datetime, timedelta

# Conexión a la base de datos
connection = psycopg2.connect(
    host= "localhost",
    user= "postgres",
    password="Rufo2002",
    database="Problema3_Parcial1_0980"
)

def opcion_1():
    try:
        nombre = input("Nombre: ")
        telefono = input("Por favor, ingresa tu número de teléfono en el formato 1234-5678: ")
        cantidad_ml = int(input("Ingrese la cantidad de agua consumida en mililitros: "))
        fecha = input("Ingrese la fecha del consumo (en formato YYYY-MM-DD) o presione Enter para usar la fecha actual: ")
        if fecha:
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        else:
            fecha = datetime.now().date()

        # Verificar si el usuario ya está registrado
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE telefono = %s", (telefono,))
        usuario = cursor.fetchone()

        if usuario:
            usuario_id = usuario[0]
        else:
            # Si el usuario no está registrado, registrarlos
            cursor.execute("INSERT INTO usuarios(nombre, telefono) VALUES (%s, %s) ON CONFLICT (telefono) DO NOTHING RETURNING id", (nombre, telefono))
            connection.commit()
            usuario = cursor.fetchone()
            if usuario:
                usuario_id = usuario[0]
                print("¡Usuario registrado correctamente!")
            else:
                # Obtener el ID del usuario existente si ya está registrado
                cursor.execute("SELECT id FROM usuarios WHERE telefono = %s", (telefono,))
                usuario_id = cursor.fetchone()[0]

        # Registrar consumo de agua
        cursor.execute("INSERT INTO consumo_agua(usuario_id, fecha, cantidad_ml) VALUES (%s, %s, %s)",
                       (usuario_id, fecha, cantidad_ml))
        connection.commit()
        print("Registro de consumo de agua realizado correctamente.")
    except Exception as ex:
        print("Error al registrar consumo de agua:", ex)


def opcion_2():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT consumo_agua.cantidad_ml, usuarios.nombre FROM consumo_agua INNER JOIN usuarios ON consumo_agua.usuario_id = usuarios.id")
        consumos = cursor.fetchall()
        if not consumos:
            print("No hay registros de consumo de agua.")
        else:
            print("Consumo de agua registrado por:")
            for consumo in consumos:
                print(f"Nombre: {consumo[1]}, Cantidad: {consumo[0]} ml")
    except Exception as ex:
        print("Error al obtener registros de consumo de agua:", ex)

def opcion_3(dias=7):
    try:
        cursor = connection.cursor()
        fecha_limite = datetime.now().date() - timedelta(days=dias)
        cursor.execute("SELECT AVG(cantidad_ml) FROM consumo_agua WHERE fecha >= %s", (fecha_limite,))
        promedio = cursor.fetchone()[0]
        if promedio:
            print(f"El consumo promedio de agua en los últimos {dias} días es de aproximadamente {promedio:.2f} mililitros por día.")
            opcion_2()  # Mostrar las personas que registraron el consumo
        else:
            print("No hay registros de consumo de agua en los últimos días.")
    except Exception as ex:
        print("Error al calcular el consumo promedio:", ex)

def menu():
    print("\nSeleccione una opción:")
    print("1. Registrar consumo de agua")
    print("2. Ver consumo y personas que registraron el consumo")
    print("3. Ver consumo promedio de los últimos 7 días")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        opcion_3()
    elif opcion == "4":
        print("Saliendo del programa.")
        return False
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
    return True

if __name__ == "__main__":
    print("¡Bienvenido al sistema de registro de consumo de agua!")
    continuar = True
    while continuar:
        continuar = menu()

# Cierre de la conexión a la base de datos
connection.close()