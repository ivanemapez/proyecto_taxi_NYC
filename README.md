
<div style="position: relative; height: 300px;">
  <!-- Imagen inferior derecha -->
  <img src="LogoTaxiCom.png" alt="Imagen Derecha" style="position: absolute; bottom: 0; right: 0; width: 150px; height: auto;">
  <!-- Imagen inferior izquierda (20% más grande) -->
  <img src="LogoConsultora.jpg" alt="Imagen Izquierda" style="position: absolute; bottom: 0; left: 0; width: 420px; height: auto;">
</div>


# Demo 1. Presentación y propuesta de trabajo en base al negocio.
## Introducción
Somos una consultora de Data Science enfocada en el análisis estadístico de datos, desarrollo de modelos de machine learning y visualizaciones gráficas.

Consultora data se enfoca en establecer objetivos de negocios para obtener así estrategias que promuevan la optimización de rendimientos a corto, mediano y largo plazo, como también mostrar propuestas de mejora mediante el uso de modelos predictivos y visualizaciones. 

Nuestra consultora cuenta con un board, el cual está encargado de abordar los proyectos y negocios. 

Para garantizar la excelencia en nuestros servicios, nuestro equipo está compuesto por especialistas con roles claramente definidos, que abordarán los objetivos propuestos por la empresa:
- Analista de Datos: Julian Ariel Burastero, Francisco Fajardo
Responsable de la limpieza, integración y preprocesamiento de datasets.
- Especialista en Visualización de Datos: Julian Ariel Burastero,
Diseña dashboards interactivos, mapas de calor y gráficos que transforman datos complejos en información comprensible para los clientes.
- Ingeniero de Machine Learning: Gabriel Arturo Monzon Luna, Jerónimo Martinez
Desarrolla modelos predictivos y optimiza algoritmos para correlaciones clave 
- Data Engineer: Ivan Lopez-Francisco Fajardo
Diseñar, desarrollar y mantener sistemas que procesan grandes cantidades de datos (Big Data), a través de base de datos relacionales y no relacionales, o en la nube.
- Gerente de Proyecto: Jerónimo Martinez
Coordina las tareas del equipo, gestiona los entregables y asegura 
la alineación con los objetivos del cliente.

## Contexto del negocio
Taxicom 2.0 es una empresa de taxis estadounidense que quiere expandir su negocio en la ciudad de New York para el segundo semestre de 2025. La empresa es consciente de que la tecnología y la ciencia de datos es crucial para la supervivencia y éxito de dicho proyecto frente a la competencia y las demandas sociales. Para ello Taxicom 2.0 decide contratar a nuestra consultora a fin de emplear nuestros servicios en base a sus objetivos. 

- Objetivos de negocio
Optimizar la logística y operación del transporte mediante análisis detallado de patrones de movilidad.
Evaluar el impacto ambiental del transporte y proponer soluciones hacia una transición sostenible.
Mejorar la experiencia del cliente identificando puntos críticos como tiempo, costo, y satisfacción (propinas).
Generar estrategias económicas basadas en la elasticidad de demanda, precios y eficiencia operativa.
- Servicios requeridos de la empresa TaxiCom 2.0

La empresa Taxicom 2.0 se dispone a contratar un conjunto de servicios personalizados en base a sus objetivos:  

+ Análisis de Demanda y Logística:
	- Identificación de zonas y horarios de alta demanda.
	- Optimización de rutas basadas en patrones de congestión y tiempo promedio de viaje.
	- Mapas dinámicos para la planificación de horarios pico.
+ Monitoreo de Impacto Ambiental:
	- Modelos predictivos que correlacionen calidad del aire (AQI) con cantidad de viajes.
	- Evaluación de la transición a vehículos eléctricos comparando emisiones y costos operativos.
+ Estudios de Satisfacción del Cliente:
	- Análisis de propinas promedio por zona como indicador de calidad.
	- Propuestas para implementar soluciones tecnológicas (pagos digitales, apps).

## Análisis Exploratorio de los datos (EDA)

El EDA se realizó en base a los dataset provistos por la empresa y en base a los que visualizamos como relevantes para el negocio. Cada link que se ve a continuación abre el EDA de cada data set trabajado y analizado:
- AlternativeFuelVehicleUS
- Air_quality.csv
- sensores 22-24.csv
- ElectricCarData_Norm
- FuelEconomy
- Lighr duty vehicles
- taxis_amarillos
- taxis_verdes
- Zonastaxi

