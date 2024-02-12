Radio OSInt Project
Overview

The Radio Listener Project is designed to connect to a specific radio frequency, listen for a predetermined amount of time, record the transmission, and transcribe the audio content into text. This project integrates GNU Radio for radio frequency (RF) signal processing, Python for scripting and control flow, and additional libraries for audio processing and speech-to-text conversion.
Components

The project is structured into several key components:

    GNU Radio Connector (gnuradio_connector.py): Handles the connection to the specified radio frequency using GNU Radio and records the audio transmission.
    Audio Converter (convert_audio.py): Converts the recorded raw audio file into a WAV format file, making it suitable for transcription.
    Speech-to-Text Converter (speech_to_text.py): Transcribes the audio content from the WAV file into text using the speech_recognition library.
    Graphical User Interface (GUI) (main.py): Provides a user-friendly interface to input the desired frequency and duration, initiate the recording and transcription process, and display the transcribed text. The GUI is developed using Tkinter with a modern design emphasizing light blue and white colors.

Setup and Installation
Prerequisites

    Python 3.x
    GNU Radio
    speech_recognition Python library
    pydub Python library (for audio conversion)

Ensure GNU Radio is correctly installed and configured on your system. For Python libraries, you can install them using pip:



```pip install speechrecognition pydub```

Running the Project

To run the project, execute the main.py script:


```python main.py```
Or
```python radio_osint_gui.py```

This will launch the GUI, where you can enter the frequency and duration for the listening session. After the session, the GUI will display the transcribed text.
Implementation Details
GNU Radio Connector

The gnuradio_connector.py script is responsible for setting up the connection to the radio frequency using GNU Radio. It captures the audio signal for the duration specified by the user and saves it as a raw audio file.
Audio Converter

The convert_audio.py module takes the raw audio file and converts it into a WAV format file. This step is necessary because the speech-to-text library requires the audio to be in a standard format (e.g., WAV) for processing.
Speech-to-Text Conversion

The speech_to_text.py script uses the speech_recognition library to transcribe the audio content of the WAV file into text. This module can be extended to use different speech-to-text engines as needed.
GUI Design

The GUI, implemented in main.py, is designed with Tkinter to provide a simple yet modern interface. It allows users to input the frequency and duration, start the recording and transcription process, and view the transcribed text. The design focuses on usability and visual appeal, with a color scheme of light blue and white.
Future Work

    Enhanced Error Handling: Improve the robustness of the system by handling potential errors in the radio connection, audio processing, and transcription phases.
    Support for Multiple Languages: Extend the speech-to-text conversion to support transcription in multiple languages.
    Performance Optimization: Optimize the performance for real-time or near-real-time transcription.
    Advanced Audio Processing: Implement noise reduction and audio enhancement techniques to improve transcription accuracy.
