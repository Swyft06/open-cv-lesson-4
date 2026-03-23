import cv2
image = cv2.imread("pikachu.png")
start = (100,100)
end = (300,300)
color = (0,0,255)
thickness1 = 2
thickness2 = -2
image1 = cv2.rectangle(image,start,end,color,thickness1)
cv2.imshow("output",image1)
image2 = cv2.rectangle(image,start,end,color,thickness2)
cv2.imshow("output1",image2) 
cv2.waitKey(0)
cv2.destroyAllWindows()