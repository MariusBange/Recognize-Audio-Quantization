# Recognize-Audio-Quantization

### Invastigate a given .wav file

* Input is a .wav file.
* Extract duration, sample rate, value range and percentage of realized values.
* Display histograms for the entire file and for chosen parts of it.
* Check parts of the file for normalization, dynamic range compression and clipping. After the check, a second window will show the results.
  * Checking for dynamic range compression takes a long time, so the results for single seconds are additionaly returned in the console.


### Apply operations to .wav file

In the lower half the operations mentioned above can be applied to the loaded file. For this, a threshold value and/or a factor must be selected. After creating the file, the corresponding histogram of the created file is displayed.


### Additional features

In the section on the top right of the window, the proportions of values in the value range and its size can be displayed. This option should give the user a sense of why no basis for a frequency analysis was found in my research for this project. The results are displayed in a window as well as saved in a file in the folder *LogFiles*.


### Provided sample files

The Audio folder contains audio files for testing the program. The files that will be loaded into the program will be loaded from this folder and also written into this folder. The file FullTest.wav contains a dynamic compression section (seconds 26-28) as well as a clipping section (43-45) and a normalized section (53-54).


### Other

It should be noted that the user input is not checked for correct format. This means that the application crashes with all unexpected inputs (e.g. letters instead of numbers) and with too large threshold values (threshold value larger than the largest sample value of the file) only copies the loaded file. When entering file names the extension .wav must be omitted!
