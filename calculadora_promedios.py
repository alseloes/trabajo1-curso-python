def ingresar_calificaciones():
    """
    Solicita al usuario el nombre de las materias y sus calificaciones.

    Permite ingresar múltiples materias hasta que el usuario indique que
    desea finalizar. Valida que el nombre de la materia no esté vacío y que
    la calificación sea un número entre 0 y 10.

    Returns:
        tuple[list[str], list[float]] | tuple[None, None]:
            Una tupla con la lista de materias y la lista de calificaciones.
            Si el usuario no ingresa ninguna materia, retorna (None, None).
    """

    materias = []
    calificaciones = []
    continuar = 's'
    while continuar.lower() == 's':
        materia = input("Ingrese el nombre de la materia: ")
        calificacion = None
        while not isinstance(calificacion, (int, float)):
            if materia == "" and len(materias) == 0:
                return None, None
            elif materia == "" and len(materias) > 0:
                print("Ingrese un nombre de materia válido")
                materia = input("Ingrese el nombre de la materia: ")
                continue
            calificacion = input(
                f"Ingrese la calificación para {materia} (0-10): ")
            if isfloat(calificacion) and 0 <= float(calificacion) <= 10:
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
    """
    Calcula el promedio de una lista de calificaciones.

    Args:
        calificaciones (list[float]): Lista de calificaciones.

    Returns:
        float: El promedio de las calificaciones. Retorna 0 si la lista está
        vacía.
    """

    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Determina cuáles materias están aprobadas y cuáles reprobadas.

    Args:
        calificaciones (list[float]): Lista de calificaciones.
        umbral (float, optional): Calificación mínima para aprobar.
            Por defecto es 5.0.

    Returns:
        tuple[list[int], list[int]]:
            Dos listas con los índices de las materias aprobadas y
            reprobadas, respectivamente.
    """

    aprobadas = [i for i, cal in enumerate(calificaciones) if cal >= umbral]
    reprobadas = [i for i, cal in enumerate(calificaciones) if cal < umbral]
    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Encuentra los índices de las calificaciones máximas y mínimas.

    Args:
        calificaciones (list[float]): Lista de calificaciones.

    Returns:
        tuple[list[int], list[int]] | tuple[None, None]:
            Una tupla con los índices de las calificaciones máximas y
            mínimas. Si la lista está vacía, retorna (None, None).
    """

    if not calificaciones:
        return None, None
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    return indice_max, indice_min


def isfloat(valor):
    """
    Verifica si un valor puede convertirse a un número de tipo float.

    Args:
        valor (Any): Valor a validar.

    Returns:
        bool: True si el valor puede convertirse a float; False en caso
        contrario.
    """

    try:
        float(valor)
        return True
    except ValueError:
        return False


def main():
    """
    Ejecuta el flujo principal del programa.

    Solicita las materias y calificaciones al usuario, calcula el promedio,
    determina las materias aprobadas y reprobadas, identifica las mejores y
    peores calificaciones, y muestra un resumen con toda la información.

    Returns:
        None
    """

    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        print("No se ingresaron materias. Finalizando el programa.")
        return

    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    indice_max, indice_min = encontrar_extremos(calificaciones)

    print("\nRESUMEN FINAL:")
    print("Materias y Calificaciones:")
    for i, materia in enumerate(materias):
        print(f"- {materia}: {calificaciones[i]}")

    print(f"\nPromedio General: {promedio:.2f}")

    print("\nMaterias Aprobadas:")
    for i in aprobadas:
        print(f"{materias[i]}: {calificaciones[i]}")

    print("\nMaterias Reprobadas:")
    for i in reprobadas:
        print(f"{materias[i]}: {calificaciones[i]}")

    print(
        f"\nMateria con mejor calificación: {materias[indice_max]} ({calificaciones[indice_max]})")
    print(
        f"Materia con peor calificación: {materias[indice_min]} ({calificaciones[indice_min]})")

    print("\nGracias por usar la calculadora de promedios. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
