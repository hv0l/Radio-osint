from pydub import AudioSegment

def raw_to_wav(raw_filepath, wav_filepath):
    audio = AudioSegment.from_raw(raw_filepath, sample_width=2, frame_rate=44100, channels=1)
    audio.export(wav_filepath, format="wav")
