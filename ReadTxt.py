# def readTxt():
#     deviceDetails = []
#     header = ['SN',' Name', ' Brand', ' Price', ' Quantity', ' Processor', ' Graphic card']
#     sn = 1
#     deviceDetails.append(header)
#     file = open('files.txt','r')
#     for line in file:
#         data = line.rstrip('\n').split(',')
#         deviceDetails.append([str(sn),*data])
#         sn +=1
#     return deviceDetails
def readTxt():
    deviceDetails = []
    sn = 1
    file = open('files.txt','r')
    for line in file:
        data = line.rstrip('\n').split(',')
        deviceDetails.append([str(sn),*data])
        sn +=1
    return deviceDetails


# def readTxt():
#     laptopData = [['Name','Brand','Price','Quantity','Processor','Graphic Card']]

#     with open('files.txt', 'r') as f:
#         for i in f:
#             data = i.strip()
#             dataTwo = data.split(",")
#             laptopData.append(dataTwo)
#     return laptopData


    # file = open("files.txt", "r")
    # lines = file.readlines()
    # laptop = []
    # for line in lines:
    #     line = line.rstrip('\n')
    #     line = line.split(",")
    #     laptop.append(line)
    # file.close()
    # return laptop

# def displayLaptop():
#     pass
# def readTxt():
#     deviceDetails = []
#     header = ['SN', 'Name', 'Brand', 'Price', 'Quantity', 'Processor', 'Graphic card']
#     sn = 1
#     deviceDetails.append(header)
#     try:
#         with open('backupfile.txt', 'r') as file:
#             for line in file:
#                 data = line.rstrip('\n').split(',')
#                 deviceDetails.append([str(sn), *data])
#                 sn += 1
#     except FileNotFoundError:
#         print("The file 'backupfile.txt' could not be found.")
#     return deviceDetails

# def readTxt():
#     deviceDetails = []
#     header = ['SN', 'Name', 'Brand', 'Price', 'Quantity', 'Processor', 'Graphic card']
#     sn = 1
#     deviceDetails.append(header)
#     try:
#         with open('backupfile.txt', 'r') as file:
#             for line in file:
#                 data = line.rstrip('\n').split(',')
#                 if len(data) > 0:  # check for empty line
#                     deviceDetails.append([str(sn), *data])
#                     sn += 1
#     except FileNotFoundError:
#         print("The file 'backupfile.txt' could not be found.")
#     return deviceDetails


# def readTxt():
#     with open('backupfile.txt')as file:
#         data=file.readlines()

#     deviceDetails=[]
#     for line in data:
#         row=line.strip().split(',')
#         deviceDetails.append(row)
    
#     return
