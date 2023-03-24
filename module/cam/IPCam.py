from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from threading import Thread
from PySide6.QtGui import QImage, QPixmap
import cv2
from module.ImageTool import create_filename

class IPCam(Thread):
    lnk_connect: str = None
    qLabel: QLabel = None

    def __init__(self, parent=None) -> None:
        Thread.__init__(self, parent)
        self.status = True
        self.cap = True

    def run(self) -> None:
        self.cap = cv2.VideoCapture()
        
        while self.status:
            self.cap.open(self.lnk_connect)
            ret, frame = self.cap.read()
            if not ret:
                continue

            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            h, w, ch = color_frame.shape
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            self.__scaled_img = QPixmap.fromImage(img.scaled(640, 480, Qt.KeepAspectRatio))

            self.qLabel.setPixmap(self.__scaled_img)

            # "http://admin:admin102030@192.168.1.108/cgi-bin/snapshot.cgi?2"\
    
    def stop_cam(self):
        print("Stopped...")
        self.cap.release()
        self.status = False
        # cv2.destroyAllWindows()
        self.join()

    def cupture_image(self, qLabel: QLabel) -> str:
        name_file = create_filename()
        qLabel.setPixmap(self.__scaled_img)
        self.__scaled_img.save(name_file, 'jpg')
        return name_file