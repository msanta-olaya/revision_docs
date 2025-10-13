
import pandas as pd

def comprobar_vacios(df, columna):
    """
    Comprueba si una columna de un DataFrame contiene valores vacíos (NaN).
    
    Parámetros:
        df (pd.DataFrame): El DataFrame a analizar.
        columna (str): El nombre de la columna a comprobar.
    
    Return:
        bool: True si la columna NO tiene vacíos, False si sí los tiene.
    """
    if df[columna].notnull().all():
        return True, ""
    else:
        vacios = df[columna].isnull().sum()
        return False, f"La columna '{columna}' tiene {vacios} valores vacíos."


def valores_permitidos(df, columna, valores_permitidos):
    """
    Verifica si los valores de una columna del DataFrame están dentro de los valores permitidos.

    Parámetros
    ----------
    df : pandas.DataFrame
        El DataFrame a verificar.
    columna : str
        El nombre de la columna que se va a comprobar.
    valores_permitidos : list
        Lista con los valores aceptados para esa columna.

    Return
    -------
    pandas.DataFrame
        Un DataFrame con las filas que contienen valores no permitidos.
    """
    # Filtrar las filas donde el valor no está en la lista permitida
    df_invalidos = df[~df[columna].isin(valores_permitidos)]

    # Mostrar un resumen
    if df_invalidos.empty:
        return True, ""
    else:
        return False, f"Se encontraron {len(df_invalidos)} valores no permitidos en '{columna}'."
    
def comprobar_resp_fun(df, columna_clave, columnas_concat, diccionario_valores_permitidos):
    """
    Valida que el valor de una columna y la concatenación de otras tres columnas coincidan
    con las combinaciones indicadas en un diccionario {valor_clave: valor_concatenado}.
    
    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame a analizar.
    columna_clave : str
        Columna cuyo valor se usará como clave para el diccionario.
    columnas_concat : list
        Lista con las tres columnas cuyos valores se concatenarán.
    diccionario : dict
        Diccionario con estructura {valor_columna: concatenacion_esperada}.
    
    Return
    -------
    pandas.DataFrame
        Filas donde la concatenación real no coincide con la esperada según el diccionario.
    """
    # Crear una columna temporal con la concatenación real de las tres columnas
    df["concat_real"] = df[columnas_concat].fillna('').agg(''.join, axis=1)

    # Obtener el valor esperado del diccionario según la clave
    df["concat_esperada"] = df[columna_clave].map(diccionario_valores_permitidos)

    # Comparar ambas concatenaciones
    df_invalidos = df[df["concat_real"] != df["concat_esperada"]]

    # Mensaje de resumen
    if df_invalidos.empty:
        return True, ""
    else:
        return False, f"Se encontraron {len(df_invalidos)} registros con discrepancias."