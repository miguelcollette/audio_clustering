import audioop
import wave
import math
import struct
import numpy as np

class audio_file:
  def __init__(self, path, name):
    self.path = path
    self.name = name
    self.average = 0
    self.main_freq=0
    self.standard_deviation=0
    self.label = -1
    
  def analyse(self):
    audio = wave.open(self.path, 'rb')
    n_frames = audio.getnframes()
    raw_audio = audio.readframes(n_frames)
    width = audio.getsampwidth()
    self.average = audioop.avg(raw_audio,width)
    frate = audio.getframerate()
    raw_audio = audioop.bias(raw_audio, width, -1*audioop.avg(raw_audio, width))
    data = np.array(struct.unpack('{n}h'.format(n=n_frames), raw_audio))
    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w))
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    self.main_freq = abs(freq * frate)
    audio.rewind()
    variance = 0
    for i in range(n_frames):
      frame = audio.readframes(1)
      val = audioop.avg(frame, width)
      variance+=(val - self.average)**2
    variance = variance / float(n_frames)
    self.standard_deviation = math.sqrt(variance)
    audio.close()
   
  def set_label(self,label):
self.label=label