## KPI propuestos a la empresa

Un KPI es un indicador clave de desempeño, es decir, es una métrica utilizada para medir y evaluar el rendimiento de una actividad, proceso o estrategia en relación con un objetivo específico en el tiempo. En base a estos indicadores la empresa puede tomar decisiones y monitorear los procesos. 

1. Inclusión de autos eléctricos. 
El KPI en este caso mide el progreso en la inclusión de autos eléctricos en función de un objetivo predeterminado (por defecto, 1000 autos). El cálculo genera un porcentaje que permite visualizar cuánto se ha avanzado hacia la meta.

	- Fórmula del KPI para el cliente:
	Progreso de Inclusión (%) = (Número de autos eléctricos integrados/ objetivo total de autos eléctricos) x 100

	- Explicación para el cliente:
	Número de autos eléctricos integrados: Es el número actual de autos eléctricos incorporados en la flota.
	Objetivo total de autos eléctricos: Es la meta establecida para integrar autos eléctricos, por defecto 1000.
	El resultado se expresa en porcentaje, mostrando cuánto se ha avanzado hacia el objetivo.

2. Reducir las Emisiones de CO2 en un 10%
Este KPI mide el progreso hacia el objetivo de reducir las emisiones de CO2 en un 10% respecto a su valor inicial. Permite evaluar si las estrategias implementadas para reducir emisiones son efectivas y cuán cerca estamos de alcanzar la meta.

	- Fórmula para el cliente:
	Reducción de CO2 (%) =  (Emisiones iniciales - Emisiones actuales/emisiones iniciales) x 100

	- Componentes de la Fórmula:
	Emisiones iniciales: El nivel de emisiones de CO2 antes de implementar las estrategias de reducción.
	Emisiones actuales: El nivel de emisiones de CO2 después de implementar las estrategias.
	El resultado expresa el porcentaje de reducción logrado respecto al valor inicial.

3. Reducción de Tiempo Muerto (%)
Este KPI mide el progreso en la reducción del tiempo muerto (o inactivo) de los taxis, es decir, el tiempo que pasan sin pasajeros mientras esperan una solicitud. Es clave para optimizar la operación y la rentabilidad del servicio, así como para disminuir el impacto ambiental.

	- Fórmula para el cliente:
	Reducción de tiempo muerto = (Tiempo muerto inicial- Tiempo muerto actual / Tiempo muerto inicial) x 100

	- Componentes de la Fórmula:
	Tiempo muerto inicial: El tiempo promedio que los taxis pasan inactivos por turno antes de implementar mejoras (en minutos u horas).
	Tiempo muerto actual: El tiempo promedio que los taxis pasan inactivos por turno después de implementar mejoras.
	Resultado: Indica en porcentaje cuánto se ha reducido el tiempo muerto respecto al punto de partida.

4. Aumentar los ingresos de pasajeros en un 2% de taxis amarillos
Objetivo: Incrementar los ingresos totales generados por los viajes en un 2% en el próximo trimestre.

	- Fórmula:  (Ingresos actuales - Ingresos previos / Ingresos previos) × 100 

	- Medición:
	Ingresos actuales: Total de la columna total_amount para el período actual.
	Ingresos previos: Total de la columna total_amount para el período de comparación (mes o trimestre anterior).

5. Reducir la duración promedio de los viajes en un 5% de taxis amarillos
Objetivo: Disminuir la duración promedio de los trayectos para mejorar la eficiencia operativa y reducir el tiempo muerto.

	- Fórmula:(Duración previa - Duración actual) / Duracioón previa×100

	- Medición:
	Duración promedio previa: Promedio de la diferencia entre tpep_pickup_datetime y tpep_dropoff_datetime para el período anterior.
	Duración promedio actual: Promedio de la misma métrica para el período actual.


6. Incrementar la ocupación promedio de pasajeros en un 3% de taxis amarillos
Objetivo: Aumentar el número promedio de pasajeros por viaje en un 3% para maximizar la capacidad utilizada.

	- Fórmula:(Ocupación actual - Ocupación previa) / Ocupación previa×100

	- Medición:
		Ocupación promedio actual: Promedio de la columna passenger_count en el período actual.
		Ocupación promedio previa: Promedio de la misma columna en el período anterior.


