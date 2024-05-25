##### This package is still in development and may be slow in installation

<img align="center" src="figures/apollo_logo.png">

-----------------

# Apollo: Illuminating the Path of Multimodal Understanding with Vision, Text, and Audio 

[![License](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://github.com/VerbaNexAI/APOLLO.AI/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-red)](https://github.com/VerbaNexAI/APOLLO.AI/issues)
[![Python Version](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)

In ancient Greece, Apollo, the god of music, truth and prophecy, known for his golden lyre, was requested by Argus, the all-seeing giant, to play his divine music. Argus was soothed into sleep and Pythia, the hish priestess of Apollo's temple in Delphi, experienced enchanced phophetic abilities.

Apollo is a python package that provides three different channels: Audio (Lyre), Text (Pythia) and Vision (Argus), making it faster to develop complex apps with different services and utility functions for all three channels at once. In addition to this, we provide our own models into the scene for Text processing and Syllabification which is one of the strengths of the package, the Vision part is composed of various tools such as Head Analysis, Part Indices and more for a complete diagnostic in motor patterns, facial movements and statistical analysis. 

##### This package is under testing and development.

## Contents
- [Languages](#languages)
- [Behind Apollo](#behind-apollo)
- [What Does](#what-does)
- [Case Study](#case-study)

## Languages 
| Available Languages |
|---------------------|
| Spanish Latin American ('spa-ltn') |


## Behind Apollo
A brief introduction of our goal

The research centers around identifying specific motor patterns in children with dyspraxia, it is crucial to trace and document the landmarks of facial movements to help us gain deeper understanding of the unique characteristics of each children. For the statistical analysis will help to explain the difference between different groups (normal movements and dyspraxia), we aim to uncover patterns that will provide the necessary insights in this study. Additionally, in this journey we pretend to study deeper into the phonoarticulatory organs via audio and speech-to-text processing in order to study at a lower level the sentiment and emotion.

This research is of utmost importance as it contributes to a better understanding of dyspraxia and holds the potential to lead to the development of more specific and effective treatments for children who suffer from it. We want to emphasize our commitment to adhering to all ethical guidelines and ensuring the privacy of all research participants.

## What Does
Some of the things specifically Apollo is able to do

<img align="center" src="figures/apollo_parts.png">

We have divided apollo into three parts as described above.

- Argus is our vision package which is composed of varios utility functions and tools for analyzing not only facial movements but head movements and average motion on the head.
- Lyre is our sound analysis package powered as an interface for [Librosa](https://librosa.org/doc/latest/index.html) able to retrieve accurate and crucial information from sound waves and speech audio.
- Pythia is based on pure text analysis and comprehensive vectorization of characters, composed by multiple functions for word alignment and syllabification in the available languages. It also uses the [Faster-whisper](https://github.com/guillaumekln/faster-whisper) model for making transcriptions in chunks of audio.

### Keypoints to point out in this three parts

The text we've analyzed so far will not be processed in real-time due to our performance limitations, we have tried multiple times with different speech-to-text tools and until now we continue to trust whisper for our transcriptions tasks. 

Not only for text processing but for Lyre and the `recording_voice()` function which works as a type of buffer and helps us manage the audio into a Queue which the full process can be seen inside the apollo package documentation.

These three parts also form an amazing alignment and room for paralellization which it is possible to implement into application such as API's and Microservices, avoiding the limitations of the larger models inside the package which can be overwhelming sometimes due to the time of execution, tasks that is being focused on. 

- Extracting words from a corpus cleaned and without punctuation.
- Extracting syllables from word
- Align two transcriptions for missing words or extra words
- Check EYE and MOUTH movement in contrast of time
- Analyze with MEL, SPECTRAL, SIGNAL DOMAIN, ONSETS for audio files and recordings

## Case Study

FACS is a facial action coding system which has certain limitations as it can be bias and expensive to compute, this is why in the [Automated detection of smiles as dicrete episodes]([https://pubmed.ncbi.nlm.nih.gov/36205621/) paper propose an episode-wide analysis of individual smiles based on the action units of the upper face and lower face. The combined activation of zygomaticus major and the orbicularis oculi muscles determine and distinguishes between a genuine smile and "social" smiles, which are expressed during smiles of non-enjoyment. 

<img align="center" src="figures/apollo_case_study.png">

However, this instead of being a guide we take it as our starting point for the dyspraxia research, since we are not only analyzing the two muscles mentioned but, going further, the whole mouth and head movements in contrast with sounds made and sentiment of things said. To add more knowledge to our documentation here is a brief explanation of what dyspraxia is in the first place:

_"Dyspraxia, also known as Developmental Coordination Disorder (DCD), is a neurological condition that affects a child's ability to plan and coordinate physical movements. It primarily impacts motor skills, but it can also affect other areas of development, including language, perception, and social interactions"._

With this said, the experiment is based on 4 variables:
- Individual Points: For facial expresisons and movements.
- Spikes of movement: For statistical analysis of average movements on the head.
- Read Text: Transcriptions of specific corpuses.
- Phonesthemes (PETER): Analysis of language for further comprehension of things said by the subject.

Which we believe will be they key takeaways in the study with real subjects and out of these for the most important two:

### Individual Points

In terms of the computer vision approach we only used the [MediaPipe's](https://github.com/google/mediapipe) video analysis together with the OpenCV an open source library that provides a comprehensive set of tools, functions, and algorithms to enable computer vision and image processing tasks, making it a valuable resource for this approach.

For dyspraxia facial movement analysis, we tend to focus on opening and closing movements of the mouth, in order to analyze in which parts of the speech the person tends to struggle the most pronouncing specific words. To get this mouth opening movement we get the top and bottom lip mouth landmarks 0 and 17 respectively. With this landmarks we can analyze each frame of the video with OpenCV, and calculate the distance between those two landmarks, each one of them has and x and y position relative to the 2D plane of the face, measured in pixels. To calculate the distance at the beginning we used Euclidean distance, but this one had some sort of bias when normalizing the distance from pixels to millimeters, so to fix this we decided that the best approach was the *ChebyShev* distance, with this when normalizing it, the results were more accurate. Also, to visualize the results we plotted the distances in terms of the timestamps of the video using *Savitzky-Golay filter* given by the Scipy library to smoothen the result curve.

In addition, at the beginning, to have a more sustainable approach, the usage of a Fourier Transform to get the frequency for the mouth opening was accepted but once the curve was correctly smoothed and the data was as clean as possible, because of the low frequency of recording in the video this approach was rejected.

### Phonesthemes (PETER)

Studying the spanish language refers to an extensive knowledge of phonology and syntax, in contrast, the analysis of phonetic segments as categorical units helps us find the similarities between them (syllables (phonesthemes)), PETER is our proposed phonestheme model for understanding in-depth the spanish language, this model serves as the last part of the research providing insightful information connecting the facial points with the spikes of movement in the subject of the research. 

<h6>The architecture of this model is in the works.</h6>
