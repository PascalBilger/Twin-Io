from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import Lib
import statistics

sample_rate = 2000  # Hz

FilePath = filedialog.askopenfilename()

fig, axs = 0,0 # init the variables for the plot
lines = [] # init the variables for the plot

#Define the names for the charts
ChartNames = ["LEAD_I", "LEAD_II", "LEAD_III", "LEAD_aVR", "LEAD_aVL", "LEAD_aVF", "LEAD_V1", "LEAD_V2", "LEAD_V3", "LEAD_V4", "LEAD_V5", "LEAD_V6"]

AdcDataLen          = 14    # Specify how many bytes each measurement of an ADC contains
NumAdc              = 3     # Specify the number of ADCs used
NumChannelPerAdc    = 4     # Specify the number of channels per ADCW
NumSecondsToGraph   = 5     # Specify the number of seconds to put into the graph
AutoScaleYAxis      = True  # Set to true to autoscale the axis of the displayed graphs
                            # Set to false to have the same scale on all graphs to zomm around manually

AdcResolution = 23
AdcRefVolt = 2.442
AdcVoltagePerBit = AdcRefVolt / 2**AdcResolution

#define the indeces of the different electrodes
#This is the same numbering as indicated on the PCB V00-00-00
IDX_LL = 0
IDX_RA = 1
IDX_LA = 2
IDX_V1 = 3
IDX_V2 = 4
IDX_V3 = 5
IDX_V4 = 6
IDX_V5 = 7
IDX_V6 = 8
NumElectrodes = 9

#define the indeces of the different leads
IDX_LD_I   = 0
IDX_LD_II  = 1
IDX_LD_III = 2
IDX_LD_aVR = 3
IDX_LD_aVL = 4
IDX_LD_aVF = 5
IDX_LD_V1  = 6
IDX_LD_V2  = 7
IDX_LD_V3  = 8
IDX_LD_V4  = 9
IDX_LD_V5  = 10
IDX_LD_V6  = 11

NumLeads   = 12

