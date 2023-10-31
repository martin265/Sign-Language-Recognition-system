import os
import datetime
import sounddevice as sd
import soundfile as sf


def record(duration, file_name):
    # Set up recording parameters
    sample_rate = 44100
    channels = 1
    file_format = "wav"

    # Create the recordings directory if it does not exist
    if not os.path.exists("recordings"):
        os.makedirs("recordings")

    # Start recording
    print("Recording started. Press Ctrl+C to stop.")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)

    # Wait for the recording to finish
    sd.wait()

    # Save the recording to a file
    file_name = os.path.join("recordings", f"{file_name}.{file_format}")
    sf.write(file_name, recording, sample_rate)

    print(f"Recording saved to {file_name}")


if __name__ == "__main__":
    duration = float(input("Enter recording duration in seconds: "))
    file_name = input("Enter file name (without extension): ")
    record(duration, file_name)
