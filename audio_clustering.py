from audio_analysis import *
import os

if __name__ == "__main__":
	print("Welcome, please provide a path to a folder you wish to create clusters for. The folder must contain audio files only")
	directory = input().strip()
	audio_list, map_coords_objects = analyse_folder(directory)
	clusters = cluster(audio_list, map_coords_objects)
	compare_clusters_folders(["./music_speech/music_wav", "./music_speech/speech_wav"], clusters)
#the list of folders has to be changed if we deal with other datasets
