import pandas as pd
import sys
import sqlite3
from sqlite3 import Error

diccionario_notas = {}

notas_dicc = pd.DataFrame(diccionario_notas)


try:
    with sqlite3.connect("fase3base2.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS alumno(matricula INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS materia(idmateria INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS reporte(mat_alum INTEGER NOT NULL, id_materia INTEGER NOT NULL, calificacion INTEGER NOT NULL, periodo INTEGER NOT NULL, FOREIGN KEY(mat_alum) REFERENCES alumno(matricula), FOREIGN KEY(id_materia) REFERENCES materia(idmateria));")
        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    conn.close()

def guardar_alumno(matricula, nombre):
    try:
        with sqlite3.connect("fase3base2.db") as conn:
            mi_cursor = conn.cursor()
            valores = {"matricula":matricula, "nombre":diccionario}
            mi_cursor.execute("INSERT INTO alumno VALUES(:matricula,:nombre)", valores)
        print("Alumno agregado exitosamente a SQLite3")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

def guardar_materia(idmateria, materia):
    try:
        with sqlite3.connect("fase3base2.db") as conn:
            mi_cursor = conn.cursor()
            valores = {"idmateria":idmat, "materia":materianombre,}
            mi_cursor.execute("INSERT INTO materia VALUES(:idmateria,:materia)", valores)
            print()
    except Error as e:
        print()
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

def reporte_calificaciones(mat_alum, id_materia, calificacion, periodo):
    try:
        with sqlite3.connect("fase3base2.db") as conn:
            mi_cursor = conn.cursor()
            valores = {"mat_alum":suma, "id_materia":idmat, "calificacion":calif, "periodo":añoactual}
            mi_cursor.execute("INSERT INTO reporte VALUES(:mat_alum,:id_materia,:calificacion,:periodo)", valores)
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        
        
