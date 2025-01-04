from google.cloud import storage, bigquery
import pandas as pd
import os
import numpy as np

def etl_process(event, context):
    """
    Cloud Function que realiza un proceso ETL cuando se sube un archivo al bucket.

    Args:
        event (dict): Datos del evento de GCS.
        context (google.cloud.functions.Context): Contexto del evento.
    """
    # Extraer información del evento
    bucket_name = event['bucket']
    file_name = event['name']

    # Verificar el tipo de archivo
    if not (file_name.endswith('.csv') or file_name.endswith('.xlsx') or file_name.endswith('.parquet')):
        print(f"El archivo {file_name} no es un CSV, Excel o Parquet. Se omite el procesamiento.")
        return

    # Descargar el archivo desde el bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    local_file_path = f"/tmp/{file_name}"
    blob.download_to_filename(local_file_path)
    print(f"Archivo descargado: {local_file_path}")

    # Leer el archivo según su formato con manejo de errores
    try:
        if file_name.endswith('.csv'):
            df = pd.read_csv(local_file_path, on_bad_lines='skip', quotechar='"', encoding_errors='replace')
        elif file_name.endswith('.xlsx'):
            df = pd.read_excel(local_file_path)
        elif file_name.endswith('.parquet'):
            df = pd.read_parquet(local_file_path)
    except Exception as e:
        print(f"Error al leer el archivo {file_name}: {e}")
        return

    # Transformar: Normalizar nombres de columnas
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

    # Transformar: Manejar valores inválidos o no procesables
    for col in df.columns:
        if df[col].dtype == "object":  # Columnas categóricas
            df[col] = df[col].replace({r'[^ -~]': 'N/A'}, regex=True)  # Reemplazar caracteres especiales
            df[col] = df[col].fillna("N/A").astype(str)
        elif pd.api.types.is_integer_dtype(df[col]):  # Columnas enteras
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        elif pd.api.types.is_float_dtype(df[col]):  # Columnas flotantes
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(np.nan).astype(float)
        else:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(np.nan)  # Caso genérico

    # Guardar el archivo transformado temporalmente
    transformed_dir = "/tmp/transformed"
    os.makedirs(transformed_dir, exist_ok=True)  # Crear el directorio si no existe

    transformed_file = f"{transformed_dir}/{file_name.replace('+', '_')}"  # Reemplazar caracteres inválidos en el nombre del archivo
    if file_name.endswith('.csv') or file_name.endswith('.xlsx'):
        df.to_csv(transformed_file, index=False)
    elif file_name.endswith('.parquet'):
        df.to_parquet(transformed_file, index=False)

    # Subir el archivo transformado al bucket dentro de la carpeta "transformed/"
    transformed_blob = bucket.blob(f"transformed/{file_name.replace('+', '_')}")
    transformed_blob.upload_from_filename(transformed_file)
    print(f"Archivo transformado subido a GCS: gs://{bucket_name}/transformed/{file_name.replace('+', '_')}")

    # Configurar BigQuery
    dataset_name = file_name.split('.')[0].replace(' ', '_').replace('-', '_').replace('+', '_').lower()  # Dataset basado en el nombre del archivo
    table_name = "data"  # Nombre genérico para la tabla
    bq_client = bigquery.Client()

    # Crear el dataset si no existe
    dataset_ref = bq_client.dataset(dataset_name)
    try:
        bq_client.get_dataset(dataset_ref)  # Verifica si el dataset existe
    except Exception:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "us-central1"
        bq_client.create_dataset(dataset)
        print(f"Dataset creado: {dataset_name}")

    # Definir el esquema de la tabla basado en los tipos de datos del DataFrame
    schema = []
    for column, dtype in zip(df.columns, df.dtypes):
        if pd.api.types.is_integer_dtype(dtype):
            field_type = "INTEGER"
        elif pd.api.types.is_float_dtype(dtype):
            field_type = "FLOAT"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            field_type = "TIMESTAMP"
        else:
            field_type = "STRING"
        schema.append(bigquery.SchemaField(column, field_type))

    # Configurar el trabajo de carga
    if file_name.endswith('.csv'):
        job_config = bigquery.LoadJobConfig(
            schema=schema,
            skip_leading_rows=1,  # Aplicable solo para archivos CSV
            source_format=bigquery.SourceFormat.CSV,
        )
    elif file_name.endswith('.parquet'):
        job_config = bigquery.LoadJobConfig(
            schema=schema,
            source_format=bigquery.SourceFormat.PARQUET,
        )
    elif file_name.endswith('.xlsx'):
        print("BigQuery no soporta directamente la carga de archivos Excel. Asegúrate de convertir a CSV o Parquet.")
        return
    else:
        print(f"Formato de archivo no soportado para BigQuery: {file_name}")
        return

    # Cargar los datos a la tabla
    with open(transformed_file, "rb") as source_file:
        job = bq_client.load_table_from_file(
            source_file, dataset_ref.table(table_name), job_config=job_config
        )

    # Esperar a que termine el trabajo
    try:
        job.result()
        print(f"Datos cargados en BigQuery: {dataset_name}.{table_name}")
    except Exception as e:
        print(f"Error durante la carga a BigQuery: {e}")
        return

    # Eliminar archivos temporales
    try:
        os.remove(local_file_path)
        os.remove(transformed_file)
        print(f"Archivos temporales eliminados: {local_file_path}, {transformed_file}")
    except Exception as e:
        print(f"Error al eliminar archivos temporales: {e}")

    print("Proceso ETL completado exitosamente.")