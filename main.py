import wave
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import math
from PyQt5 import QtWidgets
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        self.mainWidget = QtWidgets.QWidget()
        self.gui = Gui(self)
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.addWidget(self.gui)
        self.mainWidget.setLayout(self.hLayout)
        self.setCentralWidget(self.mainWidget)
        self.show() # Show the GUI



class Gui(QtWidgets.QGroupBox):

    def __init__(self, parent):
        super(Gui, self).__init__()

        self.setFixedSize(1500, 750)
        # self.setTitle("Audio Quantisierung erkennen")
        self.setStyleSheet("""
            QGroupBox {
                border: 2px solid lightgray;
                border-radius: 5px;
                padding: 5px
            }

            QGroupBox::title {
                subcontrol-origin: top;
                subcontrol-position: top center; /* position at the top center */
                padding: 1 5px;
                background-color: lightgray;
            }""")

        self.grid = QtWidgets.QGridLayout()
        self.space1 = QtWidgets.QLabel()
        self.space2 = QtWidgets.QLabel()
        self.space2.setStyleSheet("background-color: lightgray")
        self.space2.setFixedSize(5, 712)
        self.space3 = QtWidgets.QLabel()
        self.space4 = QtWidgets.QLabel()
        self.space5 = QtWidgets.QLabel()
        self.space5.setStyleSheet("background-color: lightgray")
        self.space5.setFixedSize(5, 712)
        self.space6 = QtWidgets.QLabel()
        self.space7 = QtWidgets.QLabel()
        self.space7.setFixedSize(1462, 15)
        self.space8 = QtWidgets.QLabel()
        self.space8.setStyleSheet("background-color: lightgray")
        self.space8.setFixedSize(1462, 5)
        self.space9 = QtWidgets.QLabel()
        self.space9.setFixedSize(1462, 15)
        self.fileLabel = QtWidgets.QLabel("Name der Audiodatei:")
        self.fileLabel.setFixedSize(300, 50)
        self.fileInput = QtWidgets.QLineEdit()
        self.fileInput.setFixedSize(400, 25)
        self.loadButton = QtWidgets.QPushButton(text="Datei laden")
        self.loadButton.setFixedSize(400, 50)
        self.loadButton.clicked.connect(self.loadFile)
        self.startInput = QtWidgets.QLineEdit()
        self.startInput.setPlaceholderText("Von Sekunde...")
        self.startInput.setFixedSize(100, 25)
        self.endInput = QtWidgets.QLineEdit()
        self.endInput.setPlaceholderText("bis Sekunde...")
        self.endInput.setFixedSize(100, 25)
        self.histButton = QtWidgets.QPushButton(text="Histogram anzeigen")
        self.histButton.setFixedSize(200, 50)
        self.histButton.clicked.connect(self.showHistogram)
        self.startInput2 = QtWidgets.QLineEdit()
        self.startInput2.setPlaceholderText("Von Sekunde...")
        self.startInput2.setFixedSize(100, 25)
        self.endInput2 = QtWidgets.QLineEdit()
        self.endInput2.setPlaceholderText("bis Sekunde...")
        self.endInput2.setFixedSize(100, 25)
        self.checkButton = QtWidgets.QPushButton(text="Datei überprüfen")
        self.checkButton.setFixedSize(200, 50)
        self.checkButton.clicked.connect(self.checkFile)
        self.nameLabel = QtWidgets.QLabel("Name: ")
        self.nameLabel.setFixedSize(400, 50)
        self.durationLabel = QtWidgets.QLabel("Dauer: ")
        self.durationLabel.setFixedSize(400, 50)
        self.frameRateLabel = QtWidgets.QLabel("Samplerate: ")
        self.frameRateLabel.setFixedSize(400, 50)
        self.rangeLabel = QtWidgets.QLabel("Wertebereich: ")
        self.rangeLabel.setFixedSize(400, 50)
        self.percentageLabel = QtWidgets.QLabel("Wertebereich ausgeschöpft zu ")
        self.percentageLabel.setFixedSize(400, 50)
        self.sizeLabel = QtWidgets.QLabel("Größe des Suchfensters (in Sekunden):")
        self.sizeInput = QtWidgets.QComboBox()
        self.sizeInput.addItems(["0.5", "1", "2", "3", "5", "10"])
        self.sizeInput.setFixedSize(400, 25)
        self.newNameLabel1 = QtWidgets.QLabel("Name der neuen Datei:")
        self.newNameLabel1.setFixedSize(400, 50)
        self.newNameInput1 = QtWidgets.QLineEdit()
        self.newNameInput1.setFixedSize(400, 25)
        self.calculateButton = QtWidgets.QPushButton(text="Häufigkeiten berechnen")
        self.calculateButton.setFixedSize(400, 50)
        self.calculateButton.clicked.connect(self.calculateFrequency)
        self.factorLabel = QtWidgets.QLabel("Faktor für Lautstärkeänderung:")
        self.factorLabel.setFixedSize(400, 25)
        self.factorInput = QtWidgets.QComboBox()
        self.factorInput.addItems(["0.1", "0.25", "0.33", "0.5", "0.66", "0.75", "1.5", "2"])
        self.factorInput.setFixedSize(400, 50)
        self.newNameLabel2 = QtWidgets.QLabel("Name der neuen Datei:")
        self.newNameLabel2.setFixedSize(400, 25)
        self.newNameInput2 = QtWidgets.QLineEdit()
        self.newNameInput2.setFixedSize(400, 25)
        self.linearButton = QtWidgets.QPushButton(text="Lineare Lautstärkeänderung durchführen")
        self.linearButton.setFixedSize(400, 50)
        self.linearButton.clicked.connect(self.linearVolumeChange)
        self.factorLabel2 = QtWidgets.QLabel("Schwellwert:")
        self.factorLabel2.setFixedSize(400, 25)
        self.factorInput2 = QtWidgets.QLineEdit()
        self.factorInput2.setFixedSize(400, 25)
        self.factorLabel3 = QtWidgets.QLabel("Faktor:")
        self.factorInput3 = QtWidgets.QComboBox()
        self.factorInput3.addItems(["0.5", "0.33", "0.25", "0.2", "0.1", "0.05"])
        self.factorInput3.setFixedSize(400, 25)
        self.newNameLabel3 = QtWidgets.QLabel("Name der neuen Datei:")
        self.newNameLabel3.setFixedSize(400, 25)
        self.newNameInput3 = QtWidgets.QLineEdit()
        self.newNameInput3.setFixedSize(400, 25)
        self.dynamicButton = QtWidgets.QPushButton(text="Dynamik-Kompression durchführen")
        self.dynamicButton.setFixedSize(400, 50)
        self.dynamicButton.clicked.connect(self.dynamicCompression)
        self.limitLabel = QtWidgets.QLabel("Maximalwert für Clipping:")
        self.limitInput = QtWidgets.QLineEdit()
        self.limitInput.setFixedSize(400, 25)
        self.newNameLabel4 = QtWidgets.QLabel("Name der neuen Datei:")
        self.newNameLabel4.setFixedSize(400, 25)
        self.newNameInput4 = QtWidgets.QLineEdit()
        self.newNameInput4.setFixedSize(400, 25)
        self.clippingButton = QtWidgets.QPushButton(text="Clipping durchführen")
        self.clippingButton.setFixedSize(400, 50)
        self.clippingButton.clicked.connect(self.clipping)
        self.messageBox = None

        for button in [self.histButton, self.checkButton, self.calculateButton, self.linearButton, self.dynamicButton, self.clippingButton]:
            button.setEnabled(False)


        self.grid.addWidget(self.fileLabel, 0, 0, 1, 21)
        self.grid.addWidget(self.fileInput, 1, 0, 1, 21)
        self.grid.addWidget(self.loadButton, 2, 0, 1, 21)
        self.grid.addWidget(self.startInput, 3, 0, 1, 5)
        self.grid.addWidget(self.endInput, 3, 5, 1, 5)
        self.grid.addWidget(self.histButton, 3, 10, 1, 11)
        self.grid.addWidget(self.startInput2, 4, 0, 1, 5)
        self.grid.addWidget(self.endInput2, 4, 5, 1, 5)
        self.grid.addWidget(self.checkButton, 4, 10, 1, 11)
        self.grid.addWidget(self.space1, 0, 21, 15, 1)
        self.grid.addWidget(self.space2, 0, 22, 15, 1)
        self.grid.addWidget(self.space3, 0, 23, 15, 1)

        self.grid.addWidget(self.nameLabel, 0, 24, 1, 21)
        self.grid.addWidget(self.durationLabel, 1, 24, 1, 21)
        self.grid.addWidget(self.frameRateLabel, 2, 24, 1, 21)
        self.grid.addWidget(self.rangeLabel, 3, 24, 1, 21)
        self.grid.addWidget(self.percentageLabel, 4, 24, 1, 21)
        self.grid.addWidget(self.space4, 0, 45, 15, 1)
        self.grid.addWidget(self.space5, 0, 46, 15, 1)
        self.grid.addWidget(self.space6, 0, 47, 15, 1)

        self.grid.addWidget(self.sizeLabel, 0, 48, 1, 21)
        self.grid.addWidget(self.sizeInput, 1, 48, 1, 21)
        self.grid.addWidget(self.newNameLabel1, 2, 48, 1, 21)
        self.grid.addWidget(self.newNameInput1, 3, 48, 1, 21)
        self.grid.addWidget(self.calculateButton, 4, 48, 1, 21)
        self.grid.addWidget(self.space7, 5, 0, 1, 69)
        self.grid.addWidget(self.space8, 6, 0, 1, 69)
        self.grid.addWidget(self.space9, 7, 0, 1, 69)

        self.grid.addWidget(self.factorLabel, 10, 0, 1, 21)
        self.grid.addWidget(self.factorInput, 11, 0, 1, 21)
        self.grid.addWidget(self.newNameLabel2, 12, 0, 1, 21)
        self.grid.addWidget(self.newNameInput2, 13, 0, 1, 21)
        self.grid.addWidget(self.linearButton, 14, 0, 1, 21)

        self.grid.addWidget(self.factorLabel2, 8, 24, 1, 21)
        self.grid.addWidget(self.factorInput2, 9, 24, 1, 21)
        self.grid.addWidget(self.factorLabel3, 10, 24, 1, 21)
        self.grid.addWidget(self.factorInput3, 11, 24, 1, 21)
        self.grid.addWidget(self.newNameLabel3, 12, 24, 1, 21)
        self.grid.addWidget(self.newNameInput3, 13, 24, 1, 21)
        self.grid.addWidget(self.dynamicButton, 14, 24, 1, 21)

        self.grid.addWidget(self.limitLabel, 10, 48, 1, 21)
        self.grid.addWidget(self.limitInput, 11, 48, 1, 21)
        self.grid.addWidget(self.newNameLabel4, 12, 48, 1, 21)
        self.grid.addWidget(self.newNameInput4, 13, 48, 1, 21)
        self.grid.addWidget(self.clippingButton, 14, 48, 1, 21)

        self.setLayout(self.grid)


        self.fileName = None
        self.filePath = None
        self.channels = None
        self.sampleRate = None
        self.bitDepth = None
        self.bitRate = None
        self.frames = None
        self.duration = None
        self.samples = None




    def loadFile(self):

        self.fileName = self.fileInput.text()
        self.filePath = "./Audio/" + self.fileName + ".wav"
        try:
            f = wave.open(self.filePath)
        except IOError:
            self.fileInput.setStyleSheet("border: 1px solid red;")
            return
        self.fileInput.setStyleSheet("")
        #Audio head parameters
        self.channels = f.getnchannels()
        self.sampleRate = f.getframerate()
        self.bitDepth = f.getsampwidth() * 8
        self.bitRate = self.sampleRate * self.bitDepth * self.channels / 1000
        self.frames = f.getnframes()
        self.duration = self.frames / float(self.sampleRate)
        _, self.samples = wavfile.read(self.filePath) # reading wave file.

        maxSample = 0
        minSample = 0
        frequency = {}

        missingValues = 0

        for sample in self.samples:

            key = str(sample)

            if key in frequency:
                frequency[key] = frequency[key] + 1

            else:
                frequency[key] = 1

            if sample > maxSample:
                maxSample = int(sample)

            if sample < minSample:
                minSample = int(sample)

        for j in range(minSample, maxSample+1):

            if str(j) not in frequency:
                missingValues += 1

        rangeSize = maxSample - minSample + 1
        percentage = (100-round(missingValues / (rangeSize) * 100, 2))

        self.factorLabel2.setText("Schwellwert (<" + str(max(minSample*-1, maxSample)) + "):")
        self.limitLabel.setText("Maximalwert für Clipping (<" + str(max(minSample*-1, maxSample)) + "):")
        self.nameLabel.setText("Name: " + self.fileName)
        self.durationLabel.setText("Dauer: " + str(self.duration) + " Sekunden")
        self.frameRateLabel.setText("Samplerate: " + str(self.sampleRate) + "Hz")
        self.rangeLabel.setText("Wertebereich: " + str([minSample, maxSample]))
        self.percentageLabel.setText("Wertebereich ausgeschöpft zu " + str(percentage) + "% (" + str(rangeSize-missingValues) + "/" + str(rangeSize) + ")")

        for button in [self.histButton, self.checkButton, self.calculateButton, self.linearButton, self.dynamicButton, self.clippingButton]:
            button.setEnabled(True)




    def showHistogram(self):

        start = int(self.startInput.text())*self.sampleRate if self.startInput.text() != "" else 0
        end = int(self.endInput.text())*self.sampleRate if self.endInput.text() != "" else 0
        samples = None
        if end == 0:
            samples = self.samples[start:]
        else:
            samples = self.samples[start:end]
        bins = int(math.ceil(math.sqrt(abs(min(samples))+max(samples)+1)))

        (_, _, _) = plt.hist(samples, bins=bins)  # arguments are passed to np.histogram.

        title = self.fileName + " " + self.startInput.text() + "-" + self.endInput.text() + ".wav"

        plt.title(title)
        plt.xlabel('Samplewerte')
        plt.ylabel('Häufigkeit')
        plt.show()



    def checkFile(self):



        stepSize = self.sampleRate

        steps = None

        start, end = (self.startInput2.text(), self.endInput2.text())

        if start == "" and end == "":
            steps = range(int(math.floor(len(self.samples)/stepSize)))
        elif start != "" and end == "":
            steps = range(int(start), int(math.floor(len(self.samples)/stepSize)))
        elif start == "" and end != "":
            steps = range(0, int(end))
        elif start != "" and end != "":
            steps = range(int(start), int(end))

        samples = self.samples[steps.start*stepSize:(steps.stop)*stepSize] if self.channels == 1 else self.samples[0][steps.start*stepSize:steps.stop*stepSize]

        isNormalized = None
        dynamicCompressionAbnormalities = []
        dynamicCompressionThresholds = []
        clippingAbnormalities = []
        clippingThresholds = []

        for i in steps:

            c = self.samples[i*stepSize:(i+1)*stepSize] if self.channels == 1 else self.samples[0][i*stepSize:(i+1)*stepSize]

            print("\n", i, "-", i+1)

            normalized = -(2**self.bitDepth) / 2 in c or (2**self.bitDepth ) / 2 - 1 in c
            print("Normalisiert" if normalized else "Nicht normalisiert")

            isDynamicCompressed = self.isDynamicCompressed(c, i)

            if isDynamicCompressed:
                dynamicCompressionAbnormalities.append((i, i+1))
                dynamicCompressionThresholds.append(isDynamicCompressed)
                print("Dynamik-Kompression im Bereich", isDynamicCompressed)
            else:
                print("Keine Dynamik-Kompression")

            isClipping, amplitude = self.isClipping(c)

            if isClipping:

                if clippingAbnormalities and clippingAbnormalities[-1][1] == i:
                    clippingAbnormalities[-1] = (clippingAbnormalities[-1][0], i+1)

                else:
                    clippingAbnormalities.append((i, i+1))
                    clippingThresholds.append(abs(amplitude))

                print("Clipping bei", abs(amplitude))
            else:
                print("Kein Clipping")

        results = ["Ergebnis Überprüfung " + self.fileName + ".wav Sekunden " + str(steps.start) + "-" + str(steps.stop), "", "Lineare Lautstärkeänderung:"]

        results.extend(["Der untersuchte Abschnitt ist normalisiert. Daraus lässt sich schließen, dass die Lautstärke des untersuchten Abschnitts höchstwahrscheinlich linear verändert wurde.", ""] if isNormalized else ["Der untersuchte Abschnitt ist nicht normalisiert. Somit wurde die Lautstärke eher nicht linear verändert.", ""])

        results.extend(["Dynamik-Komression:"] if dynamicCompressionAbnormalities else ["Dynamik-Kompression:", "Es wurden keine Anzeichen für eine Dynamik-Kompression gefunden"])

        for i in range(len(dynamicCompressionAbnormalities)):

            time = dynamicCompressionAbnormalities[i]
            amplitude = str(dynamicCompressionThresholds[i])
            results.append("Auffälligkeiten bei Sekunde " + str(time[0]) + " bis " + str(time[1]) + ". Voraussichtlicher Bereich des Schwellwerts: " + amplitude)

        results.extend(["", "Clipping:"] if clippingAbnormalities else ["", "Clipping:", "Es wurden keine Anzeichen für Clipping gefunden"])

        for i in range(len(clippingAbnormalities)):

            time = clippingAbnormalities[i]
            amplitude = str(clippingThresholds[i])

            results.append("Auffälligkeiten bei Sekunde " + str(time[0]) + " bis " + str(time[1]) + ". Voraussichtlicher Schwellwert: " + amplitude)

        self.messageBox = ScrollMessageBox(results)
        self.messageBox.exec_()



    def calculateFrequency(self):

        stepSize = int(float(self.sizeInput.currentText()) * self.sampleRate)

        steps = int(math.floor(len(self.samples)/stepSize))

        logFile = [self.fileName]

        sizeToRate = {}

        for i in range(steps):

            c = self.samples[i*stepSize:(i+1)*stepSize] if self.channels == 1 else self.samples[0][i*stepSize:(i+1)*stepSize]

            frequency = {}

            maxSample = 0
            minSample = 0
            count = 0

            for sample in c:

                key = str(sample)

                if key in frequency:
                    frequency[key] = frequency[key] + 1

                else:
                    frequency[key] = 1

                if sample > maxSample:
                    maxSample = int(sample)

                if sample < minSample:
                    minSample = int(sample)

                count += 1

            missingValues = 0

            for j in range(minSample, maxSample+1):

                if str(j) not in frequency:
                    missingValues += 1

            rangeSize = maxSample - minSample + 1
            sizeToRate[rangeSize] = (missingValues,  round(missingValues / (rangeSize), 2))

        keys = sorted(sizeToRate.keys())

        for key in keys:
            logFile.append(str(key) + " " + str(sizeToRate[key]))

        with open('./logFiles/' + self.newNameInput1.text() + '.txt', 'w') as f:

            for line in logFile:
                f.write(line)
                f.write('\n')

        self.messageBox = ScrollMessageBox(logFile)
        self.messageBox.exec_()



    def linearVolumeChange(self):

        newFile = []

        for sample in self.samples:
            newFile.append(int(round(sample*float(self.factorInput.currentText()))))

        array = np.ndarray((self.frames,), buffer =np.array(newFile), dtype=int)

        wavfile.write("./Audio/" + self.newNameInput2.text() + ".wav", self.sampleRate, array.astype(np.int16))

        (_, _, _) = plt.hist(newFile, bins='auto')  # arguments are passed to np.histogram.

        title = self.newNameInput2.text() + ".wav"

        plt.title(title)
        plt.xlabel('Amplitude')
        plt.ylabel('Häufigkeit (Frequency)')
        plt.show()



    def dynamicCompression(self):

        newFile = []
        threshold = int(self.factorInput2.text())

        for sample in self.samples:

            if sample > threshold:
                newFile.append(int(round(threshold + (sample-threshold)*float(self.factorInput.currentText()))))

            elif sample < -threshold:
                newFile.append(int(round(-threshold + (sample+threshold)*float(self.factorInput.currentText()))))

            else:
                newFile.append(int(sample))

        array = np.ndarray((self.frames,), buffer =np.array(newFile), dtype=int)

        wavfile.write("./Audio/" + self.newNameInput3.text() + ".wav", self.sampleRate, array.astype(np.int16))

        (_, _, _) = plt.hist(newFile, bins='auto')  # arguments are passed to np.histogram.

        title = self.newNameInput3.text() + ".wav"

        plt.title(title)
        plt.xlabel('Amplitude')
        plt.ylabel('Häufigkeit (Frequency)')
        plt.show()



    def clipping(self):

        newFile = []

        for sample in self.samples:

            if sample > int(self.limitInput.text()):
                newFile.append(int(self.limitInput.text()))

            elif sample < -int(self.limitInput.text()):
                newFile.append(-int(self.limitInput.text()))

            else:
                newFile.append(int(sample))

        array = np.ndarray((self.frames,), buffer =np.array(newFile), dtype=int)

        wavfile.write("./Audio/" + self.newNameInput4.text() + ".wav", self.sampleRate, array.astype(np.int16))

        (_, _, _) = plt.hist(newFile, bins='auto')  # arguments are passed to np.histogram.

        title = self.newNameInput4.text() + ".wav"

        plt.title(title)
        plt.xlabel('Amplitude')
        plt.ylabel('Häufigkeit (Frequency)')
        plt.show()



    def isDynamicCompressed(self, samples, i):

        frequency = {}

        for sample in samples:

            if sample in frequency:
                frequency[sample] = frequency[sample] + 1

            else:
                frequency[sample] = 1

        keys = sorted(frequency.keys())

        lastAvg = None
        secondLastAvg = None

        thresholds = []
        stepSize = int(math.ceil(math.sqrt(abs(int(min(samples))) + int(max(samples)) + 1)))

        for start in range(1, keys[-1], stepSize):

            avg = 0
            values = 0

            for amplitude in range(start, start+stepSize, 1):

                if amplitude in keys:
                    values += frequency[amplitude]

            avg = values / stepSize

            if lastAvg == None:
                lastAvg = avg
                continue

            if secondLastAvg == None:
                secondLastAvg = lastAvg
                lastAvg = avg
                continue

            if thresholds and avg > secondLastAvg:
                break
            elif thresholds:
                thresholds = []

            if lastAvg * 2 < avg and lastAvg > 1/30 and start + stepSize < keys[-1]:
                thresholds.append([start, start+stepSize-1])

            secondLastAvg = lastAvg
            lastAvg = avg

        lastAvg = None
        secondLastAvg = None


        for start in range(-1, keys[0], -stepSize):

            avg = 0
            values = 0

            for amplitude in range(start, start-stepSize, -1):

                if amplitude in keys:
                    values += frequency[amplitude]

            avg = values / stepSize

            if lastAvg == None:
                lastAvg = avg
                continue

            if secondLastAvg == None:
                secondLastAvg = lastAvg
                lastAvg = avg
                continue

            if len(thresholds) == 2 and avg > secondLastAvg:
                break
            elif len(thresholds) == 2:
                thresholds.pop()

            if lastAvg * 2 < avg and lastAvg > 1/30 and start - stepSize > keys[0]:
                thresholds.append([start, start-stepSize+1])

            secondLastAvg = lastAvg
            lastAvg = avg

        compressionRange = []

        if len(thresholds) == 2 and thresholds[0][0] + thresholds[1][0] == 0 and thresholds[0][1] + thresholds[1][1] == 0:
            compressionRange = [abs(thresholds[0][0]), abs(thresholds[0][1])]

        return compressionRange



    def isClipping(self, samples):

        minValue = -(2**self.bitDepth) / 2
        maxValue = (2**self.bitDepth ) / 2 - 1

        maxSamples = [[0, 0], [0, 0]]

        minSamples = [[0, 0], [0, 0]]

        for sample in samples:

            if sample > minValue and sample < maxValue:

                if sample > maxSamples[0][0]:
                    maxSamples[0] = [sample, 1]

                elif sample == maxSamples[0][0]:
                    maxSamples[0][1] += 1

                elif sample < minSamples[0][0]:
                    minSamples[0] = [sample, 1]

                elif sample == minSamples[0][0]:
                    minSamples[0][1] += 1

        for sample in self.samples:

            if sample > maxSamples[1][0] and sample < maxSamples[0][0]:
                maxSamples[1] = [sample, 1]

            elif sample == maxSamples[1][0]:
                maxSamples[1][1] += 1

            elif sample < minSamples[1][0] and sample > minSamples[0][0]:
                minSamples[1] = [sample, 1]

            elif sample == minSamples[1][0]:
                minSamples[1][1] += 1

        return (True, max(maxSamples[0][0], abs(minSamples[0][0]))) if maxSamples[0][1] > maxSamples[1][1] * 10 or minSamples[0][1] > minSamples[1][1] * 10 else (False, None)




class ScrollMessageBox(QtWidgets.QMessageBox):

   def __init__(self, l):

      QtWidgets.QMessageBox.__init__(self)
      scroll = QtWidgets.QScrollArea(self)
      scroll.setWidgetResizable(True)
      self.content = QtWidgets.QWidget()
      scroll.setWidget(self.content)
      lay = QtWidgets.QVBoxLayout(self.content)

      for item in l:
         lay.addWidget(QtWidgets.QLabel(item, self))

      self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
      self.setStyleSheet("QScrollArea{min-width:650 px; min-height: 400px}")




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_() # Start the application
