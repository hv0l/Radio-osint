import gnuradio_connector
import audio_processor
import speech_to_text

def main():
    frequency = 100.0e6  # Frequenza di esempio in Hz (100 MHz)
    duration = 10  # Durata dell'ascolto in secondi
    
    print(f"Connessione alla frequenza {frequency} Hz per {duration} secondi...")
    # Stabilire la connessione e registrare l'audio
    audio_path = gnuradio_connector.connect_and_record(frequency, duration)
    
    if audio_path:
        print("Trasformazione dell'audio in testo...")
        # Processare l'audio registrato e convertirlo in testo
        text = speech_to_text.audio_to_text(audio_path)
        
        print("Trascrizione completata:")
        print(text)
    else:
        print("Errore nella cattura dell'audio.")

if __name__ == "__main__":
    main()
