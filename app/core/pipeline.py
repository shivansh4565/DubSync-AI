from app.core.config import TEMP_DIR, TTS_DIR, OUTPUT_DIR
from app.core.extractor import extract_audio
from app.core.transcriber import transcribe
from app.core.diarization import diarize
from app.core.translator import translate_segments
from app.core.tts import generate_speech
from app.core.video_merger import merge_video
from app.services.job_manager import job_manager


def process_video(job_id):

    job = job_manager.get_job(job_id)

    if job is None:
        raise Exception("Job not found.")

    # Extract Audio
    job_manager.update_job(job_id, status="Extracting Audio")

    audio_path = extract_audio(
        job.video_path,
        TEMP_DIR
    )

    job_manager.update_job(
        job_id,
        audio_path=audio_path
    )

    # Transcribe
    job_manager.update_job(job_id, status="Transcribing")

    transcript = transcribe(audio_path)

    # Speaker Detection
    job_manager.update_job(job_id, status="Detecting Speakers")

    speakers = diarize(transcript)

    # Translation
    job_manager.update_job(job_id, status="Translating")

    translated_segments = translate_segments(
        speakers,
        target_language="hi"
    )

    # Generate Speech
    job_manager.update_job(job_id, status="Generating Speech")

    speech_files = generate_speech(
        translated_segments,
        TTS_DIR
    )

    # Merge Video
    job_manager.update_job(job_id, status="Creating Dubbed Video")

    output_video = merge_video(
        str(job.video_path),
        speech_files,
        str(OUTPUT_DIR)
    )

    # Finish
    job_manager.update_job(
        job_id,
        transcript=transcript,
        speakers=speakers,
        translations=translated_segments,
        output_video=output_video,
        status="Completed"
    )

    return {
        "success": True,
        "audio_path": audio_path,
        "transcript": transcript,
        "speakers": speakers,
        "translations": translated_segments,
        "speech_files": speech_files,
        "output_video": output_video
    }