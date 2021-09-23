import cv2


""" Requirements:

       - opencv-python==3.4.3.18

"""



def detect_face_on_image():       # Detection on Image

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    image = cv2.imread("Face.jpg")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:

        cv2.rectangle(image,(x, y), (x + w, y + h), (255, 200, 0), 2)

    cv2.imshow("Detected Faces",image)
    cv2.waitKey()



def detect_face_on_video():   # Detection on Video

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture("faces_human.mp4")

    while True:

        _,image = cap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces_on_video = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces_on_video:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 100), 2)


        cv2.imshow("Detected Faces", image)
        k = cv2.waitKey(30) & 0xff            # Press Esc Button to close video screen
        if k ==27:
            break

    cap.release()



def detect_face_on_webcam():                        # Detection on Webcam

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    while True:

        _,image = cap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces_on_webcam = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces_on_webcam:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

        cv2.imshow("Detected Faces", image)
        k = cv2.waitKey(30) & 0xff            # Press Esc Button to close video screen
        if k ==27:
            break

    cap.release()



def run_program():

    while True:

        que = input("""Please Select Detection Process:
        
        - Face Detection on Image: 1
        -- Face Detection on Video: 2
        --- Face Detection on Webcam: 3""")

        if que == "1":

            detect_face_on_image()
            break

        elif que =="2":
            detect_face_on_video()
            break

        else:
            detect_face_on_webcam()
            break




run_program()





