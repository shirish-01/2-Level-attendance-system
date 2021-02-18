"""
=============================================
QR AUTHENTICATION FUNCTIONALITY             ||
                                 1ST LEVEL  ||
==============================================
"""

import datetime
import re
import time

import cv2
import numpy as np
from pyzbar.pyzbar import decode

# THIS FUNCTION CREATES A .CSV FILE ON CURRENT DATE
# FORMAT OF FILE "YEAR-MONTH-DAY.CSV" (HYPEHENS INCLUDED)
file_name = (str(datetime.datetime.now()).split())[0] + ".csv"
with open(file_name, 'a') as f:
    pass


# QR CODE AUTHENTICATION FUNCTION
def QRcodeAuthentication():
    # SETTING UP WEBCAM AND DIMENSIONS OF THE WINDOW
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    count = 0

    myData = None
    flag = False
    t = 0

    # OPENING THE RESPECTIVE CSV FILE , CHECKING FOR DUPLICATES
    with open((str(datetime.datetime.now()).split())[0] + ".csv") as f:
        myDataList = f.read().splitlines()

    while True:
        success, img = cap.read()
        t += 1

        # TAKING THE INPUT FROM WEBCAM AND DECODING IT.
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            count = 1

            # CHECKING IF GIVEN QR OCDE IS VALID USING REGEX
            x = re.search("^2451-18-733-(00[1-9]|0[1-9]\d|1[0-7]\d|180|30\d|31[0-8])$", myData)
            if x:
                flag = True

            # CHECKING IF USER HAS ALREADY GIVEN ATTENDANCE
            # IF YES NOTIFICATION IS GIVEN TO USER AND TERMINATED
            if myData + ",P" in myDataList:
                print("attendance already marked")
                flag = False

            # USED TO SHOW THE BOUNDARIES OF QR CODE IN WINDOW AND DECODED OUTPUT ON THE SCREEN
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 255, 0), 5)
            pts2 = barcode.rect
            cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (255, 0, 255), 2)

        cv2.imshow('Result', img)

        cv2.waitKey(1)

        # SCANS ONLY ONE QR CODE AT A TIME
        if (count == 1):
            time.sleep(2)
            cv2.destroyAllWindows()
            break
        if t == 300:
            break

    cv2.destroyAllWindows()

    return (flag, myData)


"""MAIN FUNCTION """
if __name__ == '__main__':
    print(QRcodeAuthentication())
