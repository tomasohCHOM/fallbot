import cv2
import cvzone
import math
from ultralytics import YOLO

cap = cv2.VideoCapture("video/falling.mp4")
# Change to this when using raspbot
# cap = cv2.VideoCapture(0)

model = YOLO("yolov8s.pt")

classnames = []
with open("classes/classes.txt", "r") as f:
    classnames = f.read().splitlines()


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (980, 740))

    results = model(frame)

    for info in results:
        parameters = info.boxes
        for box in parameters:
            # Get the x1, x2, y1, and y2 coordinates from the box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            conf = math.ceil(box.conf[0] * 100)
            class_detect = classnames[int(box.cls[0])]

            # Calculate the height and the width of the entity
            height = y2 - y1
            width = x2 - x1
            threshold = height - width

            # Only process fall detection for class "person"
            if conf > 80 and class_detect == "person":
                cvzone.cornerRect(frame, [x1, y1, width, height], l=30, rt=6)
                cvzone.putTextRect(
                    frame, f"{class_detect}", [x1 + 8, y1 - 12], thickness=2, scale=2
                )
                if threshold < 0:
                    cvzone.putTextRect(
                        frame, "Fall Detected", [height, width], thickness=2, scale=2
                    )

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("t"):
        break


cap.release()
cv2.destroyAllWindows()
