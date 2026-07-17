from pydantic import BaseModel
from typing import Optional, List, Dict


class Job(BaseModel):
    job_id: str

    status: str

    video_path: Optional[str] = None

    audio_path: Optional[str] = None

    transcript: Optional[str] = None

    speakers: Optional[List[Dict]] = None

    translations: Optional[List[Dict]] = None

    output_video: Optional[str] = None