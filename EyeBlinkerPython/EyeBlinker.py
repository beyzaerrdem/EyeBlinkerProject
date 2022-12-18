import cv2 
import dlib 

from scipy.spatial import distance
from imutils import face_utils

from threading import Timer
import winsdk.windows.ui.notifications as notifications
import winsdk.windows.data.xml.dom as dom

tString = """
<toast>
    <visual>
        <binding template='ToastGeneric'>s
            <text>1 DAKİKA BOYUNCA GEREKENDEN AZ GÖZ KIRPTINIZ</text>
            <text>GÖZ KIRP!</text>
        </binding>
    </visual>
</toast>
"""
xDoc = dom.XmlDocument()
xDoc.load_xml(tString)


#create notifier

nManager = notifications.ToastNotificationManager
notifier = nManager.create_toast_notifier();

cap = cv2.VideoCapture(0)  #0 olma sebebi birden çok kamera olabilir ve dahili kamerayı algılaması için 

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])

    C = distance.euclidean(eye[0], eye[3])
    eye = (A + B) / (2.0 * C)

    return eye

count = 0
total = 0

baslangic=total
uyariText = ""

kontrolSaniye = 10
minimumEyeBlinkerCount = 5

def check():
    print("60 SANİYE DOLDU")
    global uyariText
    global baslangic
    global t
    global notifier
    if total-baslangic < minimumEyeBlinkerCount:    
        uyariText = "1 DAKIKA BOYUNCA GEREKENDEN AZ GOZ KIRPTINIZ"
        notifier.show(notifications.ToastNotification(xDoc))
    else:
        uyariText = ""
    t = Timer(kontrolSaniye,check)
    t.start()
    baslangic = total

t = Timer(kontrolSaniye,check)
t.start()
while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #gri algılamayı renkli yapmak için 
    faces = detector(imgGray)

    for face in faces:
        landmarks = predictor(imgGray,face)

        landmarks = face_utils.shape_to_np(landmarks)
        leftEye = landmarks[42:48]
        rightEye = landmarks[36:42]

        leftEye = eye_aspect_ratio(leftEye)
        rightEye = eye_aspect_ratio(rightEye)

        eye = (leftEye + rightEye) / 2.0

        if eye<0.3:
            count+=1
        else:
            if count>=3:
                total+=1

            count=0
        bitis = total

    cv2.putText(img, "Goz Kirpma Sayisi: {0} {1}".format(total,uyariText), (10, 30),cv2.FONT_HERSHEY_COMPLEX, 0.8, (100, 87, 135),2)
    cv2.imshow('Video',img)
    
    try :
        if cv2.waitKey(1) & 0xff==ord('w') or cv2.getWindowProperty('Video',1) == -1 :
            t.cancel()
            break
    except :
            t.cancel()
            break