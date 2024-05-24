from azure.data.tables import TableServiceClient
from azure.core.exceptions import ResourceExistsError
import logging
from datetime import datetime

class AzureDataTablesClient:
    def __init__(self, connection_string, table_name):
        self.connection_string = connection_string
        self.table_name = table_name
        self.table_service_client = None

    def connect(self):

        """
        Establishes a connection to Azure Data Tables.

        This method attempts to connect to Azure Data Tables using the provided connection string.
        If successful, it initializes a TableServiceClient object that can be used for data operations.

        :raises: Any exception raised during the connection attempt is caught and logged.
                This ensures that errors are properly handled without crashing the program.

        :return: None
        """
        try:
            logging.info('Trying to connect to Azure Data Tables')
            self.table_service_client = TableServiceClient.from_connection_string(self.connection_string)
            logging.info("Connected to Azure Data Tables")
        except Exception as e:
            logging.error(f"Error connecting to Azure Data Tables: {e}")

    def insert_batch_entities(self, entities,PartitionKey, RowKey,columnstoinsert, batch_size=1):


        """
        Inserts entities into an Azure Data Table in batches.

        This method prepares data to be inserted into the specified Azure Data Table in batches,
        based on the provided entities, partition key, row key, and columns to insert.

        :param entities: The data to be inserted into the table.
        :type entities: Json
        :param PartitionKey: The partition key for the entities.
        :type PartitionKey: str
        :param RowKey: The row key for the entities.
        :type RowKey: str
        :param columnstoinsert: The list of columns to insert into the table.
        :type columnstoinsert: list
        :param batch_size: The size of each batch for batch insertion (default is 1).
        :type batch_size: int

        :raises ValueError: If an error occurs during data insertion, a ValueError is raised and logged.

        :return: None
        """
        try : 
            logging.info(f'Preparing data to insert into {self.table_name} table')
            table_client = self.table_service_client.get_table_client(self.table_name)
            entities_to_insert = []
            for row in entities:
                entity = {'PartitionKey': PartitionKey, 'RowKey': row[RowKey]}
                for col in columnstoinsert:
                    entity[col] = row[col]
                entities_to_insert.append(("upsert", entity))
                if len(entities_to_insert) == batch_size : 
                     logging.info(f'batch to insert : {entities_to_insert}')
                     table_client.submit_transaction(entities_to_insert)
                     entities_to_insert = []
            if len(entities_to_insert) > 0 : 
                logging.info(f'batch to insert : {entities_to_insert}')
                table_client.submit_transaction(entities_to_insert)
                
            logging.info(f'All lines are successfully inserted into {self.table_name} table.')

        except ValueError as e : 
             logging.error(f'An error was occured while trying to insert data into {self.table_name} table : {e}')

    def query_entities(self,filter_condition,batch_size=1):


        """
        Executes a query to retrieve entities from an Azure Data Table.

        This method executes a query on the specified Azure Data Table using the provided filter condition.
        It retrieves entities based on the query results, with an optional batch size parameter for pagination.

        :param filter_condition: The filter condition to apply to the query.
        :type filter_condition: str
        :param batch_size: The number of results per page (default is 1).
        :type batch_size: int

        :return: A list of entities retrieved from the table based on the query results.
        :rtype: list
        """
        try:

            table_client = self.table_service_client.get_table_client(self.table_name)
            entities = []
            logging.info(f'Executing query : {filter_condition}')
            for entity_page in table_client.query_entities(query_filter=filter_condition, results_per_page=batch_size).by_page():
                entities.extend(list(entity_page))
                break
            logging.info(f'Query Results : {entities}')
            return entities
        except ValueError as e:
            logging.error(f'An error occured while trying to query data from {self.table_name} table : {e}')
            


