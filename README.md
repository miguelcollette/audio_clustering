

Problem description :

Given a set of audio files of different style, the first set will be some music songs and some speech audio files . We want to create clusters based on some analysis of these files. There is no anotation in the given data and no further precision is given regarding the clusters and their numbeer.

Ideas for solutions:

- The first thing is to have a set of generic operations to select the files, process them, cluster them and give a final output that is readable and usable for the user, who does not necessarilly have technical knowledge of audio analysis.
- One first way to cluster will be with a basic frequency analysis of the audio file. We are using two dimensions for this analysis, one is the average frequency along the song, the other is the standard deviation along the song. From these we are using the K-means algorithm to create different clusters.


