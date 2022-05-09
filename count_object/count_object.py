# Very simple way of counting objects in an image
# https://www.geeksforgeeks.org/count-number-of-object-using-python-opencv/
import cv2
import matplotlib.pyplot as plt
 
image = cv2.imread('img_1_all.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(12,7))
plt.imshow(gray, cmap='gray')

blur = cv2.GaussianBlur(gray, (11, 11), 0)
plt.figure(figsize=(12,7))
plt.imshow(blur, cmap='gray')

canny = cv2.Canny(blur, 30, 150, 3)
plt.figure(figsize=(12,7))
plt.imshow(canny, cmap='gray')

dilated = cv2.dilate(canny, (1, 1), iterations=0)
plt.figure(figsize=(12,7))
plt.imshow(dilated, cmap='gray')
 
(cnt, hierarchy) = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12,7))
plt.imshow(rgb)

cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
 
print("coins in the image : ", len(cnt))

plt.show()
