# from ReadTxt import readTxt
# def sellDevices():

#         # Read the data from file
#     deviceDetails = readTxt()
#     selectedDevice = input("Enter the serial number of the device you want to sell: ")
#     for i in range(1, len(deviceDetails)):
#         if deviceDetails[i][0] == selectedDevice:
#             newQuantity = int(input("Enter the new quantity: "))
#             initialQuantity=int(deviceDetails[i][4])
#             if initialQuantity<newQuantity:
#                 print("Sorry the entered Quantity is more than available")
#             else:
#                 deviceDetails[i][4] = str(initialQuantity-newQuantity)
#             break
#     option="yes"
#     while option.lower()=="yes":
#         option=input("Do you want to sell more stock?(yes/no)")
#         if option.lower()=="yes":
            
#             # Ask user to select a device and update its quantity
#             selectedDevice = input("Enter the serial number of the device you want to sell: ")
#             for i in range(1, len(deviceDetails)):
#                 if deviceDetails[i][0] == selectedDevice:
#                     newQuantity = int(input("Enter the new quantity: "))
#                     initialQuantity=int(deviceDetails[i][4])
#                     if initialQuantity<newQuantity:
#                         print("Sorry the entered Quantity is more than available")
#                     else:
#                         deviceDetails[i][4] = str(initialQuantity-newQuantity)
#                     break
#                 # Save the updated data to the file
#             with open('files.txt', 'w') as f:
#                 for row in deviceDetails:
#                     f.write(','.join(row[1:]) + '\n')
#         elif option.lower()=="no":
#             print("Thank you")
#         else:
#             print("Please answer in yes or no!!")




# from ReadTxt import readTxt
# def sellDevices():

#         # Read the data from file
#     deviceDetails = readTxt()
#     selectedDevice = int(input("Enter the serial number of the device you want to sell: "))
#     if selectedDevice>0 and selectedDevice<len(deviceDetails):
#         for i in range(1,len(deviceDetails)):
#             if deviceDetails[i][0] == str(selectedDevice):
#                 newQuantity = int(input("Enter the new quantity: "))
#                 initialQuantity=int(deviceDetails[i][4])
#                 if initialQuantity<newQuantity:
#                     print("Sorry the entered Quantity is more than available")
#                 else:
#                     deviceDetails[i][4] = str(initialQuantity-newQuantity)
                
#     else:
#         print("Please Enter Valid Serial Number")
#     option="yes"
#     while option.lower()!="no":
#         option=input("Do you want to sell more stock?(yes/no)")
#         if option.lower()=="yes":
            
#             # Ask user to select a device and update its quantity
#             selectedDevice = input("Enter the serial number of the device you want to sell: ")
#             for i in range(1, len(deviceDetails)):
#                 if deviceDetails[i][0] == selectedDevice:
#                     try:
#                         newQuantity = int(input("Enter the new quantity: "))
#                         initialQuantity=int(deviceDetails[i][4])
#                         if initialQuantity<newQuantity:
#                             print("Sorry the entered Quantity is more than available")
#                         else:
#                             deviceDetails[i][4] = str(initialQuantity-newQuantity)
#                         break
#                     except ValueError:
#                         print("Please Enter Quantity in Integer")
            
#                 # Save the updated data to the file
#             with open('files.txt', 'w') as f:
#                 for row in deviceDetails:
#                     f.write(','.join(row[1:]) + '\n')
#         elif option.lower()=="no":
#             print("Thank you")
#         else:
#             print("Please answer in yes or no!!")





# from ReadTxt import readTxt
# def sellDevices():

#         # Read the data from file
#     deviceDetails = readTxt()
#         selectedDevice = input("Enter the serial number of the device you want to sell: ")
#         for i in range(1, len(deviceDetails)):
#             if deviceDetails[i][0] == selectedDevice:
#                 newQuantity = int(input("Enter the new quantity: "))
#                 initialQuantity=int(deviceDetails[i][4])
#                 if initialQuantity<newQuantity:
#                     print("Sorry the entered Quantity is more than available")
#                 else:
#                     deviceDetails[i][4] = str(initialQuantity-newQuantity)
#                 break
#             else:
#                 print("Please enter valid serial number")
#                 break
#     option="yes"
#     while option.lower()=="yes":
#         option=input("Do you want to sell more stock?(yes/no)")
#         if option.lower()=="yes":
            
#             # Ask user to select a device and update its quantity
#             selectedDevice = input("Enter the serial number of the device you want to sell: ")
#             for i in range(1, len(deviceDetails)):
#                 if deviceDetails[i][0] == selectedDevice:
#                     newQuantity = int(input("Enter the new quantity: "))
#                     initialQuantity=int(deviceDetails[i][4])
#                     if initialQuantity<newQuantity:
#                         print("Sorry the entered Quantity is more than available")
#                     else:
#                         deviceDetails[i][4] = str(initialQuantity-newQuantity)
#                     break
#                 # Save the updated data to the file
#             with open('files.txt', 'w') as f:
#                 for row in deviceDetails:
#                     f.write(','.join(row[1:]) + '\n')
#         elif option.lower()=="no":
#             print("Thank you")
#         else:
#             print("Please answer in yes or no!!")
#             break
#     else:
#         print("Please enter valid serial number")


