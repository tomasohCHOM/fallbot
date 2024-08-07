import cv2
import torch
import numpy as np

# Load YOLO model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")


# Define a function to detect falls
def detect_fall(boxes, threshold=0.5):
    for box in boxes:
        # box format: [x1, y1, x2, y2, confidence, class]
        x1, y1, x2, y2, conf, cls = box
        if cls == 0:  # class 0 is for 'person'
            width = x2 - x1
            height = y2 - y1
            if (
                height < threshold * width
            ):  # Simple heuristic: if height < threshold * width, it's a fall
                return True
    return False


# Capture video from webcam
cap = cv2.VideoCapture("video/falling.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)
    boxes = results.xyxy[0].cpu().numpy()

    # Check for falls
    if detect_fall(boxes):
        cv2.putText(
            frame,
            "Fall Detected",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )

    # Display the frame
    cv2.imshow("Fall Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
