import time
from datetime import datetime
from queue import Queue
import threading
import tkinter
import tkinter.ttk as ttk
import tkinter as tk
from random import random

from tkinter import filedialog, scrolledtext
from tkinter.messagebox import showinfo

import cv2
from numpy.random import randint
from win32api import GetSystemMetrics
from tkinter import *
from tkinter.filedialog import askopenfilename

from BL.analyzer import analyzer
from BL.generators.hardmard import hardmard
from BL.classifier import classify
import BL.Input_handler.image as imghandler
import BL.Input_handler.text as textHandler
import os
import PIL.Image
import io
from Crypto.Random import get_random_bytes
from BL.ciphering import ChaCha
from BL.generators.threshold import threshold
import BL.preper_key as pk
#key = [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]
# key = get_random_bytes(32)
# nonce = get_random_bytes(12)
hardmardkey =  os.listdir(r'C:\Users\yasse\PycharmProjects\dsc\keystream\hardmard')
thresholdkey = os.listdir(r'C:\Users\yasse\PycharmProjects\dsc\keystream\threshold')


master = Tk()


global orginalfilepath


if __name__ == '__main__':
    size = str(GetSystemMetrics(0)) + 'x' + str(GetSystemMetrics(1))
    master.geometry(size)
    master.title("AllSafe")

def openHardMardGenWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("HardMard")

    # sets the geometry of toplevel
    size = str(GetSystemMetrics(0)) + 'x' + str(GetSystemMetrics(1))
    newWindow.geometry(size)
    # retrieves object from queue #

    tkinter.Label(newWindow, text="Polynomial 1").grid(row=0, column=1,pady=5,padx=10)
    tkinter.Label(newWindow, text="Polynomial 2").grid(row=1, column=1,pady=5,padx=10)
    e3 = tkinter.Entry(newWindow, width=50)
    e4 = tkinter.Entry(newWindow, width=50)

    e3.grid(row=0, column=2)
    e4.grid(row=1, column=2)

    tkinter.Label(newWindow, text="Key buffer Of HARDMARD ").grid(row=3, column=2, pady=10)
    #T1 = Text(newWindow, height=20, width=100)
    T1 = scrolledtext.ScrolledText(newWindow,
                                      wrap = tk.WORD,
                                      width = 100,
                                      height = 20,
                                      font = ("Times New Roman",15))
    T1.grid(row=3, column=3)


    # keypath = ""
    # keyfilename = ""
    # key_file_extension = ""

    def openkeyFileThred():
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        orginalfilepath = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
       # keyfilename, key_file_extension, keypath
        keyfilename, key_file_extension = os.path.splitext(orginalfilepath)
        keypath = os.path.abspath(orginalfilepath)
        data = pk.key_loader(orginalfilepath)
        word = pk.split(data)
        chunk = pk.chunks(word,256)
        x=randint(0, len(chunk)-1)
        T1.insert(tk.INSERT, chunk[x])

    def openkeyFile():
        k1 = threading.Thread(target=openkeyFileThred)
        k1.start()


    btn_hardmard = Button(newWindow, text="Read Genrated Key", command=openkeyFile)
    btn_hardmard.grid(row=4, column=2, padx=10, pady=10)

    def hardmard_go():
        hardmard_ploy1 = e3.get()
        hardmard_ploy2 = e4.get()
        function1, max_period1 = analyzer(hardmard_ploy1).convert_pol_to_bin()
        function2, max_period2 = analyzer(hardmard_ploy2).convert_pol_to_bin()
        bit_to_xor = [0, 1, 2]
        max_clock = (2 ** int(max_period1) - 1) * (2 ** int(max_period2) - 1)
        hm = hardmard(function1, function2, bit_to_xor, max_clock)
        hm.start_key_streamming()

    def hardmard_thread():
        t1 = threading.Thread(target=hardmard_go)
        t1.start()
        # defines indeterminate progress bar (used while thread is alive) #
        pb1 = ttk.Progressbar(newWindow, orient='horizontal', mode='indeterminate')

        # defines determinate progress bar (used when thread is dead) #
        pb2 = ttk.Progressbar(newWindow, orient='horizontal', mode='determinate')
        pb2['value'] = 100

        # places and starts progress bar #
        pb1.grid(row=3, column=3, padx=10, pady=10)
        pb1.start()

        # checks whether thread is alive #
        while t1.is_alive():
            newWindow.update()
            pass

        # once thread is no longer active, remove pb1 and place the '100%' progress bar #
        pb1.destroy()
        pb2.pack()


        # hardmard command

    btn_hardmard = Button(newWindow, text="Hardmard Go", command=hardmard_thread)
    btn_hardmard.grid(row=2, column=2, padx=10, pady=10)


