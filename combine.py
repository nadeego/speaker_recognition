from pydub import AudioSegment

name = 'James'

# Load the first MP3 file
audio1 = AudioSegment.from_file("{}1.mp3".format(name))
audio2 = AudioSegment.from_file("{}2.mp3".format(name))
audio3 = AudioSegment.from_file("{}2.mp3".format(name))


# Concatenate audio files
combined_audio = audio1 + audio2 + audio3 # You can add more in the same way

# Export the concatenated audio
combined_audio.export("{}_combined.mp3".format(name), format="mp3")

