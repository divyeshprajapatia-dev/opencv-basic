import cv2

image = cv2.imread("test_image/test3.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200) # 100 and 200 is range that if pixel fall under it its not consider and if it bigger that it strong or it not than weak 


cv2.imshow("grayscale", gray)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()