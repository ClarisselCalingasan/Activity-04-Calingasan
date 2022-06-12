import cv2

filePath = 'moon.jpg'
img = cv2.imread(filePath, 1)
cv2.imshow("Moon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()