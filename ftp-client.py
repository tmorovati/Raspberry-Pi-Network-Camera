from ftplib import FTP
import os
import fileinput

'''
ftp = FTP('192.168.97.31' , user= 'win7' , passwd = '2')
ftp.getwelcome()
'''
ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('192.168.97.31', 21)
ftp.login('win7','2')


#ftp.mkd('//imges-raspcamera-p')
ftp.cwd('/imges-raspcamera-p')


def ftp_upload(localfile , remotefile):
    fp = open(localfile , 'rb')
    print(localfile)
    ftp.storbinary('STOR %s' % os.path.basename(localfile) , fp , 1024)
    fp.close()
    print ("after upload" , localfile , " to " , remotefile )

localdir = '/home/pi/Pictures/camera-img/camera-image'

def upload_img(file):
    ftp_upload(localdir + "/" + file , file )


lastlist = []
for line in fileinput.input(localdir + "/list.txt"):
    lastlist.append(line.rstrip("\n"))

#print(lastlist)
currentlist = os.listdir(localdir)
#print (currentlist)
newfiles = list(set(currentlist) - set(lastlist))
#print(newfiles)
if len(currentlist) == 0 :
        print ("no file need to upload")
        
else :
    for needupload in newfiles:
        print("uploading" + localdir + '/' + needupload)
        upload_img(needupload)
        print(localdir+'/'+needupload)
        os.remove(localdir+'/'+needupload)
        
        with open (localdir + '/list.txt' , "a") as myfile:
            myfile.write(needupload + "\n")
        


ftp.quit()