# from ReadTxt import readTxt

# def updateDeviceQuantity(deviceDetails, selectedDevice, newQuantity):
#     for i in range(1, len(deviceDetails)):
#         if deviceDetails[i][0] == selectedDevice:
#             initialQuantity = int(deviceDetails[i][4])
#             if initialQuantity < newQuantity:
#                 print("Sorry, the entered quantity is more than available.")
#             else:
#                 deviceDetails[i][4] = str(initialQuantity - newQuantity)
#             return True
#     print("Please enter a valid serial number.")
#     return False

# def sellDevices():
#     # Read the data from file
#     deviceDetails = readTxt()
#     option = "yes"
#     while option.lower() == "yes":
#         selectedDevice = input("Enter the serial number of the device you want to sell: ")
#         newQuantity = int(input("Enter the new quantity: "))
#         if updateDeviceQuantity(deviceDetails, selectedDevice, newQuantity):
#             # Save the updated data to the file
#             with open('files.txt', 'w') as f:
#                 for row in deviceDetails:
#                     f.write(','.join(row[1:]) + '\n')
#             option = input("Do you want to sell more stock? (yes/no) ")
#         else:
#             option = input("Do you want to try again? (yes/no) ")
#     print("Thank you!")



# from Display import display
# from ReadTxt import readTxt
# import sys

# def sellDevices():
#     # Read the data from file
#     deviceDetails = readTxt()
#     display()
#     # Ask user to select a device and update its quantity
#     while True:
#         selectedDevice = input("Enter the serial number of the device you want to sell: ")
#         condition = False
#         for i in range(1, len(deviceDetails)):
#             if deviceDetails[i][0] == selectedDevice:
#                 condition = True
#                 newQuantity = int(input("Enter the new quantity: "))
#                 initialQuantity = int(deviceDetails[i][4])
#                 if initialQuantity < newQuantity:
#                     print("Sorry, the entered quantity is more than available.")
#                 else:
#                     deviceDetails[i][4] = str(initialQuantity - newQuantity)
#                 break

#         if not condition:
#             print("Please enter a valid serial number.")
#             continue

#         # Ask user if they want to sell more devices
#         while True:
#             option = input("Do you want to sell more stock? (yes/no)")
#             if option.lower() == "yes":
#                 break
#             elif option.lower() == "no":
#                 print("Thank you.")
#                 # Save the updated data to the file
#                 with open('files.txt', 'w') as f:
#                     for row in deviceDetails:
#                         f.write(','.join(row[1:]) + '\n')
#                 return
#             else:
#                 print("Please answer with yes or no.")




from typing import ItemsView
from Display import display
from ReadTxt import readTxt

def sellDevices():
            
    # Read the data from file
    try:
        deviceDetails = readTxt()
    except FileNotFoundError:
        print("File not found.")
        return
    while True:
        clientName=input("Please enter Client Name")
        if clientName=="":
            print("Please Fill details")       
        else:
            break
    while True:
        clientAddress=input("Please Enter Client Address")
        if clientAddress=="":
            print("Please Fill Details")
        else:
            break
    while True:
        clientPhone=input("Please Enter Client Phone Number")
        if clientPhone=="":
            print("Phone Number Is Mandatory to fill")
        else:
            break
    while True:
        shippingCharge=input("Do you want Home Delivery?")
        if shippingCharge=="":
            print("Shipping Charge Is Mandatory To be Filled")
        elif shippingCharge.lower()=="yes":
            print("Shipping charge will be Added")
            print("Thank You For Filling All")
            break
        elif shippingCharge.lower()=="no":
            print("No shipping charge will be added")
            print("Thank You For Filling All")
            break
        else:
            print("please answer in yes or no")
    # Display the devices
    display()

    # Ask user to select a device and update its quantity
    while True:
        mainMenu=input("Enter r to return")
        if mainMenu=="r":
            print("You've Returned")
            break 
        selectedDevice = input("Enter the serial number of the device you want to sell:\n")
        for i in range(0, len(deviceDetails)):
            if deviceDetails[i][0] == selectedDevice:
                while True:
                    try:
                        newQuantity = int(input("Enter the quantity:\n"))
                        initialQuantity = int(deviceDetails[i][4])
                        if initialQuantity < newQuantity:
                            print("Sorry, the entered quantity is more than available.")
                        else:
                            deviceDetails[i][4] = str(initialQuantity - newQuantity)
                            break
                    except ValueError:
                        print("Please enter a valid integer for the quantity.")
                break

        else:
            print("Please enter a valid serial number.")
            continue

        # Ask user if they want to sell more devices
        while True:
            option = input("Do you want to sell more stock? (yes/no)\n")
            if option.lower() == "yes":
                break
            elif option.lower() == "no":
                print("Thank you.")
                # Save the updated data to the file
                with open('files.txt', 'w') as f:
                    for row in deviceDetails:
                        f.write(','.join(row[1:]) + '\n')
                return
            else:
                print("Please answer with yes or no.")


                