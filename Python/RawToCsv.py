from tkinter import filedialog
from scipy import signal
from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy.signal import butter, filtfilt


sample_rate = 2000  # Hz
sample_period = 1 / sample_rate

# Create a notch filter to remove 50Hz component
def create_notch_filter(frequency, sample_rate, Q=10):
    nyquist = sample_rate / 2.0
    notch_freq = frequency / nyquist
    b, a = signal.iirnotch(notch_freq, Q)
    return b, a

# Apply the notch filter to remove 50Hz component
def remove_50Hz(data, sample_rate):
    b, a = create_notch_filter(50, sample_rate)
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data

def remove_xHz(data, sample_rate, filterFrequency):
    b, a = create_notch_filter(filterFrequency, sample_rate)
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data

def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

FilePath = filedialog.askopenfilename()
with open(FilePath, 'rb') as file:
    data = file.read()

data = data[1000:] ##Remove the start
ADCValues = [[] for _ in range(12)]

OFFSET = 2
while(data[OFFSET]!=10): #Check for linefeed
    OFFSET+=1

OFFSET+=1
while(True):
    try:
        
        AdcNum = data[OFFSET + 0]
        if(AdcNum > 2):
            print("invalid ADC num")
            while(data[OFFSET]!=0x0A):
                OFFSET+=1
            OFFSET+=1
            continue

        channels=[]
        for i in range(4):
            channels.append(data[OFFSET + 1+3*i] * 2**16 + data[OFFSET + 2+3*i] * 2**8 + data[OFFSET + 3+3*i])
            if(channels[i] > 2**23):
                channels[i] = channels[i] - 2**24
            try:
                ADCValues[i+4*AdcNum].append(channels[i])
            except:
                pass
        OFFSET += 14
    except Exception as error:
        break

with open("output.csv", "w") as file:
    file.write("CH0;CH1;CH2;CH3;CH4;CH5;CH6;CH7;CH8;CH9;CH10;CH11\n")
    for i in range(len(ADCValues[0])-100):
        for j in range(12):
            file.write(str(ADCValues[j][i]))
            file.write(";")
        file.write("\n")

#AVG = 0
#for ADCVal in ADCValues[0]:
#    AVG += ADCVal
#AVG/=len(ADCValues[0])

#for i in range(len(ADCValues[0])):
#    ADCValues[0][i]-=AVG

cutoff = 80  # Desired cutoff frequency (Hz)
order = 6  # Filter order

FilteredADCValues = [[] for _ in range(12)]
for i in range(12):
    FilteredADCValues[i]=remove_xHz(ADCValues[i], sample_rate,50)
    FilteredADCValues[i] = butter_lowpass_filter(FilteredADCValues[i],cutoff,sample_rate,order)


#filtered_data = butter_lowpass_filter(filtered_data,cutoff,sample_rate,order)

#filtered_data = remove_xHz(filtered_data, sample_rate,100)
#filtered_data = remove_xHz(filtered_data, sample_rate,145.6)
#filtered_data = remove_xHz(filtered_data, sample_rate,357)
#filtered_data = remove_xHz(filtered_data, sample_rate,109)

#x = np.linspace(0.0, len(ADCValues[0])*sample_period, len(ADCValues[0]))
#yf = scipy.fftpack.fft(filtered_data)
#xf = np.linspace(10, 1.0/(2.0*sample_period), len(ADCValues[0])//2)
#fig, ax = plt.subplots()
#ax.plot(xf, 2.0/len(ADCValues[0]) * np.abs(yf[:len(ADCValues[0])//2]))
#plt.show()

with open("output_filtered.csv", "w") as file:
    file.write("CH0;CH1;CH2;CH3;CH4;CH5;CH6;CH7;CH8;CH9;CH10;CH11\n")
    for i in range(len(FilteredADCValues[0])-100):
        for j in range(12):
            file.write(str(FilteredADCValues[j][i]))
            file.write(";")
        file.write("\n")


 #print(data)
