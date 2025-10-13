"""
Módulo principal

Este módulo contiene la función `main` que ejecuta todos los controles sobre los tres documentos: Población críticos, Inventario de controles consolidado, Seguimiento de direcciones.
"""

import pandas as pd
from src.ctrl_cross import comprobar_vacios

def main():
    # Cargar DataFrame desde CSV
    df = pd.read_excel('data/población de críticos.xlsx', sheet_name='Población críticos')

    # DataFrame para guardar errores
    resultados = pd.DataFrame(columns=['Archivo', 'Columna', 'Mensaje de error', 'Resultado'])

    resultado, mensaje = comprobar_vacios(df, 'INFORME')
    print(resultado, mensaje)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df, 'NOMBRE DEL CONCEPTO')
    print(resultado, mensaje)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    # ===== FILTRAR SOLO LOS ERRORES (Resultado == False) =====
    errores_df = resultados[resultados['Resultado'] == False].drop(columns=['Resultado'])

    # Guardar en Excel solo si hay errores
    if not errores_df.empty:
        errores_df.to_excel('errores.xlsx', index=False)
        print("⚠️ Se encontraron errores. Revisar 'errores.xlsx'.")
    else:
        print("✅ No se encontraron errores en los controles ejecutados.")

if __name__ == "__main__":
    main()