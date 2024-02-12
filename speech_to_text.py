import speech_recognition as sr

def audio_to_text(filepath):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text
