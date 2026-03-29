import cv2
import numpy as np 
import math
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import sys
from matplotlib import pyplot as plt


def nothing(x):
    pass

def image():

    print(a)
    print(N)
    print(p)

    # Phase 1: Bilateral filtering
    bilateral_filtimg = input_image
    for x in range(N):
        bilateral_filtimg = cv2.bilateralFilter(bilateral_filtimg, 9, 75, 75)

    median_filtimg = cv2.medianBlur(bilateral_filtimg, 5)

    rows, cols, c = median_filtimg.shape
    colorquantimg = median_filtimg.copy()

    # Color quantization
    for i in range(rows):
        for j in range(cols):
            xb = median_filtimg[i, j, 0]
            xg = median_filtimg[i, j, 1]
            xr = median_filtimg[i, j, 2]

            xb = int(math.floor(xb / a) * a)
            xg = int(math.floor(xg / a) * a)
            xr = int(math.floor(xr / a) * a)

            colorquantimg[i, j] = [xb, xg, xr]

    # Phase 2: Edge detection
    median_filtimg2 = cv2.medianBlur(input_image, 5)

    edges = cv2.Canny(median_filtimg2, p, 2 * p)
    dialateimg = cv2.dilate(edges, np.ones((3, 3), 'uint8'))
    edges_inv = cv2.bitwise_not(dialateimg)

    ret, thresh = cv2.threshold(edges_inv, 127, 255, 0)

    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
    )

    img_contours = cv2.drawContours(thresh, contours, -1, (0, 0, 0), 3)
    print(img_contours)

    
    global finalimg
    finalimg = colorquantimg.copy()

    for i in range(rows):
        for j in range(cols):
            if edges_inv[i, j] == 0:
                finalimg[i, j] = [0, 0, 0]

    cv2.imshow('Toonified Image', finalimg)
    cv2.waitKey(0) 

# Main Routine
def filecall():
   
    filename = askopenfilename()
    global input_image 
    input_image = cv2.imread(filename)

def proceed():
    global a
    global N
    global p
    a = w1.get()
    N = w2.get()
    p = w3.get()
    image()

def quit():
	cv2.destroyWindow('Toonified Image')
	cv2.imshow('Final Output, You can save this one',finalimg)
	cv2.waitKey(0)    
	root.destroy()

root = Tk()
root.geometry("500x500")

l1 = Label(root,text = 'Select Image')
l1.pack()

b1 = Button(root,text = 'Browse',command=filecall)
b1.pack()

b2 = Button(root,text = 'Proceed',command=proceed)
b2.pack()

b3 = Button(root,text = 'Quit',command=quit)
b3.pack()

w1 = Scale(root,label ='Color Quantization Degree(Optimum = 24)',length = 400, from_=10, to=50,orient=HORIZONTAL)
w1.pack()

w2 = Scale(root,label = 'Staircase Cartoon Feature Number(Optimum = 5)',length = 400, from_=1, to=10,orient=HORIZONTAL)
w2.pack()

w3 = Scale(root,label = 'Border Parameter(As per need(higher the better))', length = 400, from_=10, to=100,orient=HORIZONTAL) 
w3.pack()

root.mainloop()



    
    
