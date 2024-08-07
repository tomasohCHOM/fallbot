from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Open the video file
video_path = "../video/falling.mp4"
cap = cv2.VideoCapture(video_path)

# Store the track history
track_history = defaultdict(lambda: [])

# Calculate the total number of frames
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Get the frame dimensions
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_center = (frame_width // 2, frame_height // 2)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Get the boxes
        boxes = results[0].boxes.xywh.cpu() if results[0].boxes.xywh is not None else []

        # Get the track IDs if they exist, otherwise create an empty list
        if results[0].boxes.id is not None:
            track_ids = results[0].boxes.id.int().cpu().tolist()
        else:
            track_ids = []

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Plot the tracks
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            track = track_history[track_id]
            current_center = (float(x), float(y))
            track.append(current_center)  # x, y center point
            if len(track) > 30:  # Adjust this if needed
                track.pop(0)

            # Calculate the direction from the center of the screen
            direction_vector = (
                current_center[0] - frame_center[0],
                current_center[1] - frame_center[1],
            )
            direction = ""
            if abs(direction_vector[0]) > abs(direction_vector[1]):
                direction = "right" if direction_vector[0] > 0 else "left"
            else:
                direction = "down" if direction_vector[1] > 0 else "up"

            print(f"Track ID {track_id}: Heading {direction}")

            # Draw the tracking lines
            points = np.array(track, dtype=np.int32).reshape((-1, 1, 2))
            cv2.polylines(
                annotated_frame,
                [points],
                isClosed=False,
                color=(230, 230, 230),
                thickness=10,
            )

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
