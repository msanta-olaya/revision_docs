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

### **Controles cross**
- Completitud: asegurar que no hay vacíos

### **Controles sobre la población de críticos**
- Informes: asegurar que no hay vacíos

### **Controles sobre el inventario de controles**
- Informes: asegurar que no hay vacíos

### **Controles sobre el seguimiento de direcciones**
- Informes: asegurar que no hay vacíos

---

## **Verificación de Estilo con `pylint`**

Para verificar que el proyecto cumple con la guía de estilo PEP8, ejecuta el siguiente comando:

```bash
python -m pylint mayn.py
python -m pylint src/
python -m pylint tests/
```