"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys
import threading

CHUNK = 1024

def play_audio(audio_file_location=None):
    wf = wave.open(audio_file_location, 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)

def print_hi():
    c = raw_input('huasjdas')
    print(c)

try:
    threading.Thread(target=play_audio, kwargs={'audio_file_location': 'audio_files/ox.wav'}).start()
    threading.Thread(target=print_hi).start()
except KeyboardInterrupt:
    print('stop')
    sys.exit(1)