btnhardmard = Button(master,
              text="Go To Hardmard",
              command=openHardMardGenWindow)
btnhardmard.grid(row=5,column=0)




def openthresholdGenWindow():
    # Toplevel object which will
    # be treated as a new window
    thresholdWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    thresholdWindow.title("Threshold")

    # sets the geometry of toplevel
    size = str(GetSystemMetrics(0)) + 'x' + str(GetSystemMetrics(1))
    thresholdWindow.geometry(size)

    tkinter.Label(thresholdWindow, text="Polynomial 1").grid(row=0, column=0)
    tkinter.Label(thresholdWindow, text="Polynomial 2").grid(row=1, column=0)
    tkinter.Label(thresholdWindow, text="Polynomial 3").grid(row=2, column=0)
    e5 = tkinter.Entry(thresholdWindow, width=50)
    e6 = tkinter.Entry(thresholdWindow, width=50)
    e7 = tkinter.Entry(thresholdWindow, width=50)

    e5.grid(row=0, column=1)
    e6.grid(row=1, column=1)
    e7.grid(row=2, column=1)
    # text area
    tkinter.Label(thresholdWindow, text="Key buffer Of THRESHOLD").grid(row=4, column=1, pady=50)
    # Create text widget and specify size.



    #T2 = Text(thresholdWindow, height=20, width=
    T2 = scrolledtext.ScrolledText(thresholdWindow,
                                      wrap = tk.WORD,
                                      width = 100,
                                      height = 20,
                                      font = ("Times New Roman",15))
    T2.grid(row=4 , column=2)

    def openkeyFileThred():
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        orginalfilepath = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
       # keyfilename, key_file_extension, keypath
        keyfilename, key_file_extension = os.path.splitext(orginalfilepath)
        keypath = os.path.abspath(orginalfilepath)
        data = pk.key_loader(orginalfilepath)
        word = pk.split(data)
        chunk = pk.chunks(word,256)
        x=randint(0, len(chunk)-1)
        T2.insert(tk.INSERT, chunk[x])

    def openkeyFile():
        k2 = threading.Thread(target=openkeyFileThred)
        k2.start()

    btn_hardmard = Button(thresholdWindow, text="Read Genrated Key", command=openkeyFile)
    btn_hardmard.grid(row=5, column=1, padx=0, pady=0)

    def threshold_go():
        hardmard_ploy1 = e5.get()
        hardmard_ploy2 = e6.get()
        hardmard_ploy3 = e7.get()

        function1, max_period1 = analyzer(hardmard_ploy1).convert_pol_to_bin()
        function2, max_period2 = analyzer(hardmard_ploy2).convert_pol_to_bin()
        function3, max_period3 = analyzer(hardmard_ploy3).convert_pol_to_bin()
        bit_to_xor = [0, 2, 4]
        max_clock = ((2 ** int(max_period1)) - 1) * ((2 ** int(max_period2)) - 1) * ((2 ** int(max_period3)) - 1)

        th = threshold(function1, function2, function3, bit_to_xor, max_clock)
        th.start_key_streamming()

    def threshold_thread():
        t2 = threading.Thread(target=threshold_go)
        t2.start()
        # defines indeterminate progress bar (used while thread is alive) #
        pb3 = ttk.Progressbar(thresholdWindow, orient='horizontal', mode='indeterminate')

        # defines determinate progress bar (used when thread is dead) #
        pb4 = ttk.Progressbar(thresholdWindow, orient='horizontal', mode='determinate')
        pb4['value'] = 100

        # places and starts progress bar #
        pb3.grid(row=4, column=2, padx=10, pady=10)
        pb3.start()

        # checks whether thread is alive #
        while t2.is_alive():
            thresholdWindow.update()
            pass

        # once thread is no longer active, remove pb1 and place the '100%' progress bar #
        pb3.destroy()
        pb4.pack()

        # retrieves object from queue #


    btn_threshold = Button(thresholdWindow, text="threshold Go", command=threshold_thread)
    btn_threshold.grid(row=3, column=1, padx=10, pady=10)

