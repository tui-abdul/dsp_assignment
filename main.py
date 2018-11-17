import pylab
import pyaudio
from scipy import signal, stats, integrate
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as w

p = pyaudio.PyAudio()
fs, audio = w.read('Track48.wav')
#cycles = 5
t = np.linspace(0, 1, 500)

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=fs,
                output=True)

plt.title('Orignal Audio')
plt.plot(audio)
plt.show()

audio_stream = audio.astype(np.int16).tostring()
stream.write(audio_stream)
stream.close()

# Second Audio 5s ---------------------------------------------------

p = pyaudio.PyAudio()
fs, audio5 = w.read('5s.wav')

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=fs,
                output=True)

plt.title('5s trained audio')
plt.plot(audio5)
plt.show()

audio_stream = audio5.astype(np.int16).tostring()
stream.write(audio_stream)
stream.close()

# Uniform mid tread Quantizer  ---------------------------------------

data = audio
step = (float(np.max(data)) - float(np.min(data)))/(2**4-1)
audioQuant = np.round(data/(step)) * step

de_quantization_tread = audioQuant*step

plt.plot(de_quantization_tread)
plt.title('        Mid Tread uniform quantized audio with quantization nosie ')
plt.show()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True,
                frames_per_buffer=1024)

audio_play = de_quantization_tread.astype('float32').tostring()
stream.write(audio_play)
stream.stop_stream()
stream.close()
p.terminate()