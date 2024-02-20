from sqlite3 import Cursor
from multiprocessing import connection
import psycopg2

connection=psycopg2.connect(
host= "localhost",
user= "postgres",
password="Rufo2002",
database="Problema1_Parcial1_0980"
)

def opcion_1():
    
    print("MOASTRANDO RUTINAS: ")
    
    try:
        print("Conexión exitosa")
        # Crear un cursor para ejecutar consultas SQL
        cursor = connection.cursor()
        # Ejecutar la consulta SQL
        
        cursor.execute("""
            SELECT d.dia AS DIA,
                   r.rutinas AS RUTINA,
                   d.horas AS Horas_diarias,
                   e.tipo AS Ejercicio,
                   e.series AS "N series",
                   e.repeticiones AS REPS
            FROM rutina r
            JOIN dias d ON r.ndia = d.ndia
            JOIN ejercicios e ON r.ejercicio_id = e.nejercicio;
             """)
        # Obtener los resultados de la consulta
        rows = cursor.fetchall()
        # Mostrar los resultados
        for row in rows:
             print(row)

    except Exception as ex:
        print(ex)
    
def opcion_2():
    print("AGREGAR RUTINA")
    try:
        print("Conexión exitosa")
        
        print("Seleccione el día para la rutina:")
        cursor = connection.cursor()
        cursor.execute("SELECT ndia, dia FROM dias")
        dias = cursor.fetchall()
        for dia in dias:
            print(f"{dia[0]}. {dia[1]}")
        dia_seleccionado = int(input("Ingrese el número del día: "))
        
        print("Seleccione la intensidad de la rutina:")
        print("1. Bajo")
        print("2. Medio")
        print("3. Intenso")
        intensidad = int(input("Ingrese el número de la intensidad: "))
        opciones_intensidad = {1: "Bajo", 2: "Medio", 3: "Intenso"}
        intensidad_seleccionada = opciones_intensidad.get(intensidad)
        
        print("Seleccione los ejercicios para la rutina:")
        cursor.execute("SELECT nejercicio, tipo FROM ejercicios")
        ejercicios = cursor.fetchall()
        for ejercicio in ejercicios:
            print(f"{ejercicio[0]}. {ejercicio[1]}")
        ejercicios_seleccionados = input("Ingrese los números de los ejercicios separados por comas: ").split(",")
        
        for ejercicio_id in ejercicios_seleccionados:
            cursor.execute("INSERT INTO rutina(Rutinas, ndia, ejercicio_id) VALUES (%s, %s, %s)",
                           (intensidad_seleccionada, dia_seleccionado, int(ejercicio_id)))
            connection.commit()

        opcion_1()

    except Exception as ex:
        print(ex)




def opcion_3():
    print("OPCIÓN 3: EDITAR")
    try:
        print("Conexión exitosa")
        print("1. Editar ejercicios")
        print("2. Editar horas diarias de ejercicio")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("EDITAR EJERCICIOS")
            print("Seleccione el ejercicio que desea editar:")
            cursor = connection.cursor()
            cursor.execute("SELECT nejercicio, tipo FROM ejercicios")
            ejercicios = cursor.fetchall()
            for ejercicio in ejercicios:
                print(f"{ejercicio[0]}. {ejercicio[1]}")
            ejercicio_id = int(input("Ingrese el número del ejercicio a editar: "))

            print("¿Qué desea editar?")
            print("1. Series")
            print("2. Repeticiones")
            opcion_edicion = int(input("Ingrese el número de la opción a editar: "))
            if opcion_edicion not in [1, 2]:
                print("Opción inválida.")
                return opcion_3()

            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

            if opcion_edicion == 1:
                columna = "series"
            else:
                columna = "repeticiones"

            cursor.execute(f"UPDATE ejercicios SET {columna} = %s WHERE nejercicio = %s", (nueva_cantidad, ejercicio_id))
            connection.commit()

            print("¡Ejercicio actualizado correctamente!")

        elif opcion == 2:
            print("EDITAR HORAS DIARIAS DE EJERCICIO")
            print("Seleccione el día para editar las horas diarias de ejercicio:")
            cursor = connection.cursor()
            cursor.execute("SELECT ndia, dia FROM dias")
            dias = cursor.fetchall()
            for dia in dias:
                print(f"{dia[0]}. {dia[1]}")
            dia_seleccionado = int(input("Ingrese el número del día a editar: "))

            nueva_cantidad = int(input("Ingrese la nueva cantidad de horas: "))

            cursor.execute("UPDATE dias SET horas = %s WHERE ndia = %s", (nueva_cantidad, dia_seleccionado))
            connection.commit()

            print("¡Horas diarias actualizadas correctamente!")

        else:
            print("Opción no válida")

    except Exception as ex:
        print(ex)
 
    
def opcion_4():
    print("OPCIÓN 4: ELIMINAR RUTINA")
    try:
        print("Conexión exitosa")
        
        print("Seleccione la rutina que desea eliminar:")
        cursor = connection.cursor()
        cursor.execute("SELECT id, Rutinas FROM rutina")
        rutinas = cursor.fetchall()
        for rutina in rutinas:
            print(f"{rutina[0]}. {rutina[1]}")
        rutina_id = int(input("Ingrese el número de la rutina a eliminar: "))
        
        cursor.execute("DELETE FROM rutina WHERE id = %s", (rutina_id,))
        connection.commit()
        
        print("¡Rutina eliminada correctamente!")

    except Exception as ex:
        print(ex)


def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. MOSTRAR RUTINA")
        print("2. AGREGAR RUTINA")
        print("3. EDITAR EJERCICIOS")
        print("4. ELIMINAR RUTINA")
        print("5. Salir del programa")
        
        seleccion = input("Seleccione una opción (1-5): ")

        if seleccion == "1":
            opcion_1()
        elif seleccion == "2":
            opcion_2()
        elif seleccion == "3":
            opcion_3()
        elif seleccion == "4":
            opcion_4()
        elif seleccion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()
