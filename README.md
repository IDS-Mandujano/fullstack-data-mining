Aquí tienes el código exacto, listo para copiar y pegar directamente en tu archivo `README.md`:

```markdown
# Pipeline Full Stack de Minería de Datos: Tasador Inmobiliario (Dubai Real Estate)

**Universidad Politécnica de Chiapas (UPChiapas)** **Ingeniería de Software - 9.º Cuatrimestre (2026A)** **Autor:** Jesús Eduardo Gutiérrez Mandujano (Matrícula: 233325)  
**Profesor:** Mtro. Ramsés Camas Nájera  

---

## 📌 Descripción del Proyecto
Este proyecto es un sistema Full Stack de Minería de Datos que analiza y predice el comportamiento del mercado inmobiliario secundario en Dubai. El sistema implementa un ciclo de vida de datos completo (proceso KDD): desde la ingesta y preprocesamiento de los datos, pasando por el almacenamiento analítico en un Data Warehouse, hasta la inferencia en vivo mediante modelos de Machine Learning desplegados a través de una API REST y consumidos por una interfaz web.

## 🏗️ Arquitectura del Sistema
El proyecto está dividido en cuatro capas principales:
1. **Capa de Datos:** `secondary_sales.csv` (Kaggle).
2. **Capa de Almacenamiento (OLAP):** Base de datos analítica embebida con `DuckDB` (`warehouse.db`).
3. **Capa de Modelado (ML):** Preprocesamiento sin fuga de datos y entrenamiento de modelos `Ridge` (Regresión) y `LogisticRegression` (Clasificación) usando `scikit-learn`.
4. **Capa de Presentación:** Backend construido en `Flask` y Frontend desarrollado en HTML/CSS/Vanilla JS.

---

## 📁 Estructura del Repositorio
```text
proyecto-fullstack-data-mining-233325-gutierrez-mandujano/
│
├── data/
│   └── secondary_sales.csv           # Dataset original descargado de Kaggle
│
├── notebooks/
│   └── pipeline.ipynb                # Jupyter Notebook con el EDA, preprocesamiento y entrenamiento
│
├── backend/
│   ├── app.py                        # API REST construida con Flask
│   ├── warehouse.db                  # Data Warehouse generado por DuckDB (OLAP)
│   ├── modelo_regresion.pkl          # Modelo entrenado (Ridge) serializado
│   └── modelo_clasificacion.pkl      # Modelo entrenado (LogReg) serializado
│
├── frontend/
│   └── index.html                    # Interfaz de usuario final
│
├── AI_USAGE.md                       # Declaración de uso de Inteligencia Artificial
└── README.md                         # Documentación del proyecto

```

---

## 🚀 Instrucciones de Reproducción y Ejecución

Para evaluar este proyecto en un entorno de desarrollo como Ubuntu, sigue estos pasos desde una terminal.

### 1. Preparar el Entorno Virtual

Asegúrate de tener Python 3 instalado. Crea y activa tu entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate

```

### 2. Instalar Dependencias

Instala las librerías necesarias para correr tanto los modelos matemáticos como el servidor web:

```bash
pip install pandas scikit-learn duckdb flask flask-cors joblib jupyter ipykernel

```

### 3. Ejecutar el Pipeline de Minería de Datos (Generación de Modelos)

*Nota: Los archivos `.db` y `.pkl` ya vienen incluidos en el repositorio, pero si deseas recrearlos desde cero:*

1. Abre el archivo `notebooks/pipeline.ipynb` en tu editor.
2. Asegúrate de seleccionar el kernel del entorno virtual (`venv`).
3. Ejecuta todas las celdas. Esto procesará el CSV, generará la base de datos `warehouse.db` y exportará los archivos `modelo_regresion.pkl` y `modelo_clasificacion.pkl` en la carpeta `backend/`.

### 4. Levantar la API (Backend)

Inicia el servidor de Flask para exponer los endpoints de inferencia y OLAP:

```bash
cd backend
python3 app.py

```

El servidor comenzará a escuchar en `http://127.0.0.1:5000`. **No cierres esta terminal.**

### 5. Iniciar la Aplicación (Frontend)

Con el servidor Flask corriendo de fondo, abre el explorador de archivos, dirígete a la carpeta `frontend/` y abre el archivo `index.html` en tu navegador web.

* Haz clic en **Consultar Data Warehouse** para verificar la conexión OLAP con DuckDB.
* Captura datos en el formulario y haz clic en **Calcular Precio y Zona** para realizar inferencias en vivo con los modelos de Machine Learning.