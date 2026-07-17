import os
from gtts import gTTS


def generate_speech(translations, output_dir):
    """
    Generate one audio file for each translated segment.
    """

    os.makedirs(output_dir, exist_ok=True)

    generated_files = []

    for i, segment in enumerate(translations):

        text = segment["translated"]

        filename = os.path.join(output_dir, f"segment_{i}.mp3")

        try:
            tts = gTTS(
                text=text,
                lang="hi",
                slow=False
            )

            tts.save(filename)

            generated_files.append(filename)

        except Exception as e:
            print(e)

    return generated_files