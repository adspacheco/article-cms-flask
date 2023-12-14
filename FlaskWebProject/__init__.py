"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from azure.storage.blob import BlockBlobService
from io import StringIO
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

# Logging level
app.logger.setLevel(logging.WARNING)

# Blob Config for Logging Save
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

# Blob Log and Handlers
blob_service = BlockBlobService(account_name=app.config['BLOB_ACCOUNT'], account_key=app.config['BLOB_STORAGE_KEY'])
blob_logging_handler = AzureBlobLoggingHandler(
    block_blob_service=blob_service,
    container_name="flasklogs",
    blob_name_prefix="app_log"
)
blob_logging_handler.setLevel(logging.WARNING)
app.logger.addHandler(blob_logging_handler)

# Stream Handler
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
