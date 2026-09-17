import hashlib
import os
import time
from tkinter import messagebox

#Global Variable
malware_hashes = list(open("virusHash.unibit","r").read().split('\n'))
virusInfo = list(open("virusInfo.unibit","r").read().split('\n'))


#Get Hash Of File
def sha256_hash(filename):
    try:
        with open(filename,"rb") as f:
            bytes = f.read()
            sha256hash = hashlib.sha256(bytes).hexdigest()

            f.close()
        # print(sha256hash)
        return sha256hash
    except:
        return 0
    
#Malware Dectection By Hash
def malware_checker(pathOfFile):
    global malware_hashes
    global virusInfo
    
    hash_malware_check = sha256_hash(pathOfFile)
    counter = 0


    for i in malware_hashes:
        if i == hash_malware_check:
            return virusInfo[counter]
        counter += 1

    return 0


#Malware Dectection In Folder
virusName = []
virusPath = []

def virusScanner(path):
    # Get the list of all files in directory tree at given path
    dir_list = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]
    print("Scanning directories: " + ", ".join(set([os.path.dirname(file) for file in dir_list])))
    for i in dir_list:
        if malware_checker(i) != 0:
            print(i)
            virusName.append(malware_checker(i)+" :: File :: "+os.path.normpath(i))
            # virusPath.append(i)
    return virusName

# Virus Remover
def virusRemover(path):
    virusScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        return 0
 


def juckFileRemover():

    # Temp Files Remover

    # show all the files that are removed in messagebox
    temp_list = list()

    # Windows username

    username = os.environ.get('USERNAME').upper().split(" ")

    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]

    for (dirpath, dirnames, filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]
        

    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]


    if temp_list:
        
            for i in temp_list:
                print(i)

                try:
                    os.remove(i)

                except:
                    pass

                try:
                    os.rmdir(i)

                except:
                    pass
            messagebox.showinfo("Threat Guardian","All Temporary Files Removed Successfully"+'\n'+"Total Files Removed : {}".format(len(temp_list)))
        

    else:
        return 0


def ramBooster():

    taskList = ["notepad.exe","AnyDesk.exe","TeamViewer_Service.exe","msedge.exe","IDMan.exe"]

    # Task Kill

    for i in taskList:

            os.system("taskkill /f /im  {}".format(i))

    messagebox.showinfo("Ram Booster","Ram Boosted Successfully")


