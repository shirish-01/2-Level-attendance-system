"""
=========================================
FACE RECOGNITON FUNCTIONALITY           ||
                              2ND LEVEL ||
=========================================
"""

import time

import cv2
import face_recognition


# AUTHENTICATION OF RESPECTIVE USER'S FACE
def authenticate(rollNo):
    # READING THE RESPECTED ROLL.NO IMAGE AND CONVERTING THE FORMAT
    s_img = cv2.imread(str(rollNo) + '.JPG')
    s_img = cv2.cvtColor(s_img, cv2.COLOR_BGR2RGB)

    cap = cv2.VideoCapture(0)
    # ENCODING THE IMAGE
    s_encodings = face_recognition.face_encodings(s_img)
    flag = False
    count = 0
    while True:
        _, s_imgCap = cap.read()

        if len(face_recognition.face_encodings(s_imgCap)) > 0:
            bboxCap = face_recognition.face_locations(s_imgCap)[0]
            s_encodingsCap = face_recognition.face_encodings(s_imgCap)[0]

            # COMPARING THE USER'S FACE
            # IF TRUE PRINTS AUTHENTICATED AND MARKS THE ATTENDANCE IN EXCEL SHEET
            if face_recognition.compare_faces(s_encodings, s_encodingsCap)[0]:
                cv2.rectangle(s_imgCap, (bboxCap[3], bboxCap[0]), (bboxCap[1], bboxCap[2]), (0, 255, 0), 2)
                cv2.putText(s_imgCap, 'Authenticated', (bboxCap[3], bboxCap[2] + 25), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2)

                flag = True
            # IF FALSE SHOWS WRONG PERSON AND CLOSED
            else:
                cv2.rectangle(s_imgCap, (bboxCap[3], bboxCap[0]), (bboxCap[1], bboxCap[2]), (0, 255, 0), 2)
                cv2.putText(s_imgCap, 'Wrong Person', (bboxCap[3], bboxCap[2] + 25), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2)
                count += 1

        # IF NO FACE DETECTED SHOWS THE BELOW MESSAGE AND TERMINATES
        else:
            cv2.putText(s_imgCap, 'No face identified', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            count += 1

        cv2.imshow('face_recognition', s_imgCap)  # output
        cv2.waitKey(1)

        # HERE THE COUNT SHOULD BE ASSIGNED NEAR TO THE CLIENT'S FPS FOR BETTER PERFORMANCE
        # 30FPS BY DEFAULT
        if count == 30 or flag:  # put closer to your screen's fps
            time.sleep(2)
            break
    cv2.destroyAllWindows()
    return flag


'''MAIN FUNCTION'''
if __name__ == '__main__':
    print(authenticate(128))
