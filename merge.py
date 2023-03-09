import wave
from scipy.io import wavfile
import numpy as np


newFile = []

def appendFilePart(fileName, start, end=None):

    filePath = "./Audio/" + fileName + ".wav"
    f = wave.open(filePath)
    sampleRate = f.getframerate()
    frames = f.getnframes()
    _, samples = wavfile.read(filePath)


    if end is not None:
        for sample in samples[int(sampleRate*start):int(sampleRate*end)]:
            newFile.append(int(sample))
    else:
        for sample in samples[int(sampleRate*start):]:
            newFile.append(int(sample))





##### Hier Änderungen vornehmen #####

appendFilePart("PinkPanther60dynamic5000", 0, 30)
appendFilePart("PinkPanther60clipping5000", 30, 50)
appendFilePart("PinkPanther60normalized", 50)

fileName = "Test"

#####################################





array = np.ndarray((len(newFile),), buffer =np.array(newFile), dtype=int)

wavfile.write("./Audio/" + fileName + ".wav", 22050, array.astype(np.int16))
