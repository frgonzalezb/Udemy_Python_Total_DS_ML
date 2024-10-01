"""
Proyecto del día 9
Consulta de temperaturas interactiva
"""


import os
import time

import numpy as np
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
                break


if __name__ == '__main__':
    correr_programa()
