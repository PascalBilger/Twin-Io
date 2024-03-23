from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import Lib

sample_rate = 2000  # Hz
sample_period = 1 / sample_rate

FilePath = filedialog.askopenfilename()
FirstLoop = True

fig, axs = 0,0 # init the variables for the plot
lines = [] # init the variables for the plot

AdcDataLen = 14         # Specify how many bytes each measurement of an ADC contains
NumAdc = 3              # Specify the number of ADCs used
NumChannelPerAdc = 4    # Specify the number of channels per ADC

while(True):
    #open the raw data file and read it in binary mode
    with open(FilePath, 'rb') as file:
        data = file.read()

    data = data[- AdcDataLen * NumAdc * sample_rate * 10:]      #Get the Samples from the last 10 seconds
    ADCValues = [[] for _ in range(NumAdc * NumChannelPerAdc)]  #Create an empty 2D array for tha ADC samples

    #get the offset to the first data packet
    OFFSET = Lib.getOffset(data)

    #Extract all the ADC values from the data
    while(OFFSET < len(data) - AdcDataLen):
        ADCValues = Lib.getAdcVals(data, OFFSET, ADCValues)
        OFFSET += AdcDataLen

    #skip loop iteration if not enough values are available
    if(len(ADCValues[0]) < 1000):
        continue

    #apply the notch filter and the lowpassfilter
    cutoff = 80     # Desired cutoff frequency (Hz)
    order = 6       # Filter order
    FilteredADCValues = [[] for _ in range(12)]
    for i in range(12):
        FilteredADCValues[i] = Lib.remove_xHz(ADCValues[i], sample_rate,50)
        FilteredADCValues[i] = Lib.butter_lowpass_filter(FilteredADCValues[i],cutoff,sample_rate,order)

    #get the minimal number of samples for any channel and trim all channels to that length
    minlen = min(len(val) for val in FilteredADCValues[:12])
    for i in range(12):
        FilteredADCValues[i]=FilteredADCValues[i][0:minlen-1]

    #do the plots
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