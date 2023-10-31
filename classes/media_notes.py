import pyaudio
import wave


class AudioRecorder:
    """the class will be """

    def __init__(self, chunk=1024, sample_format=pyaudio.paInt16, channels=1, sample_rate=44100):
        self.chunk = chunk
        self.sample_format = sample_format
        self.channels = channels
        self.sample_rate = sample_rate
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_recording(self, duration=5):
        """the function will be used to save the audio file here"""
        self.stream = self.audio.open(format=self.sample_format, channels=self.channels, rate=self.sample_rate,
                                      frames_per_buffer=self.chunk, input=True)

        for i in range(0, int(self.sample_rate / self.chunk * duration)):
            data = self.stream.read(self.chunk)
            self.frames.append(data)

        self.stop_recording()
        return self.frames

    def stop_recording(self):
        """the function to stop the recording session here"""
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

    def terminate(self):
        """the recording will be terminated by this function"""
        self.stop_recording()
        self.audio.terminate()

    def save_audio_frames(self, frames, filename, channels=1, sample_width=2, sample_rate=44100):
        """"saving the audio file here for the model """
        wave_file = wave.open(filename, "wb")
        wave_file.setnchannels(channels)
        wave_file.setsampwidth(sample_width)
        wave_file.setframerate(sample_rate)
        wave_file.writeframes(b"".join(frames))
        wave_file.close()
