import cv2

# camera
cap = cv2.VideoCapture(0)

# file
# cap = cv2.VideoCapture('/root/Videos/Screencast_07-12-19_11:52:06 PM IST.webm')

if cap.isOpened() == False:
    exit()
    
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    

cap.release()
cv2.destroyAllWindows()

'''
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
