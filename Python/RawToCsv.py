from tkinter import filedialog

FilePath = filedialog.askopenfilename()
with open(FilePath, 'rb') as file:
    data = file.read()



with open("output.csv", "w") as file:
    OFFSET = 0
    while(True):
        try:
            channelNum = data[OFFSET + 0]
            channel0 = data[OFFSET + 1] * 2**16 + data[OFFSET + 2] * 2**8 + data[OFFSET + 3]
            if(channel0 > 2**23):
                channel0 = channel0 - 2**24
            file.write(str(channelNum))
            file.write(';')
            file.write(str(channel0))
            file.write('\n')
            OFFSET += 14
        except:
            break

print (data)