import cv2
import socket
import pickle
import struct

server = 'localhost'
port   = 8000

def main():
    # camera
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == False:
        print("Couldn't open the Camera. Exiting..")
        exit()
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((server, port))
    print("Connected to " + server + " at " + str(port))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == False:
            print("Couldn't read from camera")
            break
        # display
        cv2.imshow("VideoC", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # frame serialised
        data = pickle.dumps(frame)
        # use 'L' for larger frame. 'H' -> unsigned int, 'L' -> unsigned long
        clientsocket.sendall(struct.pack('L', len(data)) + data)
    clientsocket.sendall(struct.pack('L', 0) + "")
    print("Exiting..")
    cap.release()
    cv2.destroyAllWindows()
    clientsocket.close()

if __name__ == "__main__":
    main()
