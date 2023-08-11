# Langzizhixin Wanderer's Heart Technology 
# Double_Talker
This code is only used to demonstrate the loop driven dual digital human on the same screen, coupled with a framework for post processing ultra division. The code uses a WAv2lip loop to drive a dual digital human on the same screen, train a high-definition model, perform streaming processing, strengthen hardware, and do not perform post processing. It can be used for real-time live streaming of dual digital humans. It is also possible to replace WAv2lip with other digital human driven projects based on this framework. Among them, videos 1-6 are pre recorded silent videos for two people, and audio 1-6 is pre prepared speaking audio.
1. Upload the recorded dual video materials and audio separately to the temp in advance_ Video and input_ Audio.
2. The recording of this dual digital human material is crucial, as is the audio and video cutting.
3. The video processing speed is directly related to the GPU performance. If live streaming is required, it is necessary to perform streaming processing and use high-performance GPUs.
4. CodeFormer has a slow speed in supergrading, and those who do not have high requirements for digital human videos can skip supergrading or switch to GFPGAN for supergrading.
5. Variables are not used in the code, you need to write them yourself.

## Inference  
### Please click on the Colab link below to inference.
[![Open In Colab][colab-badge]][colab-notebook]
[colab-notebook]: <https://colab.research.google.com/github/langzizhixin/Double_Talker/blob/main/Double_Talker.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
***
## Useful links:
https://github.com/sczhou/CodeFormer
https://github.com/Rudrabha/Wav2Lip
### 
### 
***
### Project  made by Lu Rui from Langzizhixin Technology company in Chengdu, China.
###  Code 2023
