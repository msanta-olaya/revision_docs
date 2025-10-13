"""
Módulo principal

Este módulo contiene la función `main` que ejecuta todos los controles sobre los tres documentos: Población críticos, Inventario de controles consolidado, Seguimiento de direcciones.
"""

import pandas as pd
from src.ctrl_cross import comprobar_vacios, valores_permitidos, comprobar_resp_fun
from src.ctrl_pob_crit import conceptos_duplicados, buscar_componentes
from src.ctrl_inventario import len_id, formato_id_modoejec, formato_id_tipoctrl, comprobar_ids_repetidos, comprobar_concepto_pob_crit, valores_resp_ejecutar

## VARIABLES GLOBALES
arr_columnas_resp_funcional = ['DIRECCIÓN RESPONSABLE', 'ÁREA RESPONSABLE', 'OFICINA RESPONSABLE']
arr_columna_id_repetidos = ['CONCEPTO DEDUCIDO DEL INFORME', 'RESPONSABLE DE EJECUTAR EL CONTROL', 'TIPO DE CONTROL', 'DEFINICIÓN DEL CONTROL']

dic_resp_funcionales = {'Maria Jose Samper':'8920 - DIRECCIÓN GENERAL FINANCIERA9460 - PROYECCIÓN Y SEGUIMIENTO FINANCIERO9275 - PRESUPUESTACIÓN FINANCIERA',
                        'Manuel Hernandez García':'8782 - DIRECCIÓN DE MERCADOS FINANCIEROS8595 - TESORERÍA Y MERCADO DE CAPITALES8569 - TITULIZACIÓN',
                        'Maria de la Paz Montalvo Garcia - Estrada':'8087 - DIRECCIÓN DE CONTROL DE RIESGOS8085 - CONTROL DEL RIESGO DE CRÉDITO, INMOBILIARIO Y ASG9035 - CONTROL DEL RIESGO DE CRÉDITO E INMOBILIARIO',
                        'Emilio Joaquín Sánchez Sánchez':'8786 - DIRECCIÓN DE PLANIFICACIÓN FINANCIERA Y SUPERVISIÓN8653 - SOLVENCIA8769 - PLANIFICACIÓN DE CAPITAL',
                        'Enrique Díaz':'8782 - DIRECCIÓN DE MERCADOS FINANCIEROS8908 - GESTIÓN DE RIESGO DE LIQUIDEZ',
                        'Juan Antonio Capel Cesar':'8934 - SUBDIRECCIÓN GENERAL DE INVERSIONES8713 - RECUPERACIÓN AMISTOSA Y GESTIÓN DEL VENCIDO8715 - SISTEMÁTICA DE GESTIÓN DE RECUPERACIÓN',
                        'Maria Isabel Torrente Miras':'8900 - CONSEJO RECTOR PRESIDENTE7979 - SECRETARÍA INSTITUCIONAL',
                        'Rosario Carrillo Sánchez':'8786 - DIRECCIÓN DE PLANIFICACIÓN FINANCIERA Y SUPERVISIÓN9460 - SEGUIMIENTO PRESUPUESTARIO9265 - ESTUDIOS Y SEGUIMIENTO PRESUPUESTARIO',
                        'Myriam Rico Sandoval':'8412 - SUBDIRECCIÓN GENERAL DE SOSTENIBILIDAD Y DESARROLLO AGROALIMENTARIO8410 - SOSTENIBILIDAD8413 - FINANZAS SOSTENIBLES',
                        'Lorenzo Hernandez Martinez':'8782 - DIRECCIÓN DE MERCADOS FINANCIEROS8787 - GESTIÓN DE BALANCE',
                        'Francisco Palomero Flores':'8934 - SUBDIRECCIÓN GENERAL DE INVERSIONES8934 - SUBDIRECCIÓN GENERAL DE INVERSIONES9018 - STAFF DE SISTEMÁTICA Y SOPORTE CORPORATIVO',
                        'Marta López Infante':'8786 - DIRECCIÓN DE PLANIFICACIÓN FINANCIERA Y SUPERVISIÓN8653 - SOLVENCIA8578 - INFORMACIÓN DE SOLVENCIA',
                        'Francisco Andrés Arenas':'8083 - DIRECCIÓN DE DESARROLLO DE NEGOCIO8995 - INFORMACIÓN DE NEGOCIO9283 - INFORMACIÓN COMERCIAL',
                        'Isidro Clemot':'8934 - SUBDIRECCIÓN GENERAL DE INVERSIONES8713 - RECUPERACIÓN AMISTOSA Y GESTIÓN DEL VENCIDO8715 - SISTEMÁTICA DE GESTIÓN DE RECUPERACIÓN',
                        'Adelina Pastor Beguer':'8087 - DIRECCIÓN DE CONTROL DE RIESGOS8710 - VALIDACIÓN, REPORTE DE RIESGOS Y RDA8691 - REPORTE DE RIESGOS Y RDA',
                        'Guillermo Conesa García':'9470 - CIBER RESILIENCIA9471 - RIESGO Y CONTROL TECNOLÓGICO9476 - RIESGO TECNOLÓGICO',
                        'Tamara Aguirre Felices':'8920 - DIRECCIÓN GENERAL FINANCIERA9051 - INFORMACIÓN FINANCIERA9056 - REPORTE EE.FF. Y CONSOLIDADOS',
                        'Juan Andrés Rodríguez Pardo':'8087 - DIRECCIÓN DE CONTROL DE RIESGOS8075 - CONTROL DE OTROS RIESGOS DE BALANCE9670 - CONTROL DEL RIESGO OPERACIONAL',
                        'Jose Luis Alcazar Hernandez':'8083 - DIRECCIÓN DE DESARROLLO DE NEGOCIO8995 - INFORMACIÓN DE NEGOCIO9285 - SEGUIMIENTO DE GESTIÓN',
                        'Oscar Perals Hernández':'8083 - DIRECCIÓN DE DESARROLLO DE NEGOCIO8995 - INFORMACIÓN DE NEGOCIO',
                        'Diego Jesús Contreras Gonzalez':'8934 - SUBDIRECCIÓN GENERAL DE INVERSIONES9016 - SEGUIMIENTO ACTIVO DE LA CARTERA DE INVERSIONES8937 - ANALÍTICA Y MEDICIÓN DEL RIESGO DE CRÉDITO',
                        'Antonio Ramos Invernón':'8770 - DIRECCIÓN DE MODELOS AVANZADOS9620 - MODELOS DE RIESGO DE CRÉDITO 8704 - PARÁMETROS DE RIESGOS',
                        'Sandra Avellaneda':'8551 - DIRECCIÓN CONTABLE Y FISCAL8212 - CONTROL CONTABLE7941 - CONTROL DE INFORMACIÓN FINANCIERA',
                        'Begoña Abad Morales':'8913 - DIRECCIÓN GENERAL DE NEGOCIO8700 - STAFF DE NEGOCIO Y EXPERIENCIA DE CLIENTE',
                        'Soraya Gongora Ruano':'8913 - DIRECCIÓN GENERAL DE NEGOCIO8700 - STAFF DE NEGOCIO Y EXPERIENCIA DE CLIENTE',
                        'Maria Carmen Navarro LLorens':'8181 - Dirección General Sunaria Capital S.L.U.8179 - Valoración y Control de Participaciones Empresariales',
                        'Francisco Palomero Flores':'8934 - SUBDIRECCIÓN GENERAL DE INVERSIONES9018 - STAFF DE SISTEMÁTICA Y SOPORTE CORPORATIVO',
                        'Arturo López Moreno':'8782 - DIRECCIÓN DE MERCADOS FINANCIEROS8595 - TESORERÍA Y MERCADO DE CAPITALES8676 - TESORERÍA',
                        'Laura Stephany Zwijnenberg':'8782 - DIRECCIÓN DE MERCADOS FINANCIEROS8060 - RELACIONES CON INVERSORES',
                        'Laura Martín Valverde':'8770 - DIRECCIÓN DE MODELOS AVANZADOS9620 - MODELOS DE RIESGO DE CRÉDITO 8703 - SCORING Y RATING',
                        'Mº Carmen Palomino García':'8056 - COMERCIAL Y ECONOMÍA SOCIAL8056 - COMERCIAL Y ECONOMÍA SOCIAL',
                        'Laura Sanchez Díaz':'8550 - DIRECCIÓN DE CUMPLIMIENTO NORMATIVO8588 - SERVICIO DE ATENCIÓN AL CLIENTE8784 - ADMINISTRACIÓN Y CONTROL',
                        'Lidia Moreno Ruiz':'8550 - DIRECCIÓN DE CUMPLIMIENTO NORMATIVO9687 - PREVENCIÓN DEL BLANQUEO DE CAPITALES Y DE LA FINANCIACIÓN DEL TERRORISMO (UPBCFT)8750 - PROCEDIMIENTOS, siSTEMAS Y RIESGOS',
                        'José Manuel Cano':'8087 - DIRECCIÓN DE CONTROL DE RIESGOS8075 - CONTROL DE OTROS RIESGOS DE BALANCE',
                        'Alfonso Fernandez Guiard':'8920 - DIRECCIÓN GENERAL FINANCIERA8212 - CONTROL CONTABLE',
                        'Laura Novis Saiz':'8940 - DIRECCIÓN DE PERSONAS8161 - Estructura y Analítica8719 - Procesos y Analítica',
                        'Anabel Gilabert Gilabert':'8087 - DIRECCIÓN DE CONTROL DE RIESGOS8084 - CULTURA DEL RIESGO Y CONTROL DE RIESGOS ASG8781 - Control de Riesgos ASG',
                        'Pedro Jesús García Pedrosa':'8087 - DIRECCIÓN DE CONTROL DE RIESGOS8084 - MARCO DE CONTROL DE RIESGOS8663 - PROPENSIÓN AL RIESGO'}

