import apache_beam as beam
import logging
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions
import csv
from io import StringIO

class ParseCSV(beam.DoFn):
    def process(self, element):
        try:
            reader = csv.DictReader(StringIO(element))
            for row in reader:
                yield row
        except Exception as e:
            logging.error(f"Error al procesar el elemento: {element}, error: {str(e)}")

def run():
    options = PipelineOptions()
    options.view_as(StandardOptions).runner = 'DataflowRunner' 
    gcp_options = options.view_as(GoogleCloudOptions)
    gcp_options.project = 'boxwood-chassis-447813-m6' 
    gcp_options.job_name = 'csv-to-bigquery'
    gcp_options.temp_location = 'gs://mytesting-2024/temp' 
    gcp_options.region = 'us-central1' 


    with beam.Pipeline(options=options) as p:
        (p
         | 'Leer CSV desde GCS' >> beam.io.ReadFromText('gs://mytesting-2024/data/central/CatLineasAereas.csv')  # Reemplaza con tu ruta
         | 'Parsear CSV' >> beam.ParDo(ParseCSV())
         | 'Enviar a BigQuery' >> beam.io.WriteToBigQuery(
             'boxwood-chassis-447813-m6:airline.CatLineasAereas',  # Reemplaza con tu dataset y tabla
             schema='SCHEMA_AUTODETECT',  # O define tu esquema aquí
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
         ))
    
    with beam.Pipeline(options=options) as p:
        (p
         | 'Leer CSV desde GCS' >> beam.io.ReadFromText('gs://mytesting-2024/data/sucursal1/pasajeros.csv')  # Reemplaza con tu ruta
         | 'Parsear CSV' >> beam.ParDo(ParseCSV())
         | 'Enviar a BigQuery' >> beam.io.WriteToBigQuery(
             'boxwood-chassis-447813-m6:airline.pasajeros',  # Reemplaza con tu dataset y tabla
             schema='SCHEMA_AUTODETECT',  # O define tu esquema aquí
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
         ))
        
    with beam.Pipeline(options=options) as p:
        (p
         | 'Leer CSV desde GCS' >> beam.io.ReadFromText('gs://mytesting-2024/data/sucursal1/vuelos.csv')  # Reemplaza con tu ruta
         | 'Parsear CSV' >> beam.ParDo(ParseCSV())
         | 'Enviar a BigQuery' >> beam.io.WriteToBigQuery(
             'boxwood-chassis-447813-m6:airline.vuelos',  # Reemplaza con tu dataset y tabla
             schema='SCHEMA_AUTODETECT',  # O define tu esquema aquí
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
         ))
    
    with beam.Pipeline(options=options) as p:
        (p
         | 'Leer CSV desde GCS' >> beam.io.ReadFromText('gs://mytesting-2024/data/sucursal2/Pasajeros.csv')  # Reemplaza con tu ruta
         | 'Parsear CSV' >> beam.ParDo(ParseCSV())
         | 'Enviar a BigQuery' >> beam.io.WriteToBigQuery(
             'boxwood-chassis-447813-m6:airline.pasajeros2',  # Reemplaza con tu dataset y tabla
             schema='SCHEMA_AUTODETECT',  # O define tu esquema aquí
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
         ))
        
    with beam.Pipeline(options=options) as p:
        (p
         | 'Leer CSV desde GCS' >> beam.io.ReadFromText('gs://mytesting-2024/data/sucursal2/Vuelos.csv')  # Reemplaza con tu ruta
         | 'Parsear CSV' >> beam.ParDo(ParseCSV())
         | 'Enviar a BigQuery' >> beam.io.WriteToBigQuery(
             'boxwood-chassis-447813-m6:airline.vuelos2',  # Reemplaza con tu dataset y tabla
             schema='SCHEMA_AUTODETECT',  # O define tu esquema aquí
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
         ))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)  # Configura el nivel de logging
    run()