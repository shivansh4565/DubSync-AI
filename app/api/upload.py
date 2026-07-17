import os
import uuid
import shutil

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from app.models.job import Job
from app.services.job_manager import job_manager
from app.core.config import UPLOAD_DIR
from app.core.config import ALLOWED_VIDEO_TYPES

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_video(
    file: UploadFile = File(...)
):

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_VIDEO_TYPES:

        raise HTTPException(
            status_code=400,
            detail="Unsupported video format."
        )

    job_id = str(uuid.uuid4())

    filename = f"{job_id}{extension}"

    save_path = UPLOAD_DIR / filename

    with open(save_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    job = Job(
        job_id=job_id,
        status="uploaded",
        video_path=str(save_path)
    )

    job_manager.create_job(job)

    return {
        "message": "Video uploaded successfully.",
        "job_id": job_id
    }