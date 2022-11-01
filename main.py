import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    print(int.from_bytes(data, "little", signed=True))

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

intframes = []

for i in frames:
	intframes.append(int.from_bytes(i, "little", signed=True))
	
	
framesnp = np.array(intframes)
t = np.arange(0, 44100*RECORD_SECONDS)

print(framesnp)

fig, ax = plt.subplots()
ax.plot(t, intframes)
plt.show()