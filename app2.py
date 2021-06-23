import cv2
import pytesseract 


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'



cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read() 
    
    if ret == True:

        #frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

        Himg, Wimg, _ = frame.shape
        boxes = pytesseract.image_to_boxes(frame, lang="tha+eng")

        for i in boxes.splitlines(): 
            i = i.split(' ')
            x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])
            cv2.rectangle(frame, (x,Himg - y), ( w, Himg - h), (225,50,20), 2)
            cv2.putText(frame,i[0], (x, Himg-y),cv2.QT_FONT_NORMAL,1,(50,50,255),2)


        #frame = cv2.flip(frame,1)
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) & 0xff == ord("e"):
            break
    else:
        break 

cap.release()
cv2.destroyAllWindows()

# img = cv2.imread('./image_processing/image/rescale_img.jpg')

# print(pytesseract.image_to_string(img, lang="tha+eng"))

#Detecting Characters 
#Debug
# print(pytesseract.image_to_boxes(img, lang="eng"))

# Himg, Wimg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img, lang="eng")

# for itera,i in enumerate(boxes.splitlines()): 

#     if itera != 0:
#         i = i.split()
#         print(i)

#     #Debug 
#     #print(i)
    
#     #print(i)
#         x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])
#         cv2.rectangle(img, (x,Himg - y), ( w, Himg - h), (225,50,20), 2)
#     #print(i)

#         cv2.putText(img,i[0], (x, Himg-y),cv2.QT_FONT_NORMAL,1,(50,50,255),2)

# cv2.imshow('result',img)

# cv2.waitKey(0)

