
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
    return
