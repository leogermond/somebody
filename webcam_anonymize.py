import cv2
import anonymize

def main():
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while True:
        check, frame = webcam.read()
        if not check:
            break

        anon = anonymize.anonymize_faces(frame, min_faces=2, strokes=4)
        cv2.imshow('frame', anon)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    webcam.release()

if  __name__ == "__main__":
    main()
