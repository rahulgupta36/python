from ReadTxt import readTxt
def sellDevices():

        # Read the data from file
    deviceDetails = readTxt()
    selectedDevice = input("Enter the serial number of the device you want to sell: ")
    for i in range(1, len(deviceDetails)):
        if deviceDetails[i][0] == selectedDevice:
            newQuantity = int(input("Enter the new quantity: "))
            initialQuantity=int(deviceDetails[i][4])
            deviceDetails[i][4] = str(initialQuantity-newQuantity)
            break
    option="yes"
    while option.lower()=="yes":
        option=input("Do you want to sell more stock?(yes/no)")
        if option.lower()=="yes":
            
            # Ask user to select a device and update its quantity
            selectedDevice = input("Enter the serial number of the device you want to sell: ")
            for i in range(1, len(deviceDetails)):
                if deviceDetails[i][0] == selectedDevice:
                    newQuantity = int(input("Enter the new quantity: "))
                    initialQuantity=int(deviceDetails[i][4])
                    deviceDetails[i][4] = str(initialQuantity-newQuantity)
                    break
                # Save the updated data to the file
            with open('files.txt', 'w') as f:
                for row in deviceDetails:
                    f.write(','.join(row[1:]) + '\n')
        elif option.lower()=="no":
            print("Thank you")
        else:
            print("Please answer in yes or no!!")
    



# from ReadTxt import readTxt

# def sellDevices():
#     # Read the data from file
#     deviceDetails = readTxt()

#     # Ask user to select a device and update its quantity
#     selectedDevice = input("Enter the serial number of the device you want to sell: ")

#     # Search for the selected device in the list
#     for i, device in enumerate(deviceDetails):
#         if device[0] == selectedDevice:
#             newQuantity = int(input("Enter the new quantity: "))
#             initialQuantity = int(device[4])
#             deviceDetails[i][4] = str(initialQuantity - newQuantity)
#             break

#     # Save the updated data to the file
#     with open('updatedfiles.txt', 'w') as f:
#         for row in deviceDetails:
#             f.write(','.join(row[1:]) + '\n')
# sellDevices()