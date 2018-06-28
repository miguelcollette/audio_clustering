import audioop
import wave
import math
import struct
import numpy as np
import librosa
import scipy
import sklearn

def extract_features(x, fs):
  zcr = librosa.zero_crossings(x).sum()
  energy = scipy.linalg.norm(x)
  return [zcr, energy]


class audio_file:
  def __init__(self, path, name):
    self.path = path
    self.name = name
    self.average = 0
    self.average_peak_to_peak = 0
    self.main_freq=0
    self.standard_deviation=0
    self.label = -1
    self.silence_time = 0
    self.lef = 0
    self.zcr = 0
    
  def analyse(self):
    y, sr = librosa.load(self.path)
    self.zcr = librosa.feature.zero_crossing_rate(y).mean()
    rms = librosa.feature.rmse(y=y)[0]
    count = 0
    average = float(rms.mean())/2.0
    #print(len(rms))
    for val in rms:
      if val < average:
        count += 1
    self.lef = float(count) / len(rms)
    print("values : {} {}".format(self.zcr, self.lef))

    #onset_frames = librosa.onset.onset_detect(x, sr=fs, delta=0.04, wait=4)
    #onset_times = librosa.frames_to_time(onset_frames, sr=fs)
    #onset_samples = librosa.frames_to_samples(onset_frames)
    #
    #frame_sz = fs*0.090
    #features = numpy.array([extract_features(x[i:int(i+frame_sz)], fs) for i in onset_samples])
    #min_max_scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
    # = features_scaled
    #audio = wave.open(self.path, 'rb')
    #n_frames = audio.getnframes()
    #raw_audio = audio.readframes(n_frames)
    #width = audio.getsampwidth()
    #self.average = audioop.avg(raw_audio,width)
    #print(self.average)
    #self.average_peak_to_peak = audioop.avgpp(raw_audio,width)
    #print(self.average_peak_to_peak)
    #print("")
    #frate = audio.getframerate()
    #raw_audio = audioop.bias(raw_audio, width, -1*audioop.avg(raw_audio, width))
    #data = np.array(struct.unpack('{n}h'.format(n=n_frames), raw_audio))
    #w = np.fft.fft(data)
    #freqs = np.fft.fftfreq(len(w))
    #idx = np.argmax(np.abs(w))
    #freq = freqs[idx]
    #self.main_freq = abs(freq * frate)
    #audio.rewind()
    #variance = 0
    #for i in range(n_frames):
    #  frame = audio.readframes(1)
    #  val = audioop.avg(frame, width)
    #  variance+=(val - self.average)**2
    #variance = variance / float(n_frames)
    #self.standard_deviation = math.sqrt(variance)
    #audio.rewind()
    #count = 0
    #for i in range(n_frames):
    #  frame = audio.readframes(1)
    #  val = audioop.avg(frame, width)
    #  if val <0.1*abs(self.average) and val > -0.1*abs(self.average):
    #    count += 1
    #print(count)
    #self.silence_time = count
    #audio.close()
   
  def set_label(self,label):
self.label=label
