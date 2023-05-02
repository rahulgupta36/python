# from ReadTxt import readTxt
# def display():
#     deviceDetails = readTxt()
#     for row in deviceDetails:
#         for each in row:
#             print(str(each).center(20) + '|', end='\t')            
#         print()
#         print("_"*200)
#         Laptop_list = []
#         column = ['SN', 'Name', 'Brand', 'Price','Qusntity', 'Processor','Graphic card' ]
#         Laptop_list.append(column)

#         file = open('files.txt', "r")
#         sn = 1
#         for line in file.readlines():
#             Laptop_list.append([str(sn), *line.rstrip().split(',')])
#             sn +=1
#             print()
#         file.close()

#         return Laptop_list


from ReadTxt import readTxt


def display():
    deviceDetails = readTxt()
    for row in deviceDetails:
        for each in row:
            print(str(each).center(20) + '|', end='\t')            
        print()
        print("_" * 200)