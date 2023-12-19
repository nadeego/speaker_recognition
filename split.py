from pydub import AudioSegment

names = ['Max', 'Monika', 'Henry', 'James']

for name in names:
    audio = AudioSegment.from_file("{}_no_silence.mp3".format(name))

    # Define the length of each segment in milliseconds
    segment_length = 500  # 1000 ms = 1 seconds

    # Splitting and exporting segments
    counter = 0
    for i in range(0, len(audio), segment_length):
        counter += 1
        # Define the start and end of this segment
        start = i
        end = i + segment_length

        # Check if the end is beyond the length of the audio
        # and if the remaining duration is less than the segment length
        if end > len(audio) or (len(audio) - start) < segment_length:
            break  # Skip this segment and stop the loop

        # Extract the segment
        segment = audio[start:end]

        # Export the segment to a new file
        segment.export("{}_segment_{}.mp3".format(name, counter), format="mp3")