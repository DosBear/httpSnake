import os
import sys
import time
from config import webURL, tmpPath
import requests
import sendmail

reload(sys)
sys.setdefaultencoding('utf-8')


headers = {'User-Agent': 'Mozilla/5.0'}
for item in webURL:
    response = requests.get(webURL[item], headers=headers)
    fileName = os.path.join(tmpPath, item + ".txt")
    data = ""
    if os.path.isfile(fileName):
        with open(fileName, 'r') as myfile: 
            data = myfile.read()
    if(data != "\n".join(response.text.split('\n')[60:])):
        with open(fileName, 'w') as myfile: 
            myfile.write("\n".join(response.text.split('\n')[60:]))   
        print "Different page for: " + item
        sendmail.send_mail(item, "Text chaned", "mnc3@yandex.ru")
    else:
        print "Same page for: " + item