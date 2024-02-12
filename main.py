import gnuradio_connector
import speech_to_text
from convert_audio import raw_to_wav 

def main():
    frequency = 100.0e6  
    duration = 10 
    raw_audio_path = "output.raw"
    wav_audio_path = "output.wav"

    print(f"Connessione alla frequenza {frequency} Hz per {duration} secondi...")
    audio_path = gnuradio_connector.connect_and_record(frequency, duration)
    
    if audio_path:
        print("Conversione dell'audio in formato WAV...")
        raw_to_wav(raw_audio_path, wav_audio_path)
        
        print("Trasformazione dell'audio in testo...")
        text = speech_to_text.audio_to_text(wav_audio_path)
        
        print("Trascrizione completata:")
        print(text)
    else:
        print("Errore nella cattura dell'audio.")

if __name__ == "__main__":
    main()
