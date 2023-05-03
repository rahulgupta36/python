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


# from ReadTxt import readTxt


# def display():
#     deviceDetails = readTxt()
#     for row in deviceDetails:
#         for each in row:
#             print(str(each).center(20) + '|', end='\t')            
#         print()
#         print("_" * 200)

# if __name__ == "main":
#     display()
from ReadTxt import readTxt

    
def display():
    deviceDetails = readTxt()
    print("_" * 164)
    print(" " * 9 + "SN" + " " * 9 + '|' + " " * 10 + "Name" + " " * 9 + '|' + " " * 9 + "Brand" + " " * 9 + '|' + " " * 9 + "Price" + " " * 9 + '|' + " " * 7 + "Quantity" + " " * 8 + '|' + " " * 7 + "Processor" + " " * 7 + '|' + " " * 7 + "Graphic card" + " " * 4 + '|')
    print("_" * 164)
    for row in deviceDetails:
        for each in row:
            print(str(each).center(20) + '|', end='\t')                        
        print()
        print("_" * 164)

if __name__ == "__main__":
    display()
