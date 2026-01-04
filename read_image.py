import cv2

image = cv2.imread("test_image/test2.jpg")

if image is None:
    print("image not found")
    exit()


print(f'image shape:{image.shape}')

cv2.imshow("image:",image)


cv2.waitKey(0)
cv2.destroyAllWindows()
