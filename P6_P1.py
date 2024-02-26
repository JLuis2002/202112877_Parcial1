import psycopg2

# Establecer conexión con la base de datos
connection = psycopg2.connect(
    host= "localhost",
    user= "postgres",
    password="Rufo2002",
    database="Parcial1"
)

def agregar_dia_sueño():
    semana = int(input("Ingrese el número de semana (1 o 2): "))
    dia = input("Ingrese el día de la semana: ")
    horas = int(input("Ingrese la cantidad de horas de sueño: "))

    cursor = connection.cursor()
    cursor.execute("INSERT INTO horas (semana, dia, horas) VALUES (%s, %s, %s)", (semana, dia, horas))
    connection.commit()

    print("Día de sueño agregado exitosamente.")

def ver_historial_sueño():
    semana = int(input("Ingrese el número de semana (1 o 2): "))

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM horas WHERE semana = %s", (semana,))
    historial = cursor.fetchall()

    print("Historial de sueño:")
    for registro in historial:
        print(registro)

def recomendar_sueño(menos=True):
    cursor = connection.cursor()
    if menos:
        cursor.execute("SELECT metodo, recomendacion FROM recomendaciones ORDER BY id ASC LIMIT 3")
    else:
        cursor.execute("SELECT metodo, recomendacion FROM recomendaciones ORDER BY id DESC LIMIT 3")

    recomendaciones = cursor.fetchall()

    print("Recomendaciones:")
    for metodo, recomendacion in recomendaciones:
        print(f"{metodo}: {recomendacion}")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar nuevo día de sueño")
        print("2. Ver historial de sueño")
        print("3. Recomendaciones para días con menos horas de sueño")
        print("4. Recomendaciones para días con más horas de sueño")
        print("5. Salir del programa")

        seleccion = input("Seleccione una opción (1-5): ")

        if seleccion == "1":
            agregar_dia_sueño()
        elif seleccion == "2":
            ver_historial_sueño()
        elif seleccion == "3":
            recomendar_sueño(menos=True)
        elif seleccion == "4":
            recomendar_sueño(menos=False)
        elif seleccion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    menu()
