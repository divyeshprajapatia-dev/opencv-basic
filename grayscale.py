import cv2

image = cv2.imread("test3.jpeg")

if image is None:
    print("image not found")
    exit()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

print("image shape:",image.shape)
print("grayscale shape:",gray.shape)

cv2.imshow("original",image)
cv2.imshow("grayscale",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()