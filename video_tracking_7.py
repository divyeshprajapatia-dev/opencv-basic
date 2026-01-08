import cv2

cap = cv2.VideoCapture("test_image/video.mp4")


if not cap.isOpened():
    print("Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    # _, binary = cv2.threshold(gray, 125, 255,cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    prev_center = None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print("area",area)
        if area<300:
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),2)
        
        # M = cv2.moments(cnt)

        # if M["m00"] != 0:
        #     cx = int(M["m10"] / M["m00"])
        #     cy = int(M["m01"] / M["m00"])
        #     cv2.circle(frame, (cx,cy), 5, (0,0,255),-1)

        # if prev_center is not None:
        #     cv2.line(frame,prev_center,(cx,cy),(255,0,0),2)
        # prev_center = (cx,cy)
    
    print(len(contours))
    cv2.imshow("camera", frame)
    # cv2.imshow("grayscale", gray)
    cv2.imshow("edges", edges)
    # cv2.imshow("binary", binary)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()