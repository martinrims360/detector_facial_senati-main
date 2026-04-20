import cv2
import os
from camera import getcamera

dataPath = './data'
imagePath = os.listdir(dataPath)
print('Lista de personas : ', imagePath)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("modelo.xml")
faceClassif = cv2.CascadeClassifier("rostros.xml")

# abrir la camara
camera = getcamera()
cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150))

        resul = face_recognizer.predict(rostro)

        if resul[1] < 75:
            cv2.putText(frame, '{}'.format(imagePath[resul[0]]),
                        (x, y - 25), 2, 1, (0,255,0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0,255,0), 2)
        else:
            cv2.putText(frame, 'Desconocido',
                        (x,y - 25), 2, 1, (0,0,255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0,0,255), 2)

    # 👇 ESTO VA FUERA DEL FOR
    cv2.imshow('Reconociendo Rostros', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 👇 ESTO VA FUERA DEL WHILE
cap.release()
cv2.destroyAllWindows()