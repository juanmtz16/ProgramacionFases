import pandas as pd

diccionario_notas = {}

notas_dicc = pd.DataFrame(diccionario_notas)

valor = 1
while valor != 6:
    separador1 = ("-*-*-*-*-*" * 10)
    print(separador1)
    print("BIENVENIDO \nElige una opcion : \n \n \t 1) REGISTRAR ALUMNOS \n \t 2) CAPTURAR CALIFICACIONES \n \t 3) ALUMNOS INSCRITOS (EXPORTAR ESTUDIANTES) \n \t 4) DESEMPEÑO ALUMNOS (EXPORTAR ESTADISTICAS DESCRIPTIVAS ALUMNOS)\n \t 5) ALUMNOS REPROBADOS (EXPORTAR ESTADISTICAS DESCRIPTIVAS MATERIAS)\n \t 6) SALIR DEL SISTEMA \n")
    valor = int(input("Accion a realizar: "))

    if valor < 7 and valor > 0:
        if valor == 1:
            print("REGISTRO DE ESTUDIANTES")
            for i in range(3):
                total = i + 1
                diccionario = input(f"{total}-.Nombre del estudiante: ")
                diccionario_notas[diccionario] = [None,None,None,None,None]
            input(f"Se agregaron {total} estudiantes de manera exitosa")

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