btnthreshold = Button(master,text="Go To Threshold",command=openthresholdGenWindow)
btnthreshold.grid(row=6,column=0,padx=10, pady=10)

pa = ""
filename = ""
file_extension = ""
def openNewFile():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    orginalfilepath = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    global filename,file_extension,pa
    filename, file_extension = os.path.splitext(orginalfilepath)
    pa = os.path.abspath(orginalfilepath)


def encryption_go():
    file = file_extension.replace('.','')
    file_type = classify(file)
    x = randint(0, len(hardmardkey))
    randomfilyname = hardmardkey[x]
    data1 = pk.key_loader(r'C:\Users\yasse\PycharmProjects\dsc\keystream\hardmard'+"\\"+randomfilyname)
    word1 = pk.split(data1)
    chunk1 = pk.chunks(word1, 256)
    y = randint(0, len(chunk1) -1)
    key = chunk1[y]

    z = randint(0, len(hardmardkey))
    randomfilyname = hardmardkey[z]
    data2 = pk.key_loader(r'C:\Users\yasse\PycharmProjects\dsc\keystream\hardmard'"\\"+randomfilyname)
    word2 = pk.split(data2)
    chunk2 = pk.chunks(word2, 256)
    s = randint(0, len(chunk2) -1)
    nonce = chunk2[s]




    e1.insert('0',key)
    e2.insert('0',nonce)
    key = bytearray(key)
    key = key[1:33]
    nonce = bytearray(nonce)
    nonce = nonce[1:13]


    encryptor = ChaCha.ChaCha(key, nonce)
    if (file_type == "imageFiles"):

        image = cv2.imread(pa)

        image_bytes = []

        # image_bytes = imghandler.img_loader(path)
        height = image.shape[0]
        width = image.shape[1]
        z = 0

        for i in range(height):
            for j in range(width):
                image_bytes.append(image[i, j, 0])
                image_bytes.append(image[i, j, 1])
                image_bytes.append(image[i, j, 2])

        ciphertext = encryptor.ImgEncrypt(image_bytes)
        encyptedimage = image
        z = 0
        i = 0
        j = 0
        for x in range(len(ciphertext)):
            if (i >= height):
                break
            if (j >= width):
                j = 0
                i = i + 1
            if (z >= len(ciphertext)):
                break
            xi = ciphertext[z]
            encyptedimage[i, j, 0] = ciphertext[z]
            z = z + 1
            if (z >= len(ciphertext)):
                break
            encyptedimage[i, j, 1] = ciphertext[z]
            z = z + 1
            if (z >= len(ciphertext)):
                break
            encyptedimage[i, j, 2] = ciphertext[z]
            z = z + 1
            j = j + 1
        file_name_postfix = int(datetime.now().strftime("%Y%m%d%H%M%S"))
        cv2.imwrite(r'C:\Users\yasse\PycharmProjects\dsc\DAL\output\encrypted\img-%e.jpg' % file_name_postfix, encyptedimage)

        # algorithmkey = e1.get()
        # algorithmkey = algorithmkey.split(' ')
        # algorithmnonce = e2.get()
        # algorithmnonce = algorithmnonce.split(' ')
        #
        # for i in range(0, len(algorithmkey)):
        #     algorithmkey[i] = int(algorithmkey[i])
        #
        # for i in range(0, len(algorithmnonce)):
        #     algorithmnonce[i] = int(algorithmnonce[i])
        #
        # algorithmkey = bytearray(algorithmkey)
        # algorithmkey = algorithmkey[0:32]
        #
        # algorithmnonce = bytearray(algorithmnonce)
        # algorithmnonce = algorithmnonce[0:12]

        plaintext = encryptor.ImgDecrypt(ciphertext)
        decryptedimage = cv2.imread(r'C:\Users\yasse\PycharmProjects\dsc\DAL\output\encrypted\img-%e.jpg' % file_name_postfix)

        z = 0
        i = 0
        j = 0
        for x in range(len(plaintext)):
            if (i >= height):
                break
            if (j >= width):
                j = 0
                i = i + 1
            if (z >= len(plaintext)):
                break
            decryptedimage[i, j, 0] = plaintext[z]
            z = z + 1
            if (z >= len(plaintext)):
                break
            decryptedimage[i, j, 1] = plaintext[z]
            z = z + 1
            if (z >= len(plaintext)):
                break
            decryptedimage[i, j, 2] = plaintext[z]
            z = z + 1
            j = j + 1
        file_name_postfix = int(datetime.now().strftime("%Y%m%d%H%M%S"))
        cv2.imwrite(r'C:\Users\yasse\PycharmProjects\dsc\DAL\output\decrypted\img-%d.jpg' % file_name_postfix, decryptedimage)
        showinfo("AllSafe", "Encryption done")


    elif (file_type == "textFiles"):
        plaintext = textHandler.ReadText(pa)
        ciphertext = encryptor.encrypt(plaintext)

        # print(ciphertext)
        #ciphertext = bytes(ciphertext)
        file_name_postfix = int(datetime.now().strftime("%Y%m%d%H%M%S"))
        textHandler.WriteText(r'C:\Users\yasse\PycharmProjects\dsc\DAL\output\encrypted\text-%e.txt' % file_name_postfix, ciphertext)

        ciphertext = textHandler.ReadText(r'C:\Users\yasse\PycharmProjects\dsc\DAL\output\encrypted\text-%e.txt' % file_name_postfix)
        plaintext = encryptor.decrypt(ciphertext)
        file_name_postfix = int(datetime.now().strftime("%Y%m%d%H%M%S"))
        textHandler.WriteText(r'C:\Users\yasse\PycharmProjects\dsc\DAL\output\decrypted\text-%d.txt' % file_name_postfix, plaintext)

    else:
        print("File Type Is " + file_type)






btn = Button(master, text="Click to open a new file", command=openNewFile)
btn.grid(row=0, column=0, padx=10, pady=10)

tkinter.Label(master, text="Key").grid(row=1 ,column=0)
tkinter.Label(master, text="Nonce").grid(row=2,column=0)

tkinter.Label(master, text="                   ").grid(row=3,column=1)
tkinter.Label(master, text="                   ").grid(row=5,column=1)
tkinter.Label(master, text="                   ").grid(row=1,column=5)
tkinter.Label(master, text="                   ").grid(row=1,column=3)

e1 = tkinter.Entry(master, width=200)
e2 = tkinter.Entry(master, width=200)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)



def decryption_go():
    time.sleep(8)
    showinfo("AllSafe", "decryption done")


btn_chipering = Button(master, text="Encrypt Using ChaCha", command=encryption_go)
btn_chipering.grid(row=3, column=0,padx=10, pady=10)

btn_dechipering = Button(master, text="Decrypt Using ChaCha", command=decryption_go)
btn_dechipering.grid(row=4, column=0,padx=10, pady=10)


mainloop()
