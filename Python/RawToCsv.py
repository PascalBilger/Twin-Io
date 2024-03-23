from tkinter import filedialog
from scipy import signal
from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy.signal import butter, filtfilt
import Lib


sample_rate = 2000  # Hz
sample_period = 1 / sample_rate

FilePath = filedialog.askopenfilename()
with open(FilePath, 'rb') as file:
    data = file.read()

data = data[1000:] ##Remove the start
ADCValues = [[] for _ in range(12)]

OFFSET = Lib.getOffset(data)


while(len(data) < OFFSET - 14):
    ADCValues = Lib.getAdcVals(data, OFFSET, ADCValues) #Extract the 4 ADC Readings at position OFFSET
    OFFSET += 14                                        #Increase the offset by 14 because the number of Bytes sent by each ADC is 14 bytes


with open("output.csv", "w") as file:
    file.write("CH0;CH1;CH2;CH3;CH4;CH5;CH6;CH7;CH8;CH9;CH10;CH11\n")
    for i in range(len(ADCValues[0])-100):
        for j in range(12):
            file.write(str(ADCValues[j][i]))
            file.write(";")
        file.write("\n")

cutoff = 80  # Desired cutoff frequency (Hz)
order = 6  # Filter order

FilteredADCValues = [[] for _ in range(12)]
for i in range(12):
    FilteredADCValues[i] = Lib.remove_xHz(ADCValues[i], sample_rate,50)
    FilteredADCValues[i] = Lib.butter_lowpass_filter(FilteredADCValues[i],cutoff,sample_rate,order)


with open("output_filtered.csv", "w") as file:
    file.write("CH0;CH1;CH2;CH3;CH4;CH5;CH6;CH7;CH8;CH9;CH10;CH11\n")
    for i in range(len(FilteredADCValues[0])-100):
        for j in range(12):
            file.write(str(FilteredADCValues[j][i]))
            file.write(";")
        file.write("\n")