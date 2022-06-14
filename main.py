import PySimpleGUI as sg
import cv2
#opencv

layout = [
    [sg.Image(key='-IMAGE-')],
    [sg.Button('Record', size=(6, 1)),
    sg.Button('Stop', size=(6, 1)),
    sg.Button('Exit', size=(6, 1))]
]
#Record and Stop not functional

window = sg.Window('Open CV', layout)
#init window

# get video
video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face classifier
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#eyes classifier
while True:
    event, values = window.read(timeout=0)
    if event == 'Exit':
        #exit event
        pass
    else:
        if event == sg.WIN_CLOSED:
            #win closed
            pass
        else:
            _, frame = video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #grayscale
            # draw the rectangles
            for [x, y, w, h] in face_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=7,
                    minSize=(30, 30)):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # draw rectangle face
                cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                # draw rectangle face detection text
            for [x, y, w, h] in eyes_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=7,
                    minSize=(20, 20)):
                    #20x20 recommended
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #draw rectangle eyes
                cv2.putText(frame, 'Eye', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                # draw rectangle eyes detection text
            # update image
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()
            window['-IMAGE-'].update(data=imgbytes)
            continue
    break
# update the text
window.close()
#close
