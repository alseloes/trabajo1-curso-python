def ingresar_calificaciones():
    materias = []
    calificaciones = []
    continuar = 's'
    while continuar.lower() == 's':
        materia = input("Ingrese el nombre de la materia: ")
        calificacion = None
        while not isinstance(calificacion, (int, float)):
            calificacion = input(
                f"Ingrese la calificación para {materia} (0-10): ")
            if calificacion.isdigit() and 0 <= float(calificacion) <= 10:
                calificacion = float(calificacion)
            else:
                print(
                    "Entrada inválida. Por favor ingrese un número entre 0 y 10.")
        materias.append(materia)
        calificaciones.append(calificacion)
        continuar = None
        while continuar not in ['s', 'n']:
            continuar = input(
                "¿Desea ingresar otra materia? (s/n): ").strip().lower()
            if continuar not in ['s', 'n']:
                print("Entrada inválida. Por favor ingrese 's' o 'n'.")
    return materias, calificaciones


def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = [i for i, cal in enumerate(calificaciones) if cal >= umbral]
    reprobadas = [i for i, cal in enumerate(calificaciones) if cal < umbral]
    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    return indice_max, indice_min


def main():
    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        print("No se ingresaron materias. Finalizando el programa.")
        return

    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    indice_max, indice_min = encontrar_extremos(calificaciones)

    print("\nResumen Final:")
    print("Materias y Calificaciones:")
    for i, materia in enumerate(materias):
        print(f"{materia}: {calificaciones[i]}")

    print(f"\nPromedio General: {promedio:.2f}")

    print("\nMaterias Aprobadas:")
    for i in aprobadas:
        print(f"{materias[i]}: {calificaciones[i]}")

    print("\nMaterias Reprobadas:")
    for i in reprobadas:
        print(f"{materias[i]}: {calificaciones[i]}")

    if indice_max is not None and indice_min is not None:
        print(
            f"\nMateria con Mejor Calificación: {materias[indice_max]} ({calificaciones[indice_max]})")
        print(
            f"Materia con Peor Calificación: {materias[indice_min]} ({calificaciones[indice_min]})")

    print("\nGracias por usar la calculadora de promedios. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
