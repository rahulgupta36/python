import sys
from Display import display
from Sell import sellDevices
print('''                                     /$$      /$$           /$$                                                            
                                    | $$  /$ | $$          | $$                                                            
                                    | $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$                 
                                    | $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$                
                                    | $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$                
                                    | $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/                
                                    | $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$                
                                    |__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/                
                                                                                                                           
                                                                                                                           
                                                                                                                           
                         /$$$$$$$$                                                   /$$$$$$  /$$                          
                        |__  $$__/                                                  /$$__  $$| $$                          
                           | $$  /$$$$$$         /$$$$$$  /$$   /$$  /$$$$$$       | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$ 
                           | $$ /$$__  $$       /$$__  $$| $$  | $$ /$$__  $$      |  $$$$$$ | $$__  $$ /$$__  $$ /$$__  $$
                           | $$| $$  \ $$      | $$  \ $$| $$  | $$| $$  \__/       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
                           | $$| $$  | $$      | $$  | $$| $$  | $$| $$             /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
                           | $$|  $$$$$$/      |  $$$$$$/|  $$$$$$/| $$            |  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$/
                           |__/ \______/        \______/  \______/ |__/             \______/ |__/  |__/ \______/ | $$____/ 
                                                                                                                 | $$      
                                                                                                                 | $$      
                                                                                                                 |__/   
                                                                                                                 ''')
    



# while True:
#     print('''          __________________________________________________________________________________________________
#          |   ____________________________________________________________________________________________   |
#          |  |                                                                                            |  |
#          |  |   What do you want to do?                                                                  |  |
#          |  |   ◙ Enter  1. To Display Laptop Details                                                    |  |
#          |  |   ◙ Enter  2. To Add Stok Of Laptops                                                       |  |
#          |  |   ◙ Enter  3. To Sell Laptops                                                              |  |
#          |  |   ◙ Enter  4. To Exit Programe                                                             |  |
#          |  |____________________________________________________________________________________________|  |
#          |__________________________________________________________________________________________________|''')
    

#     options=int(input("Enter any number between 1 and 4\n"))
#     if options==0 or options>4:
#         print("Please enter number between 1 and 4")
#     else:
#         if options==1:
#             display()
#         elif options==2:
#             sellDevices()
#         elif options==3:
#             print("option 3")
#         elif options==4:
#             print("You've Exit the programe")
#             sys.exit()
#         else:
#             print("Invalid input")
#             break


while True:
        print('''          __________________________________________________________________________________________________
         |   ____________________________________________________________________________________________   |
         |  |                                                                                            |  |
         |  |   What do you want to do?                                                                  |  |
         |  |   ◙ Enter  1. To Display Laptop Details                                                    |  |
         |  |   ◙ Enter  2. To Sell Laptops                                                              |  |
         |  |   ◙ Enter  3. To Add Stok Of Laptops                                                       |  |
         |  |   ◙ Enter  4. To Exit Programe                                                             |  |
         |  |____________________________________________________________________________________________|  |
         |__________________________________________________________________________________________________|''')
        options=int(input("Enter any number between 1 and 4\n"))
        if options==1:
            display()
        elif options==2:
            sellDevices()
        elif options==3:
            print("option 3")
        elif options==4:
            print("You've Exit the program")
            break  # exit the loop
        else:
            print("Invalid input. Please enter a number between 1 and 4.")




# while True:
#     print('''          __________________________________________________________________________________________________
#          |   ____________________________________________________________________________________________   |
#          |  |                                                                                            |  |
#          |  |   What do you want to do?                                                                  |  |
#          |  |   ◙ Enter  1. To Display Laptop Details                                                    |  |
#          |  |   ◙ Enter  2. To Add Stok Of Laptops                                                       |  |
#          |  |   ◙ Enter  3. To Sell Laptops                                                              |  |
#          |  |   ◙ Enter  4. To Exit Programe                                                             |  |
#          |  |____________________________________________________________________________________________|  |
#          |__________________________________________________________________________________________________|''')
#     options=int(input("Enter any number between 1 and 4\n"))

#     if options==1:
#         display()
#     elif options==2:
#         sellDevices()
#     elif options==3:
#         print("option 3")
#     elif options==4:
#         print("You've Exit the program")
#         sys.exit()
#     else:
#         print("Invalid input")
#         break
       