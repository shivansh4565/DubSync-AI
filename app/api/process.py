from fastapi import APIRouter, HTTPException

from app.core.pipeline import process_video

router = APIRouter(
    prefix="/process",
    tags=["Processing"]
)


@router.post("/{job_id}")
def process(job_id: str):

    try:
        result = process_video(job_id)

        return {
            "message": "Processing completed successfully.",
            "status": "completed",
            "transcript": result["transcript"],
            "speakers": result["speakers"],
            "translations": result["translations"],
            "speech_files": result["speech_files"],
            "output_video": result["output_video"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )