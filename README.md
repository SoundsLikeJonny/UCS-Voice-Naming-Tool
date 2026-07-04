# UCS Voice Naming Tool [POC]
A tool to name audio recordings by analyzing the slate at the start of a file, and labeling the file metadata according to the Universal Category System.


UCS V8.1
https://www.dropbox.com/sh/l5jb1liog04ks1f/AADFiFLhQVBaWV8aCR1qNHUFa?dl=0
)
# Overview
## An average audio recordist workflow
When recording sound, one of the most hygenic things to do is record a slate; a one to two sentence description of what you're about to record.
Later, when you go to edit all of the sound files that you've recorded, you'll listen to the slate to remind yourself of the objects you were recording and the actions you were performing.
You make your edits, cut out bad takes, and then figure out how to label your files.
You label each file, one by one, according to some sort of naming standard (e.g. UCS), and export your files to your SFX library for usage late on in projects.

## What UCS-VNT is looking to solve.
In todays age, the UCS standard is a popular choice for naming, and several scripts exist to do this.
But in the recording through to the editing phase, these filenames will remain labelled in the same format the recording device chooses.
Some make more sense than others, but for myself it's either:
### A: some sort of date and time format
    202060304-4802756.wav
    202060304-4802924.wav
    202060304-4803433.wav
### Or B: some text I've entered in my recorder
    exterior, waves, beach, vancouver_001.wav 
    exterior, waves, beach, vancouver_002.wav 
    exterior, waves, beach, vancouver_003.wav 

When editing begins, even though we have an idea of all the things we recorded, it can be difficult to tell what the following sound is in the editing software without already having listened to the slate, and added a marker to the session.
<img width="709" height="200" alt="image" src="https://github.com/user-attachments/assets/b60be9f4-52e0-4eaf-9199-957e97285784" />


With the USC-VNT we're looking to introduce a file labeling step before the editing begins.
So that when you start your editing, you already have a UCS compliant filename.
And editing can look more like this.
<img width="1060" height="151" alt="image" src="https://github.com/user-attachments/assets/820359a1-85f6-43ef-ade0-e93f705d058b" />

## How it works
1. The user can setup some basic UCS details that will apply to all files (Creator ID, Source ID, User Data, etc.)
2. UCS-VNT can watch a folder and wait for new files, or the user can drop new files onto the tool.
3. UCS-VNT will read the audio files and convert the speech to text from the slate at the start of the file.
4. Files are labeled to a UCS compliant filename, and moved to a seperate folder to be used for editing.

# This repository is currently in development
Check out the [Dev Logs](https://github.com/SoundsLikeJonny/UCS-Voice-Naming-Tool/wiki/Dev-Logs) page to hear about current progress.
