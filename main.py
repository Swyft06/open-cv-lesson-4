import cv2
image = cv2.imread("pikachu.png")
center_coordinates = (100,100)
radius = 50
color = (255,0,0)
thickness = 2
thickness1 = -2
image1 = cv2.circle(image,center_coordinates,radius, color,thickness)
cv2.imshow("Output",image1)
image2 = cv2.circle(image,center_coordinates,radius,color,thickness1)
cv2.imshow("Output2",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()