## Entregables

La consultora se prone entregar a Taxicom los siguientes servicios
- Carga incremental de datos en la nube de Google (Google cloud). 
- Dashboard interactivo con metricas y gráficos: KPI y los resultados obtenidos mediante la aplicaciónmachine learning.
- APIs: Sistemas de recomendación de zonas para taxis en base a la demanda de clientes.  


# Demo 2. Carga de los datos  en la nube y posibles implementaciones de Machine learning y visualización. 

Esta segunda reunión con nuestro cliente Taxicom 2.0 tiene el objetivo de mostrar:
1. Los avances en cuanto a la extracción, tranformación y carga (ETL) de los datos (Video).
	- Interfaz de carga para el usuario
	- Carga de los mismos datos a la nube (Google Cloud)
	- Tratamiento de los datos: tranformaciones.
	- Posible carga incremental de datos. 
	- Datos preparados para implementaciones.
2. Muestra de la posible Implementación de Machine learning en los datos desde Big Query: Propuestas de modelos 
3. Esbozo de la visualización o Dashboard.  	



## Extracción,tranformación y carga de datos

En esta primera parte veremos el ciclo de vida del dato. Explicación de los pasos en el VIDEO:  

https://www.youtube.com/watch?v=PlCpHxi0iw0

- Fuente de los datos: Se obtiene el dato directamente del cliente en formato CSV o Parquet
	- Interfaz para carga de datos.(Se explica en el siguiente subtítulo)
	- Extracción: La extraccion se basa principalmente con un bucket utilizado en Google Cloud.
	- Extrae directamente al bucket creado.
	- Extrae con nombre de archivo original.
- Verificación: Nuestra función solo procesa archivos con las extensiones .csv, .xlsx (Excel), o .parquet, si el archivo tiene otro formato, se detiene el proceso.
- Creación de carpeta temporal: El archivo se descarga desde el bucket y se guarda temporalmente en la carpeta /tmp del entorno de la Cloud Function.
- Lectura del archivo: Mediante la libreria de pandas se procede asignar un dataframe al archivo abierto.
- Tranformación de los datos: 
	- Normalizacion de nombres de columnas
	- Se eliminan espacios y se convierten los nombres de columnas a minúsculas para estandarizar.
	- Manejo de valores inválidos
	- Datos categoricos: Se eliminan caracteres no imprimibles y se rellenan valores faltantes con "N/A".
	- Datos numericos: Enteros (int) y flotantes (float): Se convierten valores no válidos a NaN o 0 y se rellenan según corresponda.
	- Guardado de archivo transformado: Se guarda el DataFrame transformado en un archivo temporal (en este punto se incorpora un codigo que trasnforme cualquier caracter no imprimible en el nombre del archivo para evtar cualquier inconveniente en la futura creacion de tablas en Big Querry).
- Subida de archivo transformado a GCS
	- El archivo transformado se sube al bucket en una carpeta llamada transformed/.
- Carga de datos en BigQuery
	- Configuracion de BigQuery
	- Se configura un dataset y una tabla en BigQuery. El dataset se basa en el nombre del archivo (De igual manera se ingresa un parametro que reemplace cualquier caracter no imprimible para evitar problemas en la creacion del dataset y tabla).
	- Creacion del dataset si no existe
	- Crea el dataset en el servicio de Big Querry de Google Cloud basado en el nombre del archivo original en caso de que no exista.
- Definicion de esquema y cargar datos
	- Se crean columnas y filas dependiendo de la estructura de los datos del dataset
	- Eliminar archivos temporales
	- Con cada proceso se elimina la carpeta /temp. del entorno de Google Cloud.
- Finalización: Si el evento se finaliza correctamente el entorno devuelve el print ("Proceso ETL completado exitosamente.") garantizando el ETL y la devolucion de tablas en Big Querry, lo que a su vez nos sirve como verificacion y validacion del proceso.
- Carga incremental: para el proceso de  carga incremental se uso una funcion llamada  calculate_file_hash, que se usa para detectar archivos unicos y evitar duplicados; el algoritmo que se uso en la funcion fue SHA256 que verifica la integradad de los dato en 256 bits.

