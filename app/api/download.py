from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.services.job_manager import job_manager

router = APIRouter(
    prefix="/download",
    tags=["Download"]
)


@router.get("/{job_id}")
def download_video(job_id: str):
    """
    Download the generated dubbed video.
    """

    job = job_manager.get_job(job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found."
        )

    if job.output_video is None:
        raise HTTPException(
            status_code=400,
            detail="Output video not generated yet."
        )

    return FileResponse(
        path=job.output_video,
        media_type="video/mp4",
        filename="dubbed_video.mp4"
    )