from pathlib import Path
from moviepy import VideoFileClip


def extract_audio(video_path: str, output_dir: str) -> str:
    """
    Extract audio from a video and save it as WAV.
    """

    video_path = Path(video_path)
    output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    audio_path = output_dir / f"{video_path.stem}.wav"

    video = VideoFileClip(str(video_path))

    if video.audio is None:
        raise Exception("No audio stream found in video.")

    video.audio.write_audiofile(
        str(audio_path),
        codec="pcm_s16le",
        logger=None
    )

    video.close()

    return str(audio_path)