### Interfaz Web para Subida de Archivos a Google Cloud

1. Descripción General: Este proyecto implementa una interfaz web utilizando *Flask* para facilitar la subida de archivos a Google Cloud Storage. Su propósito es ofrecer un sistema sencillo y accesible para que el cliente pueda cargar datos desde un medio local, automatizando la conexión con Google Cloud y la ejecución de un proceso ETL (Extract, Transform, Load).
2. Características Principales
	- Interfaz de Usuario Intuitiva: Permite a los usuarios cargar archivos locales de manera sencilla desde un navegador web.
	- Conexión con Google Cloud Storage: La aplicación se conecta con un bucket específico de Google Cloud para almacenar los archivos subidos.
	- Ejecución Automática de Función ETL: Tras subir el archivo, se ejecuta un proceso ETL que permite procesar, transformar y cargar los datos según los requerimientos.
	- Validación y Notificación al Usuario: Al completar la subida, la aplicación confirma que el archivo fue subido correctamente y muestra una notificación para validar el éxito del proceso.
3. Requisitos
	- *Python 3.11 o superior*
	- *Flask*
	- *Google Cloud SDK* y librerías relacionadas
	- *Credenciales JSON* para la autenticación en Google Cloud
4. Instrucciones de Uso
	1. Configuración del Entorno
	- Instala las dependencias necesarias:bash; pip install -r requirements.txt
	-  Configura las credenciales de Google Cloud estableciendo la variable de entorno: bash; export GOOGLE_APPLICATION_CREDENTIALS="ruta/al/archivo-de-credenciales.json"
	2. *Ejecutar la Aplicación*  
   	- Inicia el servidor Flask: bash; python app.py
	- Accede a la interfaz en tu navegador ingresando a http://127.0.0.1:5000.
	3. Cargar un Archivo  
	- Selecciona un archivo desde tu computadora local.
	- Haz clic en el botón de "Subir".
	- Recibe la notificación de confirmación tras la subida exitosa.
5. Resultados
Al finalizar el proceso:
	- El archivo será almacenado en el bucket especificado en Google Cloud.
	- Se ejecutará el proceso ETL asociado.
	- El cliente recibirá una notificación indicando que la subida se realizó correctamente.

### Ejemplo de data set implementado
Funcion taxis verdes y taxis amarillos 
- Descargamos 36 meses de datos de taxis amarillos y taxis verdes en archivos parquet, divididos en fechas 
- Subimos esos archivos parquet a la nube desde la interfaz
- Al iniciar la función se leen 3 archivos parquet.(leyendo datos de a 3 meses)
- El archivo se descarga desde el bucket y se guarda temporalmente en la carpeta /tmp del entorno de la Cloud Function.
- Se eliminan espacios y se convierten los nombres de columnas a minúsculas para estandarizar.
- Se eliminan caracteres no imprimibles y se rellenan valores faltantes con "N/A".
- Se procede a separar las columnas "tpep_pickup_datetime", "tpep_dropoff_datetime" y crear las columnas "cantidad_pasajeros","distancia_recorrida", "tipo_pago", "dia_viaje"	"hora_viaje", "año", "mes", "duracion del viaje".
- Se crea la columna "tarifa" usando el costo del viaje y restando los impuestos que se pagan.
- Se guarda el DataFrame transformado en un archivo temporal.
- Lee el siguiente parquet y repite el proceso pero al segundo lo une al final del df.
- Una vez hecho los tres se agrega a BigQuery
- Una vez repetido el proceso con los tres archivos, selecciona los siguiente 3 y repite el proceso hasta culminar.
- Al finalizar devuelve un archivo parquet en la carpeta "transformacion_verde" y "transformacion_amarillo", teniendo a disposicion un archivo parquet y otra en BigQuery

