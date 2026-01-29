from fastapi import FastAPI
from .api.file_processing_controller import FileProcessingController
from .api.document_query_controller import DocumentQueryController

app = FastAPI(title="Document Processing API")

app.include_router(FileProcessingController().router)
app.include_router(DocumentQueryController().router)
