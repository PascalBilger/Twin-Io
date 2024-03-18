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
FirstLoop = True

fig, axs = 0,0 # init the variables for the plot
lines = [] # init the variables for the plot

while(True):
    with open(FilePath, 'rb') as file:
        data = file.read()

    data = data[-840000:] ##Remove the start
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

    cutoff = 80  # Desired cutoff frequency (Hz)
    order = 6  # Filter order

    

    FilteredADCValues = [[] for _ in range(12)]
    for i in range(12):
        FilteredADCValues[i]=remove_xHz(ADCValues[i], sample_rate,50)
        FilteredADCValues[i] = butter_lowpass_filter(FilteredADCValues[i],cutoff,sample_rate,order)

    minlen = 999999999999
    for i in range(12):
        if len(FilteredADCValues[i]<minlen):
            minlen = len(FilteredADCValues[i])

    for i in range(12):
        FilteredADCValues[i]=FilteredADCValues[i][0:minlen-1]

# Doesnt help with framerate which was the only reason
#    for i in range(12):
#        FilteredADCValues[i]=FilteredADCValues[i][19::20] #start at the 20th element (index 19) and take every 20th element from there


    if FirstLoop:
        x = np.linspace(0, 10, len(FilteredADCValues[0]))  # Assume the length of x is the same for all channels
        plt.ion()  # Turn on interactive mode
        fig, axs = plt.subplots(4, 3, figsize=(15, 15))
        plt.autoscale()
        plt.tight_layout()
        for i in range(12):
            ax = axs[i // 3, i % 3]
            line, = ax.plot(x, FilteredADCValues[i])  # Store line object
            lines.append(line)  # Append to lines list
            ax.set_title(f"Channel {i+1}")
            ax.set_xlabel("Time")
            ax.set_ylabel("Filtered Value")

    for i in range(12):
        ax = axs[i // 3, i % 3]
        ax.set_ylim(min(FilteredADCValues[i]), max(FilteredADCValues[i]))
        lines[i].set_xdata(np.linspace(0, 10, len(FilteredADCValues[i])))  # Update x-data
        lines[i].set_ydata(FilteredADCValues[i])  # Update y-data
    if FirstLoop:
        FirstLoop = False
    plt.draw()
    plt.pause(0.1)
    #plt.show()