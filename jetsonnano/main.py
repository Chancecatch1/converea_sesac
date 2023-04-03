import cv2
import numpy as np
from collections import deque
import tensorflow as tf
import time
import os
import json
import socket
from firestore import init_db, setup_db, update_db

model_path = os.path.join(os.path.dirname(__file__), './model/converea') 
loaded = tf.saved_model.load(model_path)
SIZE = 10
q = deque(maxlen=SIZE)

HOST='192.168.14.8'
PORT=7477

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=800,
    display_height=480,
    framerate=10,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def text_pred(img, pred):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (150, 150)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    frame = cv2.putText(img, pred, org, font,
                        fontScale, color, thickness, cv2.LINE_AA)
    return frame


def read_capture():
    window_title = 'aiot'
    video_capture = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
    if video_capture.isOpened():
        try:
            # window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
            while True:
                ret_val, frame = video_capture.read()
                # if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                img = frame[60: 420, :420]
                rimg = cv2.resize(img, (150, 150)) / 255.0

                print(rimg.shape)
                pred = loaded([rimg])
                pred = np.asarray(pred)
                pred_ind = int(np.argmax(pred, axis=1)[0])
                q.append(pred_ind)
                print(str(pred_ind))
#                    pred_img = text_pred(img,pred_ind)
                # cv2.imshow(window_title, frame)
                if len(q) == SIZE:
                    growth = sum(q) / SIZE
                    print(growth)

                try:
                    print("connected....")
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect((HOST,7477))
                    client_socket.sendall('data'.encode('utf-8'))
                    data = client_socket.recv(1024)
                    if not data:
                        continue

                    data = data.decode('utf-8')
                    json_data = json.loads(data)
                    print(json_data["data"])
                    update_db(json_data["data"]["temp"], json_data["data"]["humidity"], json_data["data"]["turbidity"], json_data["data"]["ph"], json_data["data"]["liquid_level"], pred_ind)
                    client_socket.close()
                except Exception as e:
                    print(e)

                time.sleep(5)
                # else:
                #     break
                keyCode = cv2.waitKey(10) & 0xFF
                if keyCode == 27 or keyCode == ord('q'):
                    break
        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")

def read_capture_with_view():
    window_title = 'aiot'
    video_capture = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
    if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
            while True:
                ret_val, frame = video_capture.read()
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    img = frame[60: 420, :420]
                    rimg = cv2.resize(img, (150, 150)) / 255.0

                    print(rimg.shape)
                    pred = loaded([rimg])
                    pred = np.asarray(pred)
                    pred_ind = int(np.argmax(pred, axis=1)[0])
                    q.append(pred_ind)
                    print(str(pred_ind))
    #                    pred_img = text_pred(img,pred_ind)
                    cv2.imshow(window_title, frame)
                    if len(q) == SIZE:
                        growth = sum(q) / SIZE
                        print(growth)

                    try:
                        print("connected....")
                        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client_socket.connect((HOST,7477))
                        client_socket.sendall('data'.encode('utf-8'))
                        data = client_socket.recv(1024)
                        if not data:
                            continue

                        data = data.decode('utf-8')
                        json_data = json.loads(data)
                        print(json_data["data"])
                        update_db(json_data["data"]["temp"], json_data["data"]["humidity"], json_data["data"]["turbidity"], json_data["data"]["ph"], json_data["data"]["liquid_level"], pred_ind)
                        client_socket.close()
                    except Exception as e:
                        print(e)

                time.sleep(5)
                # else:
                #     break
                keyCode = cv2.waitKey(10) & 0xFF
                if keyCode == 27 or keyCode == ord('q'):
                    break
        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")

if __name__ == "__main__":
    init_db()
    setup_db()

    read_capture_with_view()
