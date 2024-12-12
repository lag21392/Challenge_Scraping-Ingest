from os import environ
from google.cloud import bigquery

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

        table_id = f'{dataset_id}.{table}'

        try:
            self.client.get_table(table_id)
            self.logger.info(f'The table {table_id} exists')
        except:
            schema = self._generate_schema_from_df(df)
            table = bigquery.Table(table_id, schema=schema)
            self.client.create_table(table)  
            self.logger.info(f'Table {table_id} is created')  


        df.to_gbq(table_id, project_id=project_id, if_exists='append')
        
        return True