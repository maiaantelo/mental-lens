import cv2
import time

# 1. Load the 'Eye' of the AI
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Start the Webcam (Try 0, if that fails, try 1)
cap = cv2.VideoCapture(1)

# Give the camera 2 seconds to warm up
print("Warming up camera...")
time.sleep(2)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("AI Vision ACTIVE. Look at the camera. Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # Drawing the 'Mental Lens' interface
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "USER DETECTED: MONITORING", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('Mental Lens - Vision Modality', frame)

    # Critical for Macs: waitKey(1) keeps the window open
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Add these lines to force the window to close on Mac
cv2.waitKey(1)
cv2.waitKey(1)