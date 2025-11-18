"""
ctrl_inventario.py

Este módulo contiene funciones para ejecutar los controles necesarios para asegurar la correctitud del Inventario de constroles consolidado.
"""
import pandas as pd
import sys

def len_id(df, columna, max_longitud=15):
    # Convertimos los valores a string por si hay números u otros tipos
    exceso = df[columna].astype(str).str.len() > max_longitud

    if exceso.any():
        return False, f"Se encontraron los siguiente IDs que superan la longitus máxima: {df[columna][exceso]}"
    else: 
        return True, ""
    
def formato_id_modoejec(df, columna_origen, columna_busqueda):
    # Definimos el mapa de correspondencia
    mapa = {'_M_': 'Manual', '_A_': 'Automático', '_S_': 'Asegurado por sistema'}

    # Función para comprobar cada fila
    def validar_fila(fila):
        for letra, modo in mapa.items():
            if letra in str(fila[columna_origen]).upper():  # verificamos si la letra aparece en el ID
                return fila[columna_busqueda].lower() == modo.lower()
        return True  # Si no hay M/A/S en el ID, no hay error    

    # Aplicamos la función a cada fila
    errores = df[~df.apply(validar_fila, axis=1)]
    errores.to_excel("hhh.xlsx")

    if errores.empty:
        return True, ""
    else:
        return False, f"Se han encontrado las siguientes inconsistencias entre el ID y el modo de ejecución: {errores}"
    
def formato_id_tipoctrl(df, columna_origen, columna_busqueda):
    # Definimos el mapa de correspondencia
    mapa = {'N1_': ['Completitud', 'Completitud en procesos', 'Formato', 'Valores permitidos'], 
            'N2_': ['Coherencia funcional', 'Conciliación contable', 'Razonabilidad'], 
            'N3_': ['Asegurado por sistema', 'Proveedor externo', 'Consistencia entre fuentes', 'Reconciliación origen-destino'],
            'N4_': ['Agrupación de controles']}

    # Función para comprobar cada fila
    def validar_fila(fila):
        id_val = str(fila[columna_origen]).upper().strip()
        tipo_ctrl = str(fila[columna_busqueda]).strip()

        # Busca a qué grupo (N1, N2...) pertenece el ID
        for prefijo, tipos_validos in mapa.items():
            if id_val.startswith(prefijo):  # usa startswith en lugar de "in" para precisión
                # Si el tipo no está dentro de los permitidos → error
                return tipo_ctrl not in tipos_validos
        
        # Si no contiene N1_, N2_, N3_ o N4_, no lo consideramos error
        return False  

    # Aplicamos la función a cada fila
    errores_aux = df.apply(validar_fila, axis=1).astype(bool)

    errores = df[errores_aux].copy()
    errores.to_excel("lll.xlsx", index=False)

    if errores.empty:
        return True, ""
    else:
        return False, f"Se han encontrado las siguientes inconsistencias entre el ID y el tipo de control: {errores}"
    
def comprobar_ids_repetidos(df, columna_id, columna_informe, columnas_concat):
    # Crear una columna temporal con la concatenación real de las tres columnas
    df["concat"] = df[columnas_concat].fillna('').agg(''.join, axis=1)

    # Agrupamos por concat
    inconsistencias = []
    for concat_val, grupo in df.groupby('concat'):
        informes_unicos = grupo[columna_informe].nunique()
        ids_unicos = grupo[columna_id].nunique()

        # Si hay más de un informe pero varios IDs → inconsistencia
        if informes_unicos > 1 and ids_unicos > 1:
            inconsistencias.append(grupo)

    # Unimos los grupos con error
    if inconsistencias:
        df_errores = pd.concat(inconsistencias)
        df_errores.to_excel("output/errores_id_informe.xlsx", index=False)
        return False, f"Se han encontrado inconsistencias de ID entre informes. Se han encontrado IDs duplicados para el mismo dato-control. Se han guardado en 'errores_id_informe.xlsx'."
    else:
        return True, ""
    
def comprobar_concepto_pob_crit(df_pob_crit, df_invt, col_pob_crit, col_invt):
    # Normalizar espacios y mayúsculas/minúsculas
    df_pob_crit['_clave'] = df_pob_crit[col_pob_crit].astype(str).str.strip().str.upper()
    df_invt['_clave'] = df_invt[col_invt].astype(str).str.strip().str.upper()

    # Hacemos un merge left: si no encuentra match, se rellena con NaN
    df_merged = df_invt.merge(
        df_pob_crit[['_clave']],
        on='_clave',
        how='left',
        indicator=True  # indica si encontró match
    )

    # Filas que no encontraron correspondencia
    errores = df_merged[df_merged['_merge'] == 'left_only'].copy()

    if errores.empty:
        return True, ""
    else:
        errores.drop(columns=['_clave', '_merge'], inplace=True)
        errores.to_excel("output/errores_conceptos_pob_crit.xlsx", index=False)
        return False, f"Se encontraron registros en el inventario que no están en la población de críticos. Se han guardado en 'errores_inclusion_pob_crit.xlsx'."
    
def valores_resp_ejecutar(df, columna_origen, columna_busqueda):
    # Definimos el mapa de correspondencia
    mapa = {'Calidad': 'Automático', 'Tecnología': 'Automático', 'N/A': 'Asegurado por sistema'}

    # Función para comprobar cada fila
    def validar_fila(fila):
        for letra, modo in mapa.items():
            if letra in str(fila[columna_origen]).upper():  # verificamos si la letra aparece en el ID
                return fila[columna_busqueda].lower() == modo.lower()
        return True  # Si no hay M/A/S en el ID, no hay error    

    # Aplicamos la función a cada fila
    errores = df[~df.apply(validar_fila, axis=1)]
    errores.to_excel("hhh.xlsx")

    if errores.empty:
        return True, ""
    else:
        return False, f"Se han encontrado las siguientes inconsistencias entre el responsable de ejecutar el control y el modo de ejecución: {errores}"