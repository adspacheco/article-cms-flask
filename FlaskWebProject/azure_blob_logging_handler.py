import logging
from io import StringIO
from datetime import datetime
from FlaskWebProject import app
from azure.storage.blob import BlockBlobService

class AzureBlobLoggingHandler(logging.Handler):
    def __init__(self, block_blob_service, container_name, blob_name_prefix):
        super().__init__()
        self.block_blob_service = block_blob_service
        self.container_name = container_name
        self.blob_name_prefix = blob_name_prefix
        self.log_stream = StringIO()

    def emit(self, record):
        msg = self.format(record)
        self.log_stream.write(msg + '\n')
        self.flush()

    def flush(self):
        blob_name = f"{self.blob_name_prefix}_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
        self.block_blob_service.create_blob_from_text(
            container_name=self.container_name,
            blob_name=blob_name,
            text=self.log_stream.getvalue()
        )
        self.log_stream.seek(0)
        self.log_stream.truncate()

# Configuração do Blob para Logging
blob_logging_handler = AzureBlobLoggingHandler(
    block_blob_service=blob_service, 
    container_name=blob_container, 
    blob_name_prefix="app_log"
)
blob_logging_handler.setLevel(logging.WARNING)
app.logger.addHandler(blob_logging_handler)
