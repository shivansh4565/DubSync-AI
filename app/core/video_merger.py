import os
from pydub import AudioSegment
import ffmpeg


def merge_video(video_path, speech_files, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    final_audio = AudioSegment.empty()

    for file in speech_files:
        final_audio += AudioSegment.from_mp3(file)

    audio_path = os.path.join(output_dir, "dubbed_audio.mp3")
    final_audio.export(audio_path, format="mp3")

    output_video = os.path.join(output_dir, "dubbed_video.mp4")

    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(audio_path)

    (
        ffmpeg
        .output(
            video.video,
            audio.audio,
            output_video,
            vcodec="copy",
            acodec="aac"
        )
        .overwrite_output()
        .run()
    )

    return output_video