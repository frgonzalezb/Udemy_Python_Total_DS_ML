"""
Proyecto del día 9
Consulta de temperaturas interactiva
"""


import os
import time

import pandas as pd
import matplotlib.pyplot as plt


def limpiar_consola() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def cargar_dataframe(ruta: str) -> pd.DataFrame:
    return pd.read_csv(ruta)


def mostrar_titulo() -> None:
    print('### CONSULTA DE TEMPERATURAS INTERACTIVO ###\n')


def continuar() -> None:
    input('Presione ENTER para continuar...')


def mostrar_error(mensaje: str) -> None:
    print('ERROR:', mensaje)
    continuar()


def obtener_ciudades(df: pd.DataFrame) -> list[str]:
    ciudades: list[str] = df['Ciudad'].unique().tolist()
    return ciudades


def obtener_nombre_mes(mes: str) -> str:
    meses = {
        '1': 'Enero',
        '2': 'Febrero',
        '3': 'Marzo',
        '4': 'Abril',
        '5': 'Mayo',
        '6': 'Junio',
        '7': 'Julio',
        '8': 'Agosto',
        '9': 'Septiembre',
        '10': 'Octubre',
        '11': 'Noviembre',
        '12': 'Diciembre'
    }
    return meses[mes]


def procesar_datos(df: pd.DataFrame, ciudad: str, mes: str) -> tuple:
    nombre_ciudad = df['Ciudad'].iloc[int(ciudad) - 1]
    df = df[df['Ciudad'] == nombre_ciudad][df['Fecha'].dt.month == int(mes)]
    nombre_mes: str = obtener_nombre_mes(mes)
    minimas = df['Temperatura Minima'].tolist()
    maximas = df['Temperatura Maxima'].tolist()
    return nombre_ciudad, nombre_mes, minimas, maximas


def mostrar_grafico(
        ciudad: str,
        mes: str,
        minimas: list[float],
        maximas: list[float]
        ) -> None:
    """
    Muestra un gráfico de temperaturas mínimas y máximas para una ciudad
    y mes específicos.

    Parámetros:
        ciudad (str): Nombre de la ciudad para la que se mostrará el
            gráfico.
        mes (str): Mes para el que se mostrará el gráfico.
        minimas (list[float]): Lista de temperaturas mínimas para el mes
            y ciudad seleccionados.
        maximas (list[float]): Lista de temperaturas máximas para el mes
            y ciudad seleccionados.

    Retorna:
        None
    """
    dias: list[int] = list(range(1, len(minimas) + 1))

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dias, minimas, label='Minimas', marker='o')
    ax.plot(dias, maximas, label='Maximas', marker='o')
    ax.set_xticks(dias)
    ax.set_xlabel('Día')
    ax.set_ylabel('Temperatura (°C)')
    ax.legend()

    plt.title(
        f'Temperaturas mínimas y máximas para el mes de {mes} en {ciudad}',
        fontsize=16,
        fontweight='bold',
        pad=20
    )
    plt.grid()
    plt.show()


def pedir_mes() -> str:
    return input('\nIntroduce un mes (1 - 12): ')


def pedir_ciudad(df: pd.DataFrame) -> str:
    ciudades: list[str] = obtener_ciudades(df)
    for i, ciudad in enumerate(ciudades):
        print(f'{i+1}. {ciudad}')

    return input('\nSeleccione una ciudad (1 - 5) o digite 0 para salir: ')


def validar_opcion(opcion: str, rango: tuple[int, int]) -> bool:
    if not opcion.isnumeric():
        return False

    opcion_int: int = int(opcion)
    if opcion_int < rango[0] or opcion_int > rango[1]:
        return False

    return True


def salir() -> None:
    print('Saliendo del programa...')
    time.sleep(1.5)
    exit()


def correr_programa() -> None:
    """
    Pasos:

    1. Cargar un DataFrame con los datos meteorológicos provistos en el
    archivo descargable de esta lección.

    2. Asegúrate de que las fechas estén en el formato correcto para su
    manipulación posterior.

    3. Crea un programa (una función o un conjunto de funciones) que le
    pida al usuario que seleccione una ciudad de la lista de ciudades
    disponibles en nuestro DataFrame, y un mes del año.

    4. Muéstrale al usuario un gráfico que muestre las temperaturas
    mínimas y máximas que se registraron en la ciudad elegida durante el
    mes elegido.

    5. El programa debe preguntarle al usuario si desea seguir haciendo
    consultas o no.
    """
    # 1.
    df: pd.DataFrame = cargar_dataframe(
        './09_Matplotlib/Proyecto/data/Datos+Meteorológicos_Arg_2023.csv'
    )

    # 2.
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

    # 3.
    while True:
        limpiar_consola()
        mostrar_titulo()

        ciudad: str = pedir_ciudad(df)
        if ciudad == '0':
            salir()
        if not validar_opcion(ciudad, (1, 5)):
            mostrar_error('La opción ingresada no es válida')
        if ciudad >= '1' and ciudad <= '5':
            mes: str = pedir_mes()
            if not validar_opcion(mes, (1, 12)):
                mostrar_error('La opción ingresada no es válida')
            if mes >= '1' and mes <= '12':
                # 4.
                ciudad, mes, minimas, maximas = procesar_datos(df, ciudad, mes)
                mostrar_grafico(ciudad, mes, minimas, maximas)
                continuar()


if __name__ == '__main__':
    correr_programa()
