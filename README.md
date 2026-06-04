# retail-sales-analysis
**Analisis y Prediccion de ventas de una tienda retail**

Este proyecto tiene como objetivo analizar el comporatamiento de las ventas de una tienda retail mediante tecnicas de analisis exploratorio de los datos (EDA) y Machine Learning.
Se desarrollo un proceso completo de ciencia de datos que incluyo limpieza de datos, visualizacion, transformacion de variables, construccion de pipelines y entrenamiento de modelos de clasificacion para predicir el nivel de ventas de una transaccion (Baja, Media o Alta).
La importancia de este proyecto radica en la identificacion de patrones de compra y en la aplicacion de modelos predictivos que permitan apoyar la toma de decisiones basada en datos.

## Estructura del Proyecto

retail-sales-analysis/
|-- /data
| |-- retail_sales_dataset.csv
|-- /notebooks
| |-- Proyecto 1 Part 2.py
| |-- Proyecto 1 Part 3.ipynb
| |-- Proyecto 1 Part 4.ipynb
| |-- Proyecto 1 Part 5.ipynb
| |-- Proyecto 1 Part final.ipynb
|-- /presentacion
| |-- Proyecto 1 parte final.pptx
|-- /src
| |-- cargar_datos.py
|-- README.md

Contenido de las carpetas
- `data/`: Contiene los archivos de datos.
- `notebooks/`: Contiene los notebooks de este proyecto con el analisis exploratorio, preprocesamiento y modelado.
- `presentacion/`: Incluye PPT One-Page
- `src/`: Contiene el código fuente del proyecto.
- `README.md`: Este archivo.

## Tecnicas utilizadas

Exploracion de datos (EDA)
- Estadistica descriptiva.
- Analisis de valores nulos.
- Deteccion de valores atipicos.
- Visualizacion de distribuciones.
- Analisis de correlacion.

Preprocesamiento
- Tratamiento de valores faltantes.
- Codificacion de variables categoricas mediante OneHotEncoder.
- Escalamiento de variables numericas mediante StandardScaler.
- Automatizacion mediante ColumnTransformer y Pipeline.

Modelos de Machine Learning
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest

Metricas de evaluacion
- Accuracy
- Precision
- Recall
- F1-Score
- Matriz de confusion

## Instrucciones de Instalación

1. Clona el repositorio: `git clone https://github.com/tu_usuario/retail-sales-analysis.git`
2. Acceder al directorio: cd retail-sales-analysis
3. Instala las dependencias: `pip install -r requirements.txt`
4. Ejecutar el notebook: Abrir Jupyter Notebook o Visual Studio Code y ejecutar:
   Ejecutar las celdas en orden para reproducir completamente el analisis y los resultados.

## Resultados Principales

El modelo con mejor desempeño fue Random Forest, obteniendo el mayor Accuracy y F1-Score entre los modelos evaluados.
Las variables utilizadas permitieron identificar patrones asociados al nivel de ventas, aunque aun existen oportunidades de mejora incorporando nuevas caracteristicas relacionadas con el comportamiento de compra.

## Autor

Carla Bermudez Fuentes - Desarrollo de analisis, modelado y documentacion del proyecto.

## Licencia

Este proyecto fue desarrollado con fines academicos y educativos.
Su contenido se comparte unicamente con fines de aprendizaje y evaluacion.
