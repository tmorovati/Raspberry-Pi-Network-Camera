from picamera import PiCamera 
from time import sleep 
import os
import datetime 

#len(os.listdir('/home/pi/Pictures/camera-img/camera-image')) <25
print("df")
try:
    camera = PiCamera()
    camera.rotation = -90
    sleep(5)
    
    while(True):
        if(len(os.listdir('/home/pi/Pictures/camera-img/camera-image')) < 50):
            cd = datetime.datetime.now()
                
            date = str(cd.year)+'@'+str(cd.month)+'@'+str(cd.day)+'@@'+str(cd.hour)+'@'+str(cd.minute)+'@'+str(cd.second)
            print (date)
            camera.capture('/home/pi/Pictures/camera-img/camera-image/'+date+'.jpg')
            sleep(3)
               
 

                

except:
       print("error")
        

        



    

