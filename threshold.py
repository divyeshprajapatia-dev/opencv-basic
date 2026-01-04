import cv2 

image = cv2.imread("test3.jpeg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY)

print("gray shape:",gray.shape)
print("binary shape:",binary.shape)

cv2.imshow("grayscale",gray)
cv2.imshow("binary",binary)

cv2.waitKey(0)
cv2.destroyAllWindows