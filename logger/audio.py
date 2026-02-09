import pyaudio
import wave
import os
from pydub import AudioSegment

def record_audio(duration=30, output_path='logs/audio.mp3'):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=2,
        rate=44100,
        input=True,
        frames_per_buffer=1024
    )

    print("Recording...")
    frames = []
    for i in range(0, int(44100 / 1024 * duration)):
        data = stream.read(1024, exception_on_overflow=False)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Write to a temporary WAV file
    temp_wav = 'logs/temp_audio.wav'
    os.makedirs('logs', exist_ok=True)
    
    wf = wave.open(temp_wav, 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Convert WAV to MP3
    try:
        audio = AudioSegment.from_wav(temp_wav)
        audio.export(output_path, format="mp3", bitrate="192k")
        os.remove(temp_wav)
        print(f"Audio saved as MP3: {output_path}")
    except Exception as e:
        print(f"Error converting to MP3: {e}. Saving as WAV instead.")
        os.rename(temp_wav, output_path.replace('.mp3', '.wav'))