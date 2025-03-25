import cv2
import time

# Initialize video capture object (0 for the default camera)
cam = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cam.isOpened():
    print("Error: Could not open video device")
    exit()

# Get camera properties
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Resolution: {width} x {height}")

# Initialize variables for FPS calculation
fps = 0
frame_count = 0
start_time = time.time()

while True:
    # Read a frame from the camera
    ret, frame = cam.read()

    # Check if frame is read correctly
    if not ret:
        print("Error: Could not read frame")
        break

    # Display the current frame in a window named 'Webcam'
    cv2.imshow('Webcam', frame)

    # Update the frame count
    frame_count += 1

    # Calculate FPS every second
    if time.time() - start_time >= 1:
        fps = frame_count / (time.time() - start_time)
        frame_count = 0
        start_time = time.time()

    # Print the FPS
    print(f"Frames per second: {fps:.2f}")

    # Wait for 1 ms and check for the 'q' key to quit the camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
