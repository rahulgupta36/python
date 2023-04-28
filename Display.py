from ReadTxt import readTxt
def display():
    deviceDetails = readTxt()
    for row in deviceDetails:
        for each in row:
            print(str(each).center(22) + '|', end='\t')
            
        print()
        print("_"*200)
