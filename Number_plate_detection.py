# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:24:14 2022

@author: Darknman
"""
import cv2
#%%
# Define Parameters
frameWidth = 640 
frameHeight = 480
minArea = 500
color = (255,0,255)
# Using Haarcascade Russian plate number 
nPlateCascade = cv2.CascadeClassifier(r"C:\Users\Darknman\Desktop\AI\OpenCV\resources\haarcascade_russian_plate_number.xml")
#%%
# Read images
img = cv2.imread(r"C:\Users\Darknman\Desktop\AI\OpenCV\resources\car.jpg")

# Implement Haarcascade and create bounding box
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
for (x, y, w, h) in numberPlates:
    area = w*h
    if area >minArea:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.putText(img,"Number Plate",(x,y-5),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
        imgRoi = img[y:y+h,x:x+w]
        cv2.imshow("ROI", imgRoi)
cv2.imshow("Result", img)
# Save the output image
cv2.imwrite(r"C:\Users\Darknman\Desktop\AI\OpenCV\resources\Scanned\Scanned_car.jpg",imgRoi)
cv2.waitKey(0)
cv2.destroyAllWindows()