val_per_informe = ['ICAAP', 'Indicadores de actividad', 'Informe 360', 'Informe de Control al Comité de Riesgos', 'Informe Producción Nivel Agregado ', 'ISPAMAR', 'IRP', 'ISAD', 'Mercados', 'Modelos', 'RAF']
val_per_tipodato = ['Fecha', 'Importes', 'Valor numérico / alfa-numérico']
val_per_tipoctrl = ['Completitud', 'Completitud en procesos', 'Unicidad', 'Valores permitidos', 'Formato', 'Razonabilidad', 'Coherencia funcional', 'Exactitud', 'Conciliación contable', 'Reconciliación origen-destino', 'Consistencia entre fuentes', 'Puntualidad']
val_per_modoeje = ['Manual', 'Automático', 'Asegurado por sistema']
val_per_tipoconcepto = ['Métrica', 'Indicador', 'Concepto subyacente', 'Eje de estudio']

## MAIN
def main():
    # Cargar DataFrame desde Excel
    df_pob_crit = pd.read_excel('data/Inventario consolidado.xlsx', sheet_name='Población Críticos')
    df_inv_ctrls = pd.read_excel('data/Inventario consolidado.xlsx', sheet_name='Inventario Controles_Consolidad', header=2)
    df_seg_dir = pd.read_excel('data/Seguimiento direcciones.xlsx', sheet_name='Seguimiento')

    # DataFrame para guardar errores
    resultados = pd.DataFrame(columns=['Archivo', 'Columna', 'Mensaje de error', 'Resultado'])

    resultado, mensaje = comprobar_vacios(df_pob_crit, 'RESPONSABLE FUNCIONAL')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['RESPONSABLE FUNCIONAL'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_resp_fun(df_pob_crit, 'RESPONSABLE FUNCIONAL', arr_columnas_resp_funcional, dic_resp_funcionales)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['RESPONSABLE FUNCIONAL'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_resp_fun(df_inv_ctrls, 'RESPONSABLE FUNCIONAL', arr_columnas_resp_funcional, dic_resp_funcionales)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['RESPONSABLE FUNCIONAL'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_pob_crit, 'INFORME')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)


    resultado, mensaje = valores_permitidos(df_pob_crit, 'INFORME', val_per_informe)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = valores_permitidos(df_inv_ctrls, 'INFORME', val_per_informe)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_inv_ctrls, 'INFORME')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_pob_crit, 'CONCEPTO DEDUCIDO DEL INFORME')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['CONCEPTO DEDUCIDO DEL INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    columnas_concat = ["INFORME", "CONCEPTO DEDUCIDO DEL INFORME"]
    resultado, mensaje = conceptos_duplicados(df_pob_crit, columnas_concat)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['CONCEPTO DEDUCIDO DEL INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_pob_crit, 'TIPO DE DATO')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['TIPO DE DATO'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = valores_permitidos(df_pob_crit, 'TIPO DE DATO', val_per_tipodato)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['TIPO DE DATO'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = buscar_componentes(df_pob_crit, 'COMPONENTES', 'CONCEPTO DEDUCIDO DEL INFORME')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['COMPONENTES'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_pob_crit, 'MÉTRICA EN INFORME')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['MÉTRICA EN INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = valores_permitidos(df_pob_crit, 'MÉTRICA EN INFORME', ['SI', 'NO'])
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['MÉTRICA EN INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_pob_crit, 'TIPO DE CONCEPTO')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['TIPO DE CONCEPTO'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = valores_permitidos(df_pob_crit, 'TIPO DE CONCEPTO', val_per_tipoconcepto)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['TIPO DE CONCEPTO'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_pob_crit, 'CRITICIDAD')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['CRITICIDAD'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = valores_permitidos(df_pob_crit, 'CRITICIDAD', ['SI', 'NO'])
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Población críticos'],
            'Columna': ['CRITICIDAD'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_inv_ctrls, 'ID CONTROLES')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['ID CONTROLES'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)
    
    resultado, mensaje = len_id(df_inv_ctrls, 'ID CONTROLES')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['ID CONTROLES'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = formato_id_modoejec(df_inv_ctrls, 'ID CONTROLES', 'MODO DE EJECUCIÓN')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['ID CONTROLES'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = formato_id_tipoctrl(df_inv_ctrls, 'ID CONTROLES', 'TIPO DE CONTROL')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['ID CONTROLES'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_ids_repetidos(df_inv_ctrls, 'ID CONTROLES', 'INFORME', arr_columna_id_repetidos)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['ID CONTROLES'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_inv_ctrls, 'CONCEPTO DEDUCIDO DEL INFORME')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['CONCEPTO DEDUCIDO DEL INFORME'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    # resultado, mensaje = comprobar_concepto_pob_crit(df_pob_crit, df_inv_ctrls, 'CONCEPTO DEDUCIDO DEL INFORME', 'CONCEPTO DEDUCIDO DEL INFORME')
    # resultados = pd.concat([
    #     resultados,
    #     pd.DataFrame({
    #         'Archivo': ['Inventario controles'],
    #         'Columna': ['CONCEPTO DEDUCIDO DEL INFORME'],
    #         'Mensaje de error': [mensaje],
    #         'Resultado': [resultado]
    #     })
    # ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_inv_ctrls, 'RESPONSABLE DE EJECUTAR EL CONTROL')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['RESPONSABLE DE EJECUTAR EL CONTROL'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = valores_resp_ejecutar(df_inv_ctrls, 'RESPONSABLE DE EJECUTAR EL CONTROL', 'MODO DE EJECUCIÓN')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['RESPONSABLE DE EJECUTAR EL CONTROL'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_inv_ctrls, 'TIPO DE CONTROL')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['TIPO DE CONTROL'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = valores_permitidos(df_inv_ctrls, 'TIPO DE CONTROL', val_per_tipoctrl)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['TIPO DE CONTROL'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = comprobar_vacios(df_inv_ctrls, 'MODO DE EJECUCIÓN')
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['MODO DE EJECUCIÓN'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    resultado, mensaje = valores_permitidos(df_inv_ctrls, 'MODO DE EJECUCIÓN', val_per_modoeje)
    resultados = pd.concat([
        resultados,
        pd.DataFrame({
            'Archivo': ['Inventario controles'],
            'Columna': ['MODO DE EJECUCIÓN'],
            'Mensaje de error': [mensaje],
            'Resultado': [resultado]
        })
    ], ignore_index=True)

    # ===== FILTRAR SOLO LOS ERRORES (Resultado == False) =====
    # errores_df = resultados[resultados['Resultado'] == False].drop(columns=['Resultado'])
    errores_df = resultados
    # Guardar en Excel solo si hay errores
    if not errores_df.empty:
        errores_df.to_excel('errores.xlsx', index=False)
        print("Se encontraron errores. Revisar 'errores.xlsx'.")
    else:
        print("No se encontraron errores en los controles ejecutados.")

if __name__ == "__main__":
    main()