FirstLoop = True
while(True):
    #open the raw data file and read it in binary mode
    with open(FilePath, 'rb') as file:
        data = file.read()

    data = data[-(AdcDataLen * NumAdc * sample_rate * NumSecondsToGraph):] #Get the Samples from the last "NumSecondsToGraph" seconds
    ADCValues = [[] for _ in range(NumAdc * NumChannelPerAdc)]              #Create an empty 2D array for tha ADC samples

    #get the offset to the first data packet
    OFFSET = Lib.getOffset(data)

    #Extract all the ADC values from the data
    while(OFFSET < len(data) - AdcDataLen):
        ADCValues, OFFSET = Lib.getAdcVals(data, OFFSET, ADCValues)
        if(int(OFFSET / AdcDataLen) % 100000 == 0):  #Every 100000 Bytes
            print(f'{OFFSET} of {len(data)} Bytes processed. {OFFSET / len(data) * 100}% processed')
        OFFSET += AdcDataLen

    #get the minimal number of samples for any channel and trim all channels to that length
    minlen = min(len(val) for val in ADCValues[:12])
    for i in range(12):
        ADCValues[i]=ADCValues[i][0:minlen-1]

    #skip loop iteration if not enough values are available
    if(len(ADCValues[0]) < 1000):
        continue

    #Calculate the leads from the data
    LeadValues = [[] for _ in range(NumLeads)]  #Create an empty 2D array for tha LeadData

    for Sample in range(len(ADCValues[0])):
        #Calculate the virtual ground
        Common = (ADCValues[IDX_LL][Sample]+ADCValues[IDX_RA][Sample]+ADCValues[IDX_LA][Sample]) / 3
        for Lead in range(NumLeads):
            if  (Lead==IDX_LD_I):
                LeadValues[Lead].append(ADCValues[IDX_LA][Sample] - ADCValues[IDX_RA][Sample])
            elif(Lead==IDX_LD_II):
                LeadValues[Lead].append(ADCValues[IDX_LL][Sample] - ADCValues[IDX_RA][Sample])
            elif(Lead==IDX_LD_III):
                LeadValues[Lead].append(ADCValues[IDX_LL][Sample] - ADCValues[IDX_LA][Sample])
            elif(Lead==IDX_LD_aVR):
                LeadValues[Lead].append(3/2*(ADCValues[IDX_RA][Sample] - Common))
            elif(Lead==IDX_LD_aVL):
                LeadValues[Lead].append(3/2*(ADCValues[IDX_LA][Sample] - Common))
            elif(Lead==IDX_LD_aVF):
                LeadValues[Lead].append(3/2*(ADCValues[IDX_LL][Sample] - Common))
            elif(Lead==IDX_LD_V1):
                LeadValues[Lead].append((ADCValues[IDX_V1][Sample] - Common))
            elif(Lead==IDX_LD_V2):
                LeadValues[Lead].append((ADCValues[IDX_V2][Sample] - Common))
            elif(Lead==IDX_LD_V3):
                LeadValues[Lead].append((ADCValues[IDX_V3][Sample] - Common))
            elif(Lead==IDX_LD_V4):
                LeadValues[Lead].append((ADCValues[IDX_V4][Sample] - Common))
            elif(Lead==IDX_LD_V5):
                LeadValues[Lead].append((ADCValues[IDX_V5][Sample] - Common))
            elif(Lead==IDX_LD_V6):
                LeadValues[Lead].append((ADCValues[IDX_V6][Sample] - Common))

    #Remove the Dc offset and calculate the voltage from the digital value
    for NumLead in range(NumLeads):
        DcOffset = statistics.mean(LeadValues[NumLead])
        for Sample in range(len(LeadValues[i])):
            LeadValues[NumLead][Sample] -= DcOffset
            LeadValues[NumLead][Sample] *= AdcVoltagePerBit

    #apply the notch filter and the lowpassfilter
    cutoff = 80     # Desired cutoff frequency (Hz)
    order = 6       # Filter order
    FilteredLeadValues = [[] for _ in range(12)]
    for i in range(12):
        FilteredLeadValues[i] = Lib.remove_xHz(LeadValues[i], sample_rate,50)
        FilteredLeadValues[i] = Lib.butter_lowpass_filter(FilteredLeadValues[i],cutoff,sample_rate,order)

    #do the plots TODO: scale simultaneously
    if FirstLoop:
        x = np.linspace(0, NumSecondsToGraph, len(FilteredLeadValues[0]))  # Assume the length of x is the same for all channels
        plt.ion()  # Turn on interactive mode
        if(AutoScaleYAxis):
            fig, axs = plt.subplots(4, 3, figsize = (15,15),sharex=False, sharey=False, layout="constrained")
        else:
            fig, axs = plt.subplots(4, 3, figsize = (15,15),sharex=True,  sharey=True,  layout="constrained")

        plt.autoscale()
        plt.tight_layout()
        for i in range(12):
            ax = axs[i // 3, i % 3]
            line, = ax.plot(x, FilteredLeadValues[i])  # Store line object
            lines.append(line)  # Append to lines list
            ax.set_title(f"Channel {ChartNames[i]}")
            ax.set_xlabel("Time")
            ax.set_ylabel("Filtered Value")
    for i in range(12):
        ax = axs[i // 3, i % 3]
        ax.set_ylim(min(FilteredLeadValues[i]), max(FilteredLeadValues[i]))
        lines[i].set_xdata(np.linspace(0, len(FilteredLeadValues[i]) / sample_rate, len(FilteredLeadValues[i])))  # Update x-data
        lines[i].set_ydata(FilteredLeadValues[i])  # Update y-data
    if FirstLoop:
        FirstLoop = False
    plt.draw()
    plt.pause(0.1)
    input("")  #Add this to stop the graph from auto updating to analyze the graphs statically. Press enter in the console to get the current image