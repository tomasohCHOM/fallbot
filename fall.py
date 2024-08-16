import cv2
import cvzone
import math
import time
from ultralytics import YOLO
import emergency

VIDEO_PATH = "video/fall1.mp4"  # Replace with 0 when using raspbot
TIME_TILL_EMERGENCY_MESSAGE = 5  # Seconds before raspbot sends emergency message
CONFIDENCE_THRESHOLD = 80  # Minimum confidence to consider detection

# Load YOLOv8 model
model = YOLO("yolov8s.pt")

# Load class names
with open("classes/classes.txt", "r") as f:
    classnames = f.read().splitlines()

cap = cv2.VideoCapture(VIDEO_PATH)

fallen = False
start_time = 0
# Every time a message is sent, value is doubled - resetted if no fall detected
retry_factor = 1


def detect_fall(box, class_detect, frame):
    global fallen, start_time, retry_factor
    # Get bounding coordinates from the box
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    # Calculate the height and the width of the entity
    height = y2 - y1
    width = x2 - x1
    threshold = height - width
    cvzone.cornerRect(frame, [x1, y1, width, height], l=30, rt=6)
    cvzone.putTextRect(
        frame, f"{class_detect}", [x1 + 8, y1 - 12], thickness=2, scale=2
    )

    if threshold < 0:
        if fallen:
            elapsed_time = time.time() - start_time
            if elapsed_time >= TIME_TILL_EMERGENCY_MESSAGE * retry_factor:
                emergency.send_emergency_message()
                retry_factor *= 2  # Double the retry factor
                fallen = False  # Reset after sending the message
        else:
            fallen = True
            start_time = time.time()

        cvzone.putTextRect(
            frame, "Fall Detected", [height, width], thickness=2, scale=2
        )
    else:
        fallen = False
        retry_factor = 1


def run():
    while True:
        ret, frame = cap.read()
        # Exit if video ends
        if not ret:
            break

        frame = cv2.resize(frame, (980, 740))
        results = model(frame)

        for result in results:
            for box in result.boxes:
                # Calculate the confidence and detected class of the object
                confidence = math.ceil(box.conf[0] * 100)
                class_detect = classnames[int(box.cls[0])]

                # Only process fall detection for class "person"
                if confidence > CONFIDENCE_THRESHOLD and class_detect == "person":
                    detect_fall(box, class_detect, frame)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("t"):
            break

    cap.release()
    cv2.destroyAllWindows()
