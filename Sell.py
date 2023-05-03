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




# import datetime
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



import datetime
from typing import ItemsView
from Display import display
from ReadTxt import readTxt


def sellDevices():
    display()
    # Read the data from file
    try:
        deviceDetails = readTxt()
    except FileNotFoundError:
        print("File not found.")
        return
    while True:
        clientName=input("Please enter Client Name: ")
        if clientName=="":
            print("Please Fill details")       
        else:
            break
    while True:
        clientAddress=input("Please Enter Client Address: ")
        if clientAddress=="":
            print("Please Fill Details")
        else:
            break
    while True:
        try:
            clientPhone=int(input("Please Enter Client Phone Number: "))
            if clientPhone=="":
                print("Phone Number Is Mandatory to fill")
            else:
                break
        except ValueError:
            print("Please Enter Integer Number")
    
    while True:
        shipping_cost = 0
        shippingCharge=input("Do you want Home Delivery?, answer in (yes/no): ")
        if shippingCharge=="":
            print("Shipping Charge Is Mandatory To be Filled")
        elif shippingCharge.lower()=="yes":
            print("Shipping charge will be Added")
            print("Thank You For Filling All")
            shipping_cost = 150
            break
        elif shippingCharge.lower()=="no":
            print("No shipping charge will be added")
            print("Thank You For Filling All")
            shipping_cost = 0
            break
        else:
            print("please answer in yes or no")
    # Display the devices


    # Ask user to select a device and update its quantity
    while True:
        # mainMenu=input("Enter r to return or Enter Any Other Key For Further Transaction: ")
        # if mainMenu=="r":
        #     print("You've Returned")
        #     break 
        selectedDevice = input("Enter the serial number of the device you want to sell: ")
        for i in range(0, len(deviceDetails)):
            if deviceDetails[i][0] == selectedDevice:
                while True:
                    try:
                        newQuantity = int(input("Enter the quantity: "))
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
            option = input("Do you want to sell more stock? (yes/no): ")
            if option.lower() == "yes":
                break
            elif option.lower() == "no":
                print("Thank you.")
            else:   
                print("Please answer with yes or no.")
            
                        # totalPrice=newQuantity*deviceDetails[i][3]
            productName= deviceDetails[i][1]
            laptop_brand = deviceDetails[i][2]
            laptop_price = deviceDetails[i][3].replace('$','')
            laptop_quantity =  newQuantity 
            total_price = newQuantity * int(laptop_price)
            total = 0
            grand_total = 0
                        # initialize the list to store purchased laptops
            purchased_laptops = []
                    
            total += total_price
            grand_total = total + shipping_cost
            laptop_total_price = grand_total
                            
                            # Write customer's details to file
            now = datetime.datetime.now()
                            # date_String = now.strftime('%Y-%m-%d %H:%M:%S')
            file_name = f"Sold_to_{clientName}.txt"
            with open(file_name, "w") as sale_file:
                sale_file.write(f"|{' '*2}Customer Name: {clientName}\n")
                sale_file.write(f"|{' '*2}Address: {clientAddress}\n")
                sale_file.write(f"|{' '*2}Phone number: {clientPhone}\n")
                sale_file.write(f"|{' '*2}Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
                            # Write order summary to file
                sale_file.write("________________________________________________________________________________________________\n")
                sale_file.write("| Laptop          | Brand          | Price per unit (USD) | Quantity       | Total price (USD) |\n")
                sale_file.write("________________________________________________________________________________________________\n")
                                # Write details of purchased laptops to file
                for purchased_laptop in purchased_laptops:
                    productName = purchased_laptop[0]
                    laptop_brand = purchased_laptop[1]
                    laptop_price = purchased_laptop[2]
                    laptop_quantity = purchased_laptop[3]
                    laptop_total_price = purchased_laptop[4]
                sale_file.write(f"| {productName:<16}| {laptop_brand:<15}|{laptop_price:>20}$ |{laptop_quantity:>15} |{laptop_total_price:>17}$ |\n")
                sale_file.write("___________________________________________________________________________________________\n")
                sale_file.write(f"|                                                                  Total   |{total:>17}$ |\n")
                sale_file.write("________________________________________________________________________________________________\n")
                sale_file.write(f"|                                                        Shipping Charge   |{shipping_cost:>17}$ |\n")
                sale_file.write("________________________________________________________________________________________________\n")
                sale_file.write(f"|{' '*60}Grand Total   |{grand_total:>17}$ |\n")
                sale_file.write("________________________________________________________________________________________________\n")
                sale_file.write(f"|{' '*32}Thank you, Please visit again!{' '*32}|\n")
                sale_file.write("________________________________________________________________________________________________\n")
                break


        print('''
                    ________________________________________________
                    |    Selling process completed Successfully.   |
                    ________________________________________________\n\n
                    ''')
        print(f"The invoice is created and stored in Sold_To_{clientName}.txt.\n\n")
        with open('files.txt', 'w') as f:
            for row in deviceDetails:
                f.write(','.join(row[1:]) + '\n')
                                
        return
  

 






                
