from fastapi import APIRouter, UploadFile, File, Depends
import tempfile, os
from fastapi.responses import RedirectResponse
from app.services.document_processing_service import DocumentProcessingService
from app.db.dependencies import get_db

class FileProcessingController:

    def __init__(self):
        self.router = APIRouter(prefix="/files", tags=["File Processing"])
        self.service = DocumentProcessingService()
        self._register_routes()

    def _register_routes(self):
        self.router.post("/process")(self.process_file)

    async def process_file(
        self,
        file: UploadFile = File(...),
        db = Depends(get_db)
    ):
        suffix = os.path.splitext(file.filename)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        try:
            result = self.service.process(
                db=db,
                file_path=tmp_path,
                filename=file.filename
            )

            document_id = result["document_id"]

            return RedirectResponse(
                url=f"/documents/{document_id}",
                status_code=303
            )

        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
