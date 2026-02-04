from fastapi import FastAPI
from .api.file_processing_controller import FileProcessingController
from .api.document_query_controller import DocumentQueryController
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Document Processing API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://localhost:3000",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(FileProcessingController().router)
app.include_router(DocumentQueryController().router)
