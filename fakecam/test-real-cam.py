import sys
import cv2

print("Python version: {}.{}.{}".format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro))
print("Capturing 1 frame from real camera")

# Test real cam:
cap = cv2.VideoCapture('/dev/video0')
height, width = 720, 1280
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 60)
success, frame = cap.read()
cv2.imwrite("real-cam.jpg", frame)