from io import BytesIO
from datetime import datetime
import re
from Azure_storage.lib.Azurestoragebaseclasse import AzureStorageConnector
from azure.storage.blob import BlobSasPermissions

class AzureBlobProcessor(AzureStorageConnector):
    """
    Cette classe permet de lire et de pousser des fichiers vers le stockage Blob Azure.

    :param str container_name: Le nom du conteneur Blob.
    :param str flow_name: Le nom du flux.
    :param str connection_string: La chaîne de connexion à utiliser pour se connecter au service Blob.
                                  Par défaut, None.
    :param str account_name: Le nom du compte de stockage Azure. Par défaut, None.
    :param str account_key: La clé du compte de stockage Azure. Par défaut, None.

    :ivar str container_name: Le nom du conteneur Blob.
    :ivar str flow_name: Le nom du flux.
    :ivar str connection_string: La chaîne de connexion à utiliser pour se connecter au service Blob.
    :ivar str account_name: Le nom du compte de stockage Azure.
    :ivar str account_key: La clé du compte de stockage Azure.
    """

    def __init__(self, container_name, flow_name, connection_string=None, account_name=None, account_key=None):
        """
        Initialise une instance de la classe AzureBlobProcessor.

        :param str container_name: Le nom du conteneur Blob.
        :param str flow_name: Le nom du flux.
        :param str connection_string: La chaîne de connexion à utiliser pour se connecter au service Blob.
                                      Par défaut, None.
        :param str account_name: Le nom du compte de stockage Azure. Par défaut, None.
        :param str account_key: La clé du compte de stockage Azure. Par défaut, None.
        """
        super().__init__(connection_string, account_name, account_key)
        self.container_name = container_name
        self.flow_name = flow_name

    def read_blob_files(self, regex_pattern=r'.*', permissions=BlobSasPermissions(read=True), expiry=None):
        """
        Récupère des fichiers depuis le stockage Blob Azure.

        :param str regex_pattern: Le motif d'expression régulière pour filtrer les noms de fichiers. Par défaut, '.*'.
        :param BlobSasPermissions permissions: Les permissions pour le SAS Blob. Par défaut, BlobSasPermissions(read=True).
        :param datetime expiry: La date d'expiration du SAS Blob. Par défaut, None.

        :return: Un générateur contenant les informations des fichiers.
        :rtype: generator
        """
        self.connect_blob_service(self.container_name, blob_permissions=permissions, blob_expiry=expiry)
        container_client = self.blob_service_client.get_container_client(self.container_name)
        for blob in container_client.list_blobs():
            if re.match(regex_pattern, blob.name):
                blob_client = container_client.get_blob_client(blob.name)
                file_content = BytesIO()
                file_content.write(blob_client.download_blob().readall())
                file_content.seek(0)
                yield {'file_name': blob.name, 'file_content': file_content}

    def push_files_to_blob(self, files_info, permissions=BlobSasPermissions(write=True), expiry=None):
        """
        Pousse des fichiers vers le stockage Blob Azure.

        :param list files_info: La liste des informations sur les fichiers à pousser, où chaque élément est un tuple
                                 contenant le nom du fichier et son contenu.
        :param BlobSasPermissions permissions: Les permissions pour le SAS Blob. Par défaut, BlobSasPermissions(write=True).
        :param datetime expiry: La date d'expiration du SAS Blob. Par défaut, None.

        :return: None
        """
        self.connect_blob_service(self.container_name, blob_permissions=permissions, blob_expiry=expiry)
        container_client = self.blob_service_client.get_container_client(self.container_name)
        for file_info in files_info:
            file_name = file_info[0]
            file_content = file_info[1]
            current_date = datetime.now().strftime("%d-%m-%Y")
            folder_name = f"{self.flow_name}/{current_date}/"
            blob_name = folder_name + file_name
            container_client.upload_blob(name=blob_name, data=file_content, overwrite=True)
            self.logger.info(f"File '{file_name}' successfully pushed to Azure Blob Storage.")
