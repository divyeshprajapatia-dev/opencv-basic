import cv2

image = cv2.imread("test_image/test3.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# _,binery = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  if we want to use binery then we need to invers it like cv2.THRESH_BINERY_INV 
edges = cv2.Canny(gray, 100, 200)

#find contours

contours,_ = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

output = image.copy()
cv2.drawContours(output, contours, -1, (0,255,0), 2)

# geting object position 
for cnt in contours:
    area = cv2.contourArea(cnt)
    print(area)
    if area < 50:
        continue #ignore noise
    
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(output,(x,y), (x+w,y+h), (255,0,0),2)

print("Number of conturs found:",len(contours))

cv2.imshow("edges",edges)
cv2.imshow("contours", output)

cv2.waitKey(0)
cv2.destroyAllWindows()