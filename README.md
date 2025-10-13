# Verificación de documentos

## **Descripción del Proyecto**
Este proyecto tiene como objetivo garantizar la correctitud de los tres documentos utilizados para obtener los KPIs: Población de críticos, Inventario de controles consolidado, Seguimiento de direcciones.

---

## **Estructura del Proyecto**
```
/Calidad_documentos
│
├── /data
│   ├── Inventario_consolidado.xlsx
│   ├── Seguimiento_direcciones.clsx
│
├── /src
│   ├── ctrl_cross.py
│   ├── ctrl_pob_crit.py
│   ├── ctrl_inventario.py
│   ├── ctrl_seguimiento.py
│
├── /tests
│
├── README.md
├── requirements.txt
├── LICENSE
└── main.py
```

---

## **Instalación**
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado (versión 3.7 o superior).
3. Instala las dependencias requeridas:

```bash
pip install -r requirements.txt
```

## **Uso del Proyecto**
El archivo principal para ejecutar el proyecto es `main.py`. Como resultado de ejecutar el main se obtiene un excel con el detalle de los errores encontrados en cada archivo.
Para ejecutar el proyecto utiliza el siguiente comando:


### **Comandos para ejecutar:**
```bash
python main.py
```

## **Descripción de los controles**

### **Controles sobre la población de críticos**
- Responsable funcional: No puede estar vacío. Todos los responsables tienen que tener su dirección, área y oficina bien. Si es TBD el RF, que todo sea TBD
- Informe: No puede estar vacío. Debe ser un valor dentro de los 11 informes que tenemos
- Concepto deducido del informe: No puede estar vacío. Haciendo el concat informe-concepto deducido del informe no puede haber duplicados
- Tipo de dato: No puede estar vacío. Tiene que tener un valor dentro de Fecha, Importes, Valor numérico / alfa-numérico
- Componentes: 
    - Todos los componentes tienen que estar levantados en la columna concepto deducido del informe
    - Si componentes esta relleno, para ese registro la fórmula tiene que estar informada, y los componentes deben estar dentro del string de la fórmula

### **Controles sobre el inventario de controles**
- Informes: No puede estar vacío. Debe ser un valor dentro de los 11 informes que tenemos
- ID controles: 
    - No puede estar vacío
    - No puede tener una longitud mayor de 15
    - Si en el ID hay M/A/S asegurar que se corresponde con la columna Modo de ejecución
    - Si en el ID hay N1/N2/N3/N4 asegurar que se corresponde con la columna Tipo de control
    - Haciendo el concat Concepto deducido del informe-Responsable de ejecutar el control-Tipo de control-Definición del control, todos los registros que tengan ese mismo concat con Informe diferente tienen que tener el mismo ID
- Concepto deducido del informe: No puede estar vacío. Confirmar que está incluido en la población de críticos
- Tipo de concepto: 
    - No puede estar vacío. El concat informe-concepto deducido del informe tiene que tener el mismo tipo de concepto que la población de críticos
- Responsable funcional: Confirmar que el concat de Informe-Concepto deducido del informe tiene asociado el mismo responsable funcional con la misma dirección area y oficina que en la población de críticos
- Responsable de ejecutar el control: 
    - No puede estar vacío
    - Si el modo de ejecución es Automático, el Responsable de ejecutar el control tiene que ser Calidad/Tecnología
    - Si el modo de ejecución es Asegurado por sistema, el Responsable de ejecutar el control tiene que ser N/A
- Tipo de control: No puede estar vacío. Tiene que tener uno de los valores permitidos por la matriz de suficiencia
- Modo de ejecución: No puede estar vacío. Tiene que tener uno de los valores permitidos.

### **Controles sobre el seguimiento de direcciones**
- Número de métricas / indicadores: debe coincidir el número por responsable con el de la población de críticos
- Número total de datos: debe coincidir el número por responsable con el de la población de críticos
- Controles levantados: debe coincidir el número de controles por responsable con el de la población de críticos filtrando por control nuevo = No
- Análisis de suficiencia realizado: no puede ser mayor que el valor de la columna 'Número de métricas / indicadores'
- Nuevos controles a implantar: debe coincidir filtrando por responsable con el número de nuevos controles en el inventario
- Resultado de controles preexistentes analizados: el dato no puede ser mayor a la suma de las columnas 'Nuevos controles a implantar' y 'Controles levantados'

---

## **Verificación de Estilo con `pylint`**

Para verificar que el proyecto cumple con la guía de estilo PEP8, ejecuta el siguiente comando:

```bash
python -m pylint mayn.py
python -m pylint src/
python -m pylint tests/
```