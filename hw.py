import cv2

image = cv2.imread("white2.jpg")

cv2.rectangle(image, (150, 50), (250, 350), (50, 50, 50), -1)

cv2.circle(image, (200, 110), 30, (0, 0, 255), -1)

cv2.circle(image, (200, 200), 30, (0, 255, 255), -1)

cv2.circle(image, (200, 290), 30, (0, 255, 0), -1)

cv2.imshow("Traffic Signal", image)
cv2.waitKey(0)
cv2.destroyAllWindows()