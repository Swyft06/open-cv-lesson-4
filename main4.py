import cv2
image = cv2.imread("pikachu.png")
text = "Hello"
pos = (150,150)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (0,0,0)
thickness = 2
image1 = cv2.putText(image,text,pos,font,fontScale,color,thickness)
cv2.imshow("output1",image1)

cv2.waitKey(0)
cv2.destroyAllWindows()