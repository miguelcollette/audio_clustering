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
    self.label = -1
    self.lef = 0
    self.zcr = 0
    #Some features might be added, even id they are not all in use at the same time, depending on the type of clustering we want to achieve.
    
  def analyse(self):
    y, sr = librosa.load(self.path)
    self.zcr = librosa.feature.zero_crossing_rate(y).mean()
    #zero crossing rate of the signal
    rms = librosa.feature.rmse(y=y)[0]
    #root mean squared of the signal
    count = 0
    threshold = float(rms.mean())/2.0
    #threshold defines when the value is considered to be a silent one.
    for val in rms:
      if val < threshold:
        count += 1
    self.lef = float(count) / len(rms)
    self.mfcc = librosa.feature.mfcc(y=y, sr=sr)
    #print(self.mfcc)

    
   
  def set_label(self,label):
    self.label=label
