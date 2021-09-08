import cv2
import numpy as np
img = cv2.imread('blur.jpeg', 0)

font = cv2.FONT_HERSHEY_COMPLEX

kernel=np.ones((3,3),np.uint8)



gauss=cv2.GaussianBlur(img,(7,7),2)

sharpened=cv2.addWeighted(img,3.5,gauss,-2.5,0)

erosion1=cv2.erode(sharpened,kernel,iterations=1)
sharpened=cv2.dilate(erosion1,kernel,iterations=2)


_, thresh = cv2.threshold(sharpened, 100, 255, cv2.THRESH_BINARY)



contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #bu komutla siyah beyaz görüntüden tüm şekillerin sınırlanı belirledik

#döngüye sokarız çünkü her şeklin kontur koordinatlarını alırız
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x, y), font, 1, (0))
    else:
        cv2.putText(img, "Circle", (x, y), font, 1, (0))

cv2.imshow("shapes", img)








cv2.imshow("img", img)
cv2.imshow("shar", sharpened)

cv2.imshow("thresh", thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()