valor = 1
while valor != 6:
    separador1 = ("-*-*-*-*-*" * 10)
    print(separador1)
    print("BIENVENIDO \nElige una opcion : \n \n \t 1) REGISTRAR ALUMNOS \n \t 2) CAPTURAR CALIFICACIONES \n \t 3) ALUMNOS INSCRITOS (EXPORTAR ESTUDIANTES) \n \t 4) DESEMPEÑO ALUMNOS (EXPORTAR ESTADISTICAS DESCRIPTIVAS ALUMNOS)\n \t 5) ALUMNOS REPROBADOS (EXPORTAR ESTADISTICAS DESCRIPTIVAS MATERIAS)\n \t 6) SALIR DEL SISTEMA \n")
    valor = int(input("Accion a realizar: "))

    if valor < 7 and valor > 0:
        if valor == 1:
            print("REGISTRO DE ESTUDIANTES")
            for i in range(30):
                total = i + 1
                matricula = total
                diccionario = input(f"Matricula: {total} -Nombre del estudiante: ")
                diccionario_notas[diccionario] = [None,None,None,None,None]
                guardar_alumno(matricula, diccionario)
            input(f"Se agregaron {total} estudiantes de manera exitosa")
        
        if valor == 2:
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - PROGRAMACION")
            print(separador1)
            suma = 0
            añoactual = 2020
            for elemento in diccionario_notas:
                suma = suma + 1
                idmat = 100
                calif = int(input(f"Calificacion en PROGRAMACION de {elemento} :"))
                notas_dicc.at["Programacion",elemento] = calif
                materianombre = "programacion"
                guardar_materia(idmat, materianombre)
                reporte_calificaciones(suma, idmat, calif, añoactual)
                
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - BASE DE DATOS")
            print(separador1)
            suma = 0
            for elemento in diccionario_notas:
                suma = suma + 1
                idmat = 200
                calif = int(input(f"Calificacion en BASEDEDATOS de {elemento} :"))
                notas_dicc.at["Base de datos",elemento] = calif
                materianombre = "base de datos"
                guardar_materia(idmat, materianombre)
                reporte_calificaciones(suma, idmat, calif, añoactual)
           
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - MACROECONOMIA")
            print(separador1)
            suma = 0
            for elemento in diccionario_notas:
                suma = suma + 1
                idmat = 300
                calif = int(input(f"Calificacion en MACROECONOMIA de {elemento} :"))
                notas_dicc.at["Macroeconomia",elemento] = calif
                materianombre = "macroeconomia"
                guardar_materia(idmat, materianombre)
                reporte_calificaciones(suma, idmat, calif, añoactual)
            
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - CONTABILIDAD")
            print(separador1)
            suma = 0
            for elemento in diccionario_notas:
                suma = suma + 1
                idmat = 400
                calif = int(input(f"Calificacion en CONTABILIDAD de {elemento} :"))
                notas_dicc.at["Contabilidad",elemento] = calif
                materianombre = "contabilidad"
                guardar_materia(idmat, materianombre)
                reporte_calificaciones(suma, idmat, calif, añoactual)
           
           
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - CREATIVIDAD")
            print(separador1)
            suma = 0
            for elemento in diccionario_notas:
                suma = suma + 1
                idmat = 500
                calif = int(input(f"Calificacion en CREATIVIDAD de {elemento} :"))
                notas_dicc.at["Creatividad",elemento] = calif
                materianombre = "creatividad"
                guardar_materia(idmat, materianombre)
                reporte_calificaciones(suma, idmat, calif, añoactual)
            
            print(separador1)
            print("Calificaciones agregadas correctamente a SQLite3")
       
        if valor == 3:
            print(separador1)
            print("NOMBRES DE LOS ESTUDIANTES REGISTRADOS Y CALIFICACIONES\n")
            print(separador1)
            print(notas_dicc.T)
            preguntar = input("¿Quieres exportar el archivo?(si/no) ")
            if preguntar == "si":
                exportacion = int(input("¿En que metodo quieres exportar los datos? \n 1.- CSV \n 2.- JSON \nEscribe el numero de la opcion elegida: "))
                if exportacion < 3 and exportacion > 0:
                    if exportacion == 1:
                        notas_dicc.T.to_csv(r'estudiantesCSV.csv',index=True,header=True)
                        print("Exito, Exportacion a formato CSV")
                        print(separador1)
                    if exportacion == 2:
                        notas_dicc.T.to_json('estudiantesJSON.json', orient = "index")
                        print("Exito, Exportacion a formato JSON")
                        print(separador1)
                else:
                    print("Incorrecto, digita una opcion valida")
                    input("Enter para volver a menu")
            if preguntar == "no":
                input("Enter para volver al menu")
            if preguntar != "si" and preguntar != "no":
                input("Digita una opcion valida")
                
        if valor == 4:
            print(separador1)
            print("CALIFICACIONES NO APROBATORIAS")
            print(separador1)
            reprobados = notas_dicc.T[(notas_dicc.T<70)]
            print(reprobados)
            input("")
            print(separador1)
            print("CALIFICACIONES APROBATORIAS")
            print(separador1)
            aprobados = notas_dicc.T[(notas_dicc.T>70)]
            print(aprobados)
            input("")
            print(separador1)
            input("INFORMACION DE LOS ALUMNOS CON BAJO DESEMPEÑO")
            print(separador1)
            print(f"MATERIAS MAS REPROBADAS: \n{reprobados.count()}")
            print(separador1)
            print(f"PEOR NOTA: \n {notas_dicc.min()}")
            input("")
            print(separador1)
            print(f"MEJOR NOTA: \n {notas_dicc.max()}")
            input("")
            print(separador1)
            print(f"PROMEDIO GENERAL DE LOS ALUMNOS \n {notas_dicc.mean()}")
            print(separador1)
            input("")
            print("\t\tESTADISTICAS DESCRIPTIVAS DE LOS ALUMNOS\n")
            alumnos = notas_dicc.describe()
            print(alumnos)
            print(separador1)
            opcioon = input("¿Quieres exportar las estadisticas descriptivas de las alumnos?(si/no)")
            if opcioon == "si":
                alumnos.to_csv(r'estdesALUMNOS.csv', index=True, header=True)
                input("Listo, Enter para continuar")
            if opcioon == "no":
                input("")
            input("Enter para volver al menu")
        if valor == 5:
            print(separador1)
            print("\tALUMNOS REPROBADOS*")
            reprobadosT = notas_dicc.T[(notas_dicc.T<70)]
            print(reprobadosT)
            input("")
            
            print(separador1)
            print("\t\tTOTAL DE MATERIAS REPROBADAS POR LOS ALUMNOS\n")
            reprobados = notas_dicc[(notas_dicc<70)]
            cantidad = reprobados.count()
            print(cantidad)
            print(separador1)
            input("")
            print("\t\tESTADISTICAS DESCRIPTIVAS DE LAS MATERIAS*\n")
            reprobados4 = (notas_dicc.T.describe())
            print(reprobados4)
            opcioon = input("¿Quieres exportar las estadisticas descriptivas de las materias?(si/no)")
            if opcioon == "si":
                reprobados4.to_csv(r'estdesMATERIAS.csv', index=True, header=True)
                input("Listo, Enter para continuar")
            if opcioon == "no":
                input("")
            print("\tDESVIACION STANDARD*\n")
            reprobados2 = (notas_dicc.T.std())
            print(reprobados2)
            opcioon2 = input("¿Quieres exportar la desviacion estandar de las materias?(si/no)")
            if opcioon2 == "si":
                reprobados2.to_csv(r'desestMATERIAS.csv', index=True, header=True)
                input("Listo, Enter para continuar")
            if opcioon2 == "no":
                input("")
            input("Enter para volver al menu")

        if valor == 6:
            print("Saliendo del sistema...")

    else:
        print("XXXXXXXXXXXXXXXXXXX DIGITE UNA OPCION VALIDA XXXXXXXXXXXXXXXXXXX")
        input("Enter para volver al menu")
