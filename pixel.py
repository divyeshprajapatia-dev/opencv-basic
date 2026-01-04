import cv2

image = cv2.imread("test3.jpeg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

pixel_value = gray[200,200]

print("pixel intensity at (200,200)",pixel_value)