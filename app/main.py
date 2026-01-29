# from fastapi import FastAPI
# from .api.file_processing_controller import FileProcessingController
# from .db.session import engine
# from .db.base import Base
# from .db import models

# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="Document Processing API")

# controller = FileProcessingController()
# app.include_router(controller.router)

from fastapi import FastAPI
from .api.file_processing_controller import FileProcessingController
from .api.document_query_controller import DocumentQueryController

app = FastAPI(title="Document Processing API")

app.include_router(FileProcessingController().router)
app.include_router(DocumentQueryController().router)
