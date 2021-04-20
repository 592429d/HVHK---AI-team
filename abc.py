import cv2
  
image = cv2.imread("1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Gray image', gray)
  
cv2.waitKey(0)
