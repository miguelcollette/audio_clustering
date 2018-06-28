# Audio classification

The idea is to solve an audio classification problem : given a set of audio files, without label, we want to return a pre-set number of clusters that classify them.
The first set will be a mix of music and speech. The second set will be a set of music of 10 different genres

## Design

	- The first thing is to have a set of generic operations to select the files, process them, cluster them and give a final output that is readable and usable for the user, who does not necessarilly have technical knowledge of audio analysis.
	- Then we need audio features that are relevent. First the dominant frequency was used: from a Fast Fourier Transform, we can get the signal component with the largest amplitude. Using this single feature as a parameter leads to roughly 60% of success rate, not tremendous considering that we only have 2 clusters, so random clustering should be around 50% itself.
	

Code explaination:
Audio_files.py : Contains the class audio_file, with the corresponding attributes, that are the name of the file, its path, and the features.
The class has a function analyse that will parse the audio file, and extract the features from it.

audio_analysis.py : contains the useful functions to create clusters from a folder containing audio songs. The function analyse_folder will create the audio_file objects for each file in the folder, and analyse it to get its feature. It returns a list of list of features (one list per object) and a dictionnary that maps features to the corresponding audio_file object(s).
The function cluster takes a list of list of features and the corresponding dictionnary as an input, executes a k-means algorithm, and returns clusters containing the files' names. Finally compare_clusters_folders checks for each cluster how many files it has in common with each folder. Basically the idea is to see, if the cluster is supposed to represent this folder, what is the success rate.

audio_clustering.py : defines what the user will do, asks for the folder that needs clustering and executes the 3 functions of audio_analysis.py



What features to try: spectral centroid, then maybe compute the percentage of silent moments across the file. Speech should have more silent times than music.
Try also the zero crossing rate, on FEATURE EXTRACTION FOR SPEECH AND MUSIC DISCRIMINATION it seems that the crossing rate of speech is higher than the one of music.
Check freesounds.org for further dataset.

