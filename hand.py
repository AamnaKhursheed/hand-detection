import numpy as np
import cv2
hand = cv2.imread("handy.png",0)
ret, threshold = cv2.threshold(hand,10,255,cv2.THRESH_BINARY)
contours, hiearchy= cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hull= [cv2.convexHull(c) for c in contours]
final = cv2.drawContours(hand,hull,-1,(255,255,255))
cv2.imshow('original',hand)
cv2.imshow('thresh',threshold)
cv2.imshow('Convex hull',hand)
cv2.waitKey(0)