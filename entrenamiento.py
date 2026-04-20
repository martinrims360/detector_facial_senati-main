import cv2
import os
import numpy as np

dataPath = "./data"
peopleList = os.listdir(dataPath) # [juan, pedro , saul]
print('Lista de personas : ', peopleList)

#Variables iniciales
labels = [] #[0,0,0,1,1,1]
facesData = []
label = 0

print('Leyendo las imagenes...')
for nameDir in peopleList :
    personPath = dataPath + '/' + nameDir

    for fileName in os.listdir(personPath) :
        print('Rostro: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath + '/' + fileName, 0))
    label = label + 1

face_recognizer =cv2.face.LBPHFaceRecognizer_create()

#Entrenar al modelo
print("Entrenando modelo...")
face_recognizer.train(facesData, np.array(labels))
face_recognizer.write('modelo.xml')
print("Modelo entrenado")

