
from Display import display
from ReadTxt import readTxt


def addStock():
        # Read the data from file
    try:
        deviceDetails = readTxt()
    except FileNotFoundError:
        print("File not found.")
        return
    

    while True:
        VendorName=input("Please enter Vendor Name")
        if VendorName=="":
            print("Name Is Mandatory To Fill")       
        else:
            break
    while True:
        vendorAddress=input("Please Enter Vendor Address")
        if vendorAddress=="":
            print("Address Is Mandatory To Fill")
        else:
            break
    while True:
        vendorPhone=input("Please Enter Vendor's Phone Number")
        if vendorPhone=="":
            print("Phone Number Is Mandatory To Fill")
        else:
            print("Thank You For Filling all Details")
            break

    
    # Display the devices
    display()
    
    # Ask user to select a device and update its quantity
    while True:
        selectedDevice = input("Enter the serial number of the device you want to sell:\n")
        for i in range(1, len(deviceDetails)):
            if deviceDetails[i][0] == selectedDevice:
                while True:
                    try:
                        newQuantity = int(input("Enter the quantity:\n"))
                        initialQuantity = int(deviceDetails[i][4])
                        if initialQuantity <=0:
                            print("Please Enter Valid Value To Add.")
                        else:
                            deviceDetails[i][4] = str(initialQuantity + newQuantity)
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
                continue
                