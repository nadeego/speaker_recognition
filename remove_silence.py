from pydub import AudioSegment
from pydub.silence import detect_nonsilent

names = ['', '', '', ''] # names removed

for name in names:
    # Load MP3 file
    audio = AudioSegment.from_file("{}_combined.mp3".format(name))

    # Define parameters for silence detection
    min_silence_len = 1000  # Minimum length of silence in ms to be considered
    silence_thresh = -40   # Silence threshold in dB

    # Detect non-silent parts
    nonsilent_parts = detect_nonsilent(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    # Create a new audio segment from the non-silent parts
    non_silent_audio = AudioSegment.empty()
    for start, end in nonsilent_parts:
        non_silent_audio += audio[start:end]

    # Export the result
    non_silent_audio.export("{}_no_silence.mp3".format(name), format="mp3")

