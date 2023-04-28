def readTxt():
    deviceDetails = []
    header = ['SN',' Name', ' Brand', ' Price', ' Quantity', ' Processor', ' Graphic card']
    sn = 1
    deviceDetails.append(header)
    file = open('files.txt','r')
    for line in file:
        data = line.rstrip().split(',')
        deviceDetails.append([str(sn),*data])
        sn +=1
    return deviceDetails

