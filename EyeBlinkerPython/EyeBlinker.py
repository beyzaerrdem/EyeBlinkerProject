from tkinter import messagebox
import cv2 
import dlib 

from scipy.spatial import distance
from imutils import face_utils

from threading import Timer
import winsdk.windows.ui.notifications as notifications
import winsdk.windows.data.xml.dom as dom
import Const
from Database import Database

class EyeBlinker:
    def __init__(self,isRecord = False):
        self.timer = Timer(60,self.Check)
        self.database = Database()
        self.predictor2 = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        self.detector2 = dlib.get_frontal_face_detector()
        self.minimumEyeBlinkerCount = Const.CurrentUser.get('EyeBlinkCount')
        self.startCount = None
        self.isContunie = True
        self.isRecord = isRecord
        self.total = 0
        self.count = 0
        self.uyariText = "1 DAKIKA BOYUNCA GEREKENDEN AZ SAYIDA GOZ KIRPTINIZ"
        self.tString = """
        <toast>
            <visual>
                <binding template='ToastGeneric'>s
                    <text>1 DAKİKA BOYUNCA GEREKENDEN AZ SAYIDA GÖZ KIRPTINIZ</text>
                    <text>GÖZ KIRP!</text>
                </binding>
            </visual>
        </toast>
        """
        self.xDoc = dom.XmlDocument()
        self.xDoc.load_xml(self.tString)
        self.cap = cv2.VideoCapture(0)

    def Check(self):
        if self.isRecord:
            self.isContunie = False  #bir kez çalışması için
            self.database.InsertEyeBlinkCount(self.total)
            messagebox.showinfo(message="Göz kırpma sayınız {} olarak güncellendi !".format(self.total),title="Kullanılacak olan göz kırpma sayınız")
            self.timer.cancel()
            
        else:
            print("60 SANİYE DOLDU")
            print(self.total)
            print(self.startCount)
            if self.total - self.startCount < self.minimumEyeBlinkerCount:
                notifications.ToastNotificationManager.create_toast_notifier().show(notifications.ToastNotification(self.xDoc))
        
    def start(self):
        self.startCount = self.total
        self.timer.start()
        while True:
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            rects = self.detector(gray, 0)
            for rect in rects:
                shape = self.predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                leftEye = shape[36:42]
                rightEye = shape[42:48]

                leftEAR = self.eye_aspect_ratio(leftEye)
                rightEAR = self.eye_aspect_ratio(rightEye)

                ear = (leftEAR + rightEAR) / 2.0

                if ear < 0.25:
                    self.count += 1
                else:
                    if self.count >= 3:
                        self.total += 1
                    self.count = 0

                cv2.putText(frame, "Goz Kirpma Sayisi: {0} {1}".format(self.total,self.uyariText), (10, 30),cv2.FONT_HERSHEY_COMPLEX, 0.8, (100, 87, 135),2)

            cv2.imshow("Frame", frame)

            try :
                if cv2.waitKey(1) & 0xff==ord('w') or cv2.getWindowProperty('Frame',1) == -1  or not self.isContunie:
                    self.timer.cancel()
                    cv2.destroyAllWindows()
                    break
            except :
                    self.timer.cancel()
                    break

        cv2.destroyAllWindows()
        self.cap.release()

    def eye_aspect_ratio(self,eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])

        C = distance.euclidean(eye[0], eye[3])
        eye = (A + B) / (2.0 * C)

        return eye

    def predictor(self,gray, rect):
        return self.predictor2(gray, rect)
    
    def detector(self,gray, rect):
        return self.detector2(gray, rect)