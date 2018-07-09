import time
import sys

def source():
    print ('''
        0) Offline Libraries
 
        1) Internet Source [Requires Internet Access]                
        
                                X) -- eXIT software
    ''')
    source_repo = str(raw_input("Dictio:~# "))

    if source_repo == "0":
        offline()
    elif source_repo == "1":
        online()
    elif source_repo == "X" or "x":
        print("Exiting in 3 seconds")
        time.sleep(2)
        sys.exit(0)
    else:
        print ("!!!Invalid Input!!!")
        source() 

def offline():
    print("Offiline stuff--Search and get definitions from offline libraries")

def online():
    print("Online Stuff -- Search and get results/definitions from the internet")