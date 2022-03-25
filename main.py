import pyautogui
import numpy
import mss
import time
import tkinter


def attack():
    pyautogui.click(1354, 64, clicks=2)
    while True:
        monitor = {
            "left": 795,
            "top": 531,
            "width": 1,
            "height": 1
        }

        img = mss.mss().grab(monitor)
        at = [60, 75, 168, 255]
        img_array = numpy.array(img)
        print(img_array)
        check = img_array[0][0]
        check = set(check)
        at = set(at)
        if check == at:
            pyautogui.click(717, 533)
    
        monitor1 = {
            "left": 677,
            "top": 269,
            "width": 1,
            "height": 1
        }
        img1 = mss.mss().grab(monitor1)                
        at1 = [87, 117, 149, 255]
        img_array1 = numpy.array(img1)
        check1 = img_array1[0][0]
        check1 = set(check1)
        at1 = set(at1)
        if check1 == at1:
            pyautogui.click(677, 269)
                    
        monitor2 = {
            "left": 807,
            "top": 679,
            "width": 1,
            "height": 1
        }
        img2 = mss.mss().grab(monitor2)
        at2 = [37, 46, 112, 255]
        img_array2 = numpy.array(img2)
        check2 = img_array2[0][0]
        check2 = set(check2)
        at2 = set(at2)
        if check2 == at2:
            pyautogui.click(807, 679)

def clantime(cont):
    cont = cont.split()
    while True:
        tl = time.localtime()
        tc = []
        tc.append(str(tl[3])+":"+str(tl[4]))
        if tc == cont:
            pyautogui.click(1354, 64, clicks=2)
            pyautogui.click(815,277)
            while True:
                attack()
        else:
            tc.clear()