## Propuestas de modelos de Machine learning.
- En cuanto a la calidad del aire: 
	- Analisis historico y predicción de la contaminación del aire (Pm 2.5)
		- Ml utilizado:
			+ Primer modelo series de tiempo: Uso del algoritmo Arima 
			+ Segundo modelo series de tiempo: Uso del algoritmo Prophet
		- Entregable: 
			+ Graficos y análisis
			+ Predicción a 1 - 3 meses.
	- Clustering basado en sitios según el indice de contaminación. 
		- ML utilizado: Kmeans, regresión lineal. 
		- Entregable:
			+ Api de agrupación por Índice de contaminación
		+ Función que devuelve, con los datos de los sensores y sitios, un mapa con la zona seleccionada en color (según el índice de métricas) y sus datos de contaminación por número de mes, día y hora
	- Clustering de boroughts en función de sus caracteristicas.
		- ML utilizado: Obtención del número óptimo de clusters con elbow, Aplicación del algoritmo k means, Análisis de correlación con regresión lineal
		- Entregable: 
			+ Gráficos aleatorios de zonas con variables
			+ Gráfico de regresión lineal que muestra la correlación entre tránsito y pm 2.5
			+ Gráfico de las 10 zonas con más correlación respecto a la recta de regresión.
- En cuanto a clasificación de vehiculos
	- Clasificación de vehiculos (fuel) basado en su rendimento.
		- Ml utilizado: regresión lineal.
		- Entregable: 
			+ Api de clasificación de vehiculos: CSV con vehiculos eficientes
			+ Metricas de vehiculos
			+ Predicción del costo por vehiculo.
- En cuanto a la demanda de usuarios por zona:
	- Sistema de recomendación de acuerdo a zonas, día de la semana, hora, ganancia para taxis amarillos y verdes
		- Ml utilizado: XGBoost, R2Score.
		- Entregable: Api de recomendación	
			+ La zonas con mayor demanda
			+ La hora de dicha demanda
			+ Ganancia promedio según la zona, el hora de día y día de la semana
			+ La distancia promedio que se recorrerá
			+ Cantidad de viajes registrados en la zona
	- Análisis de la demanda por hora (Taxis verdes y amarillos)
		- ML utilizado: Random forest, DBSCAN, Prophet.
		- Entregable:
			+ Mapa de calor con zonas y sus horarios de mayor demanda.
			+ Predicción de demanda diaria, semanal
			+ Predicción del consumo de combustible
			+ Identificación de vehiculos eficientes. 
- En cuanto a la ganancia por zonas (Amarillos y verdes).
	- Predicción de ganancia por zonas:
		- ML: DBSCAN y Regresión lineal.
		- Entregable:
			+ Grafico de predicción de ganancia por zona
			+ Función de recomendación de zonas de posible sobregancia. 

## Propuesta de Dashboard, Mockup. 

Dashboard Interactivo: Taxis Nueva York
Este dashboard interactivo explora diversos aspectos del transporte en taxi en la ciudad de Nueva York, incluyendo análisis sobre facturación, demanda horaria y por zonas, así como las emisiones de CO2 y tendencias geográficas. Está diseñado para facilitar la exploración de datos, métricas y KPI's, ayudando a reflexionar sobre las estrategias a llevar a cabo.

Pestañas del Dashboard
1. Portada Introductoria
Portada introductoria que presenta el dashboard y da inicio a su exploración.

2. Facturación y Demanda Horaria
+ Análisis interactivo de la facturación y la demanda a lo largo del día.
	- Filtros disponibles:
	- Tipo de taxi.
	- Año.
	- Mes.
Sensible al descubrimiento de insights referente a la facturación y a la demanda horaria.
3. Demanda por Zonas
+ Exploración dinámica de la demanda de taxis en las distintas zonas de Nueva York.
+ Herramienta destacada: Shape Map interactivo que permite filtrar y visualizar por zonas específicas.
+ Filtros disponibles:
	- Tipo de taxi.
	- Año.
	- Mes.
	- Zonas.
+ Analiza las áreas de mayor actividad y las diferencias geográficas en la ciudad.
4. Emisiones de CO2
+ Visualización de las emisiones de dióxido de carbono generadas por los taxis:
+ Filtros disponibles:
	- Año.
	- Mes.
	- Distrito.
	- Zonas.
Identifica tendencias de crecimiento y patrones relacionados con la emision de CO2.
5. KPI's y Objetivos:
- Presentación de las métricas clave (KPI's) relacionadas con:
- Implementación autos eléctricos.
- Ingresos.
- Emisiones CO2.
Estado actual de los objetivos establecidos y su nivel de cumplimiento.
6. Reflexión y Conclusiones
- Resumen de los hallazgos principales del análisis.
- Generar un espacio de preguntas y respuestas acerca del contenido explorado.



