import cv2
image = cv2.imread("pikachu.png")
start = (0,0)
end = (200,200)
color = (0,255,0)
thickness = 2
image1 = cv2.line(image,start,end,color,thickness)
cv2.imshow("output",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()