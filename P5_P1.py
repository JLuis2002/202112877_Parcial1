import psycopg2

# Conexión a la base de datos
connection = psycopg2.connect(
    host= "localhost",
    user= "postgres",
    password="Rufo2002",
    database="Parcial1"
)

def mostrar_viajes():
    try:
        print("Historial de Viajes:")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM viajes")
        viajes = cursor.fetchall()
        for viaje in viajes:
            print(viaje)
    except Exception as ex:
        print("Error al mostrar viajes:", ex)

def agregar_viaje():
    try:
        destino = input("Ingrese el destino del viaje: ")
        costo_alojamiento = float(input("Ingrese el costo de alojamiento (en Q): "))
        costo_comida = float(input("Ingrese el costo de comida (en Q): "))
        costo_transporte = float(input("Ingrese el costo de transporte (en Q): "))
        descripcion = input("Ingrese una descripción del viaje: ")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO viajes (destino, alojamiento, comida, transporte, descripcion, fecha) VALUES (%s, %s, %s, %s, %s, current_date)", (destino, costo_alojamiento, costo_comida, costo_transporte, descripcion))
        connection.commit()
        print("Viaje agregado exitosamente!")
    except Exception as ex:
        print("Error al agregar viaje:", ex)

def destino_menos_gastos():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT destino FROM viajes ORDER BY alojamiento + comida + transporte ASC LIMIT 1")
        destino = cursor.fetchone()[0]
        print(f"El destino en el que has gastado menos es: {destino}")
    except Exception as ex:
        print("Error al obtener destino con menos gastos:", ex)

def gasto_total_viaje():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT destino, alojamiento + comida + transporte AS TOTAL FROM viajes")
        gastos = cursor.fetchall()
        print("Gasto total de cada viaje:")
        for gasto in gastos:
            print(f"Destino: {gasto[0]}, Gasto total: {gasto[1]} Q")
    except Exception as ex:
        print("Error al obtener gasto total de cada viaje:", ex)

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar historial de viajes")
        print("2. Agregar nuevo viaje")
        print("3. Ver destino con menos gastos")
        print("4. Ver gasto total de cada viaje")
        print("5. Salir del programa")

        seleccion = input("Seleccione una opción (1-5): ")

        if seleccion == "1":
            mostrar_viajes()
        elif seleccion == "2":
            agregar_viaje()
        elif seleccion == "3":
            destino_menos_gastos()
        elif seleccion == "4":
            gasto_total_viaje()
        elif seleccion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    menu()