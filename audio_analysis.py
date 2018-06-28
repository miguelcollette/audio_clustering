import os

def analyse_audio():
  pass
  
def analyse_folder(location):
  if !os.path.isdir(location):
    return("The directory does not exist")
    
  audio_list = []
  for filename in os.listdir(location):
    audio_sample = audio_file(location+"/"+filename, filename)
    audio_sample.analyse()
audio_list.append(audio_sample)
