# Audio classification

The idea is to solve an audio differenciation problem : given a set of audio files, without label, we want to return a pre-set number of clusters that differenciate them.
The first sub-problem will be a mix of music and speech that we want to differenciate. The second will be a set of music of several different genres.

# Solution - Python

## Version

I coded my solution in Python 3.6.

## Code

The code is divided into 3 files:
  - Audio_files.py : Contains the class audio_file, with the corresponding attributes, that are the name of the file, its path, and its features.
The class has a function analyse that will parse the audio file, and extract the features from it. Librosa is the library that has been used for the features extraction. It also has a setter for the labels got by the clustering algorithm.

  -audio_analysis.py : contains the useful functions to create clusters from a folder containing audio songs. The function analyse_folder will create the audio_file objects for each file in the folder, and analyse it to get its feature. It returns a list of list of features (one list per object) and a dictionnary that maps features to the corresponding audio_file object(s). Sklearn library has been used to perform K-means.
  
The function cluster takes a list of list of features and the corresponding dictionnary as an input, executes a k-means algorithm, and returns clusters containing the files' names. Finally compare_clusters_folders checks for each cluster how many files it has in common with each folder. Basically the idea is to see, if the cluster is supposed to represent this folder, what is the success rate.

  -audio_clustering.py : defines what the user will do, asks for the folder that needs clustering and executes the 3 functions of audio_analysis.py. If you use different folders, do change the folders to use for comparison.
  
An dataset music_speech is also given. The 3 folders of interest in it are music_wav where music files are stored, speech_wav where speech files are stored and all where the combination of the previous two is stored.
  
## Execution

The code is ready to use, one just needs to execute audio_clustering and will be prompted to enter the folder containing the files to cluster. This folder must contain audio files only. It will compute k lists, that represent the k clusters, and print the number of common files between these and the actual folders.

## Explaination

I tried first to use the dominant frequency of the song (obtained with a fast Fourier transform) as well as the standard deviation of the amplitude of the signal. The results were not good, around 60% of the files were well clustered, with two clusters only, it's relatively low.

In fact when one listens to speech, one can realise that one difference with music is that speech features more silent periods especially between sentences. So I computed the percentage of low energy frames in the file: this is done by getting the root mean-squared (RMS) of each frame of the song, and calculating the percentage of them that are below a threshold value (in our case the mean of the RMS across all the frames divided by 2). Using this feature only lead to better performances as more than 85% of the files were well clustered.


So far the work has only been done for one dataset, next step is first to add files from another dataset of speech and music and see if it puts them in the right clusters. Then  the idea is to apply it to different dataset and adapt the functions and features to cluster different genres of music.

## Results

The first dataset that I use is a mix of speech and music files (http://marsyasweb.appspot.com/download/data_sets/). Originally the files are in 2 folders: one for speech one for music, with 64 files each, and I created a all folder to mix the 2. This is the folder I gave as an input to create the clusters. After k-means has been run, my function returns the corresponding lists, containing the name of files in each cluster. I compared these with the original folders of the dataset and obtained the following:

Cluster 1 -> 65 files, 56 common with the music folder, 9 common with the speech one, so about 86% accuracy.

Cluster 2 -> 63 files, 55 common with the speech folder, 8 common with the music one, so about 87% accuracy.

## Comments

Using the percentage of low energy frame across the audio files allowed to get reasonably accurate clusters. But to be sure this is relevent we have to see whether keeping the same clusters, we can add files from another dataset and keep the same level of accuracy, which will be the next part of this work.

