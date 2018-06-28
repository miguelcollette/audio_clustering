import os
from audio_files import audio_file
from collections import defaultdict
from sklearn.cluster import KMeans
import sklearn

def analyse_folder(location):
  if not os.path.isdir(location):
    return("The directory does not exist",1)
    
  audio_list = []
  map_coords_objects = defaultdict(lambda:[])
  for filename in os.listdir(location):
    audio_sample = audio_file(location+"/"+filename, filename)
    audio_sample.analyse()
    coord = [audio_sample.lef]
    
    audio_list.append(coord)
    map_coords_objects[str(coord)].append(audio_sample)
  print(audio_list)
  return audio_list, map_coords_objects
  
def cluster(audio_list, map_coords_objects):
  n=2
  res = KMeans(n_clusters=n, n_init = 20, max_iter = 1000).fit(audio_list)
  cluster_list=res.labels_
  clusters = [[] for i in range(n)]
  for i in range(len(cluster_list)):
    for audio_file in map_coords_objects[str(audio_list[i])]:
      audio_file.set_label(cluster_list[i])
  for key in map_coords_objects.keys():
    for audio_file in map_coords_objects[key]:
      cluster_index = audio_file.label
      clusters[cluster_index].append(audio_file.name)
  return clusters
  
def compare_clusters_folders(folder_list, cluster_list):
  for cluster in cluster_list:
    for folder in folder_list:
      file_list = os.listdir(folder)
      x = len(list(set(cluster) & set(file_list)))
      print("with "+folder+": {} / {}".format(x, len(cluster)))
    print("\n")

