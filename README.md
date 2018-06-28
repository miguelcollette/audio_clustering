roblem description :

Given a set of audio files corresponding to music. We want to create clusters based on some analysis of these songs.
There is no anotation in the given data and no further precision is given regarding the clusters and their numbeer.

Ideas for solutions:

	- The first thing is to have a set of generic operations to select the files, process them, cluster them and give a final output that is readable and usable for the user, who does not necessarilly have technical knowledge of audio analysis.
- One first way to cluster will be a frequency analysis of the songs, generating the average frequency of each song as well as its range of frequency. Thus we can have clusters according to both parameters.
