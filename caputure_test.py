

import sys
import cv2
import numpy as np
from tensorflow import keras

capture     = cv2.VideoCapture(0)
cascade     = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier("./haarcascade_eye.xml")
model       = keras.models.load_model('model.h5')
gender = -1
age = -1
def main(args):
    while(True):
        _, frame = capture.read()
        face_list = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3, minSize=(60, 60))
        showFrame = frame
        # print(len(face_list))
        if len(face_list) > 0:
            _x, _y, weight, height = face_list[0]
            frame = frame[_y:_y+height, _x:_x+weight]
            frame = cv2.resize(frame, (64, 64))
            frame = np.expand_dims(frame, axis=0)
            pred = model.predict(frame)
            gender = pred[0][0].argmax()
            age    = pred[1][0].argmax()
            print(pred[0][0].argmax(), pred[1][0].argmax())
            border_color = (0, 0, 255)
            border_size = 2
            cv2.rectangle(showFrame, (_x, _y), (_x+weight, _y+height), border_color, thickness=border_size)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.putText(showFrame, 
            text=('male' if gender == 0 else 'female') + " " + str(age),
            org=(100, 300),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            color=(0, 255, 0),
            fontScale=1.0,
            thickness=2,
            lineType=cv2.LINE_4
        )
        cv2.imshow('frame', showFrame)
        
if __name__ == '__main__':
    try:
        main(sys.argv)
    finally:
        capture.release()
        cv2.destroyAllWindows()
    