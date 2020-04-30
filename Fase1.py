import pandas as pd

diccionario_notas = {}

notas_dicc = pd.DataFrame(diccionario_notas)

valor = 1
while valor != 6:
    separador1 = ("-*-*-*-*-*" * 10)
    print(separador1)
    print("BIENVENIDO \nElige una opcion : \n \n \t 1) REGISTRAR ALUMNOS \n \t 2) CAPTURAR CALIFICACIONES \n \t 3) ALUMNOS INSCRITOS \n \t 4) DESEMPEÑO ALUMNOS \n \t 5) ALUMNOS REPROBADOS \n \t 6) SALIR DEL SISTEMA \n")
    valor = int(input("Accion a realizar: "))
    if valor < 7 and valor > 0:
        if valor == 1:
            print("REGISTRO DE ESTUDIANTES")
            for i in range(30):
                diccionario = input("Agrega un alumno: ")
                diccionario_notas[diccionario] = [None,None,None,None,None]
            input("")
        if valor == 2:
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - PROGRAMACION")
            print(separador1)
            for elemento in diccionario_notas:
                programacion = int(input(f"Calificacion en PROGRAMACION de {elemento} :"))
                notas_dicc.at["Programacion",elemento] = programacion
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - BASE DE DATOS")
            print(separador1)
            for elemento in diccionario_notas:
                basededatos = int(input(f"Calificacion en BASEDEDATOS de {elemento} :"))
                notas_dicc.at["Base de datos",elemento] = basededatos
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - MACROECONOMIA")
            print(separador1)
            for elemento in diccionario_notas:
                macroeconomia = int(input(f"Calificacion en MACROECONOMIA de {elemento} :"))
                notas_dicc.at["Macroeconomia",elemento] = macroeconomia
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - CONTABILIDAD")
            print(separador1)
            for elemento in diccionario_notas:
                contabilidad = int(input(f"Calificacion en CONTABILIDAD de {elemento} :"))
                notas_dicc.at["Contabilidad",elemento] = contabilidad
            print(separador1)
            print("CAPTURA DE CALIFICACIONES DE LOS ESTUDIANTES - CREATIVIDAD")
            print(separador1)
            for elemento in diccionario_notas:
                creatividad = int(input(f"Calificacion en CREATIVIDAD de {elemento} :"))
                notas_dicc.at["Creatividad",elemento] = creatividad
            print(separador1)
            
        if valor == 3:
            print(separador1)
            print("NOMBRES DE LOS ESTUDIANTES REGISTRADOS Y CALIFICACIONES\n")
            print(separador1)
            print(notas_dicc.T)
            input("Enter para volver al menu")
            
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
            print("\t\tESTADISTICAS DESCRIPTIVAS*\n")
            reprobados2 = (notas_dicc.T.describe())
            print(reprobados2)
            input("")
            print("\tDESVIACION STANDARD*\n")
            reprobados2 = (notas_dicc.T.std())
            print(reprobados2)
            input("Enter para volver al menu")
        if valor == 6:
            print("Saliendo del sistema...")
    else:
        print("XXXXXXXXXXXXXXXXXXX DIGITE UNA OPCION VALIDA XXXXXXXXXXXXXXXXXXX")
        input("Enter para volver al menu")
