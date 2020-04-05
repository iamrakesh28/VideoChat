import cv2
import socket
import pickle
import struct

host = ''
port = 8000

def main():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print("Socket bind complete")
    server.listen(10)
    print("Listening...")

    conn, addr = server.accept()

    data = ""
    payload_size = struct.calcsize("L")
    while True:
        while len(data) < payload_size:
            data += conn.recv(4096)
        msg_size = data[: payload_size]
        data = data[payload_size :]
        msg_size = struct.unpack('L', msg_size)[0]
        if msg_size == 0:
            break
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame = data[: msg_size]
        data = data[msg_size :]

        frame = pickle.loads(frame)
        cv2.imshow('VideoS', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    conn.close()

if __name__ == "__main__":
    main()
