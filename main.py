#Dictionary Program 
import sys
import time
import source

#Check for Python2 and 3
import sys
if sys.version_info > (3, 0):
    sys.stdout.write("Sorry, Python 2.7 or lower is required for sorware to run \n")
    print("Exiting in Two(2) Seconds")
    time.sleep(1)
    sys.exit(2)

def home():
    print(''''
    
    // /     //   ////   ~    tt      ii   
    //   /       //      ~  tttttt   
    //   /   //  //      ~   tt      ii    o o
    //  /    //  //      ~    t      ii   o   o
    ////     //   ////   ~     tttt  ii    o o

    ''')
home()
source.source()
