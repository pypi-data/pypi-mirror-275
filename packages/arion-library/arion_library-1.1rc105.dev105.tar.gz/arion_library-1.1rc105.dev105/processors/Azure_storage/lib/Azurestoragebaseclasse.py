import logging
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from azure.data.tables import TableServiceClient, generate_table_sas, TableSasPermissions
from datetime import datetime, timezone, timedelta

class AzureStorageConnector:
    """
    Cette classe permet d'établir une connexion avec les services de stockage Azure Blob et Azure Table.

    :param str connection_string: La chaîne de connexion à utiliser pour se connecter au service. 
                                  Par défaut, None.
    :param str account_name: Le nom du compte de stockage Azure. Par défaut, None.
    :param str account_key: La clé du compte de stockage Azure. Par défaut, None.

    :ivar str connection_string: La chaîne de connexion à utiliser pour se connecter au service.
    :ivar str account_name: Le nom du compte de stockage Azure.
    :ivar str account_key: La clé du compte de stockage Azure.
    :ivar logging.Logger logger: Le logger pour enregistrer les messages.
    """

    def __init__(self, connection_string=None, account_name=None, account_key=None):
        """
        Initialise une instance de la classe AzureStorageConnector.

        :param str connection_string: La chaîne de connexion à utiliser pour se connecter au service. 
                                      Par défaut, None.
        :param str account_name: Le nom du compte de stockage Azure. Par défaut, None.
        :param str account_key: La clé du compte de stockage Azure. Par défaut, None.
        """
        self.connection_string = connection_string
        self.account_name = account_name
        self.account_key = account_key
        self.logger = logging.getLogger('AzureStorageConnector')

    def generate_blob_sas_key(self, container_name, permissions=BlobSasPermissions(read=True), expiry=None):
        """
        Génère un jeton SAS pour le stockage Blob Azure.

        :param str container_name: Le nom du conteneur Blob.
        :param BlobSasPermissions permissions: Les permissions pour le SAS Blob. Par défaut, BlobSasPermissions(read=True).
        :param datetime expiry: La date d'expiration du SAS Blob. Par défaut, None.

        :return: Le jeton SAS généré.
        :rtype: str
        """
        expiry = expiry or datetime.now(timezone.utc) + timedelta(hours=1)  
        sas_token = generate_blob_sas(
            account_name=self.account_name,
            container_name=container_name,
            account_key=self.account_key,
            permission=permissions,
            expiry=expiry
        )
        return sas_token

    def generate_table_sas_key(self, table_name, permissions=TableSasPermissions(read=True), expiry=None):
        """
        Génère un jeton SAS pour le stockage de table Azure.

        :param str table_name: Le nom de la table.
        :param TableSasPermissions permissions: Les permissions pour le SAS de la table. Par défaut, TableSasPermissions(read=True).
        :param datetime expiry: La date d'expiration du SAS de la table. Par défaut, None.

        :return: Le jeton SAS généré.
        :rtype: str
        """
        expiry = expiry or datetime.now(timezone.utc) + timedelta(hours=1)  
        sas_token = generate_table_sas(
            account_name=self.account_name,
            table_name=table_name,
            account_key=self.account_key,
            permission=permissions,
            expiry=expiry
        )
        return sas_token

    def connect_blob_service(self, container_name, blob_permissions=BlobSasPermissions(read=True), blob_expiry=None):
        """
        Établit une connexion avec le service Blob Azure.

        :param str container_name: Le nom du conteneur Blob.
        :param BlobSasPermissions blob_permissions: Les permissions pour le SAS Blob. Par défaut, BlobSasPermissions(read=True).
        :param datetime blob_expiry: La date d'expiration du SAS Blob. Par défaut, None.

        :raises ValueError: Si aucune chaîne de connexion ni nom de compte et clé ne sont fournis.

        :return: None
        """
        try:
            if self.connection_string:
                self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
                self.logger.info("Connected to Azure Blob Service using connection string")
            elif self.account_name and self.account_key:
                sas_key = self.generate_blob_sas_key(container_name, permissions=blob_permissions, expiry=blob_expiry)
                self.blob_service_client =  BlobServiceClient(sas_key)

                self.logger.info("Connected to Azure Blob Service using SAS Key")
            else:
                raise ValueError("Either connection string or both account name and account key must be provided")
        except Exception as e:
            self.logger.error(f"Error connecting to Azure Blob Service: {e}")

    def connect_table_service(self, table_name, table_permissions=TableSasPermissions(read=True), table_expiry=None):
        """
        Établit une connexion avec le service de table Azure.

        :param str table_name: Le nom de la table.
        :param TableSasPermissions table_permissions: Les permissions pour le SAS de la table. Par défaut, TableSasPermissions(read=True).
        :param datetime table_expiry: La date d'expiration du SAS de la table. Par défaut, None.

        :raises ValueError: Si aucune chaîne de connexion ni nom de compte et clé ne sont fournis.

        :return: None
        """
        try:
            if self.connection_string:
                self.table_service_client = TableServiceClient.from_connection_string(self.connection_string)
                self.logger.info("Connected to Azure Table Service using connection string")
            elif self.account_name and self.account_key:
                sas_key = self.generate_table_sas_key(table_name, permissions=table_permissions, expiry=table_expiry)
                self.table_service_client = TableServiceClient(sas_key)
                self.logger.info("Connected to Azure Table Service using SAS token")
            else:
                raise ValueError("Either connection string or both account name and account key must be provided")
        except Exception as e:
            self.logger.error(f"Error connecting to Azure Table Service: {e}")
