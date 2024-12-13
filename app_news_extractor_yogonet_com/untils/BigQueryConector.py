from os import environ
from google.cloud import bigquery
from pandas_gbq import to_gbq

class BigQueryConector:
    def __init__(self, logger):        
        self.client = bigquery.Client()
        self.logger = logger
        

    def _generate_schema_from_df(self, df):
            schema = []
            for column, dtype in df.dtypes.items():
                if dtype == 'int64':
                    field_type = 'INTEGER'
                elif dtype == 'float64':
                    field_type = 'FLOAT'
                elif dtype == 'bool':
                    field_type = 'BOOLEAN'
                elif dtype.name == 'datetime64[ns]':
                    field_type = 'TIMESTAMP'
                else:
                    field_type = 'STRING'
                
                schema.append(bigquery.SchemaField(column, field_type))
            
            return schema


    def df_to_sql(self, project_id, dataset_id, table, df):
        # Identificador completo de la tabla
        table_id = f"{project_id}.{dataset_id}.{table}"

        try:
            # Verifica si la tabla existe
            self.client.get_table(table_id)
            self.logger.info(f"The table {table_id} exists")
        except Exception as e:
            # Si no existe, crea la tabla
            self.logger.info(f"Table {table_id} does not exist. Creating it.")
            schema = self._generate_schema_from_df(df)
            table = bigquery.Table(table_id, schema=schema)
            self.client.create_table(table)
            self.logger.info(f"Table {table_id} is created")

        # Inserts data into the table
        try:       
            to_gbq(df, destination_table=table_id, project_id=project_id, if_exists='append')
            return True
        except Exception as e:
            self.logger.info(f"Error when inserting data in the table: {str(e)}")
            return False
        