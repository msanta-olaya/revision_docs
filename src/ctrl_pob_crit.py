"""
ctrl_pob_crit.py

Este módulo contiene funciones para ejecutar los controles necesarios para asegurar la correctitud de la Poblacion de críticos.
"""
import pandas as pd
import sys

def conceptos_duplicados(df, columnas_concat):
    # Crear una columna temporal con la concatenación real de las tres columnas
    df["concat_real"] = df[columnas_concat].fillna('').agg(''.join, axis=1)

    # Filtrar duplicados
    df_duplicados = df[df.duplicated(subset=["concat_real"], keep=False)]

    if df_duplicados.empty:
        return True, ""
    else:
        df_duplicados.to_excel("output/conceptos_duplicados_pob_crit.xlsx", index=False)
        return False, f"Se encontraron {df_duplicados["concat_real"].nunique()} valores duplicados. Más detalle en el excel output/conceptos_duplicados_pob_crit.xlsx"

def buscar_componentes(df, columna_componentes, columna_conceptos, separador=';'):
    resultado = {}

    # Crear un set con todos los valores de la columna de búsqueda (para búsqueda rápida)
    valores_busqueda = set(df[columna_conceptos].dropna().astype(str))

    for idx, fila in df.iterrows():
        # Tomar el valor de la columna origen
        valor = fila[columna_componentes]

        # Saltar si la celda está vacía o es NaN
        if pd.isna(valor) or str(valor).strip() == "":
            continue

        # Descomponer la string en subvalores
        subvalores = [v.strip() for v in str(valor).split(separador) if v.strip()]

        # Buscar subvalores que NO estén en columna_busqueda
        no_encontrados = [v for v in subvalores if v not in valores_busqueda]

        if no_encontrados:
            resultado[idx] = no_encontrados
    
    if not resultado:
        return True, ""
    else:
        return False, f"No se encontraron los componentes, {resultado}, en la columna Concepto deducido del informe."
