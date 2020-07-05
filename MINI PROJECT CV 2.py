from tkinter import *
from tkinter import ttk
import cv2
import numpy as np


root = Tk()
root.title("Computer Vision ASSIGNMENT")

thelabel = ttk.Label(root, text="IMAGE Manipulation Using OpenCV ")
thelabel.pack()
thelabel = ttk.Label(root, text="HUZAIFA 2K17/IT/32")
thelabel.pack()
thelabel = ttk.Label(root, text="SOHAIL AHMED LAGHAARI 2K17/IT/88 \n")
thelabel.pack()

def fn_btn1():
 img = cv2.imread('profile.png')
 img=cv2.resize(img, (800,620))
 cv2.imshow("Original" , img)
 img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 cv2.imshow("Grayscale cvtColor", img2)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
    
def fn_btn2():
 img = cv2.imread("profile.png")
 img=cv2.resize(img , (720,480))
 cv2.imshow("Original Image", img)
 img2 = cv2.imread("profile.png",0)
 img2=cv2.resize(img2 , (720,480))
 ret,bw = cv2.threshold(img2, 90, 200, cv2.THRESH_BINARY)
 cv2.imshow("Final Binary Image",bw)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
    
def fn_btn3():
 img = cv2.imread('profile.png')
 img= cv2.resize(img, (720,480))
 cv2.imshow("Original Image", img)
 img_hsv=cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
 hsv_resize = cv2.resize(img_hsv,(720,480))
 cv2.imshow("HSV IMAGE", hsv_resize)
 cv2.imshow("HUE", hsv_resize[:, :, 0])
 cv2.imshow("Saturation", hsv_resize[:, :, 1])
 cv2.imshow("Value", hsv_resize[:, :, 2])
 cv2.waitKey(0)
 cv2.destroyAllWindows()

def fn_btn4():

 image = cv2.imread('profile.jpg', cv2.IMREAD_UNCHANGED)
 print(image.shape)
 green_channel,blue_channel,red_channel = image[:,:,1],image[:,:,0],image[:,:,2]
 green_img,blue_img,red_img = np.zeros(image.shape),np.zeros(image.shape),np.zeros(image.shape)
 green_img[:,:,1],blue_img[:,:,0],red_img[:,:,2] = green_channel,blue_channel,red_channel
 cv2.imwrite('green CV.jpg',green_img) 
 cv2.imwrite('blue CV.jpg',blue_img) 
 cv2.imwrite('Red CV.jpg',red_img) 
 cv2.imshow("Original", image)
 green_img = cv2.imread('green cv.jpg')
 cv2.imshow('Green Image', green_img)
 blue_img = cv2.imread('blue cv.jpg')
 cv2.imshow('Blue Image', blue_img)
 red_img = cv2.imread('red cv.jpg')
 cv2.imshow('RED Image', red_img)
 cv2.waitKey(0)
 cv2.destroyAllWindows()    

btn1= ttk.Button(root, text="Gray Scale Conversion ",command=fn_btn1)
btn1.pack()
btn2= ttk.Button(root, text="Binary Conversion",command=fn_btn2)
btn2.pack()
btn3= ttk.Button(root, text="HSV Channels Extraction",command=fn_btn3)
btn3.pack()
btn4= ttk.Button(root, text="RGB Channels Extraction",command=fn_btn4)
btn4.pack()

root.mainloop()
