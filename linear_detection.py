"""
How the algorithm works:
Image Capture: It captures two sequential images using a camera (you can adjust the time interval between captures with time.sleep).
Grayscale Conversion: The images are immediately converted to grayscale to focus on intensity rather than color.
Difference Calculation: The absolute difference between the two grayscale images is calculated to pinpoint areas of change.
Movement Detection: The detect_movement function applies a threshold to the difference image, isolating the pixels where significant changes (likely due to movement) occurred.
You can adjust parameters like the camera index, threshold value for movement detection, and time interval to suit your specific use case.
"""

import cv2
import numpy as np
import time

def capture_image(camera_index=0):
    """Capture an image using the camera."""
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Camera not accessible")
        return None
    ret, frame = cap.read()
    cap.release()
    if ret:
        return frame
    else:
        print("Error: Could not capture an image")
        return None

def convert_to_grayscale(image):
    """Convert an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def calculate_difference(image1, image2):
    """Calculate the absolute difference between two grayscale images."""
    return cv2.absdiff(image1, image2)

def detect_movement(difference_image, threshold=30):
    """Detect areas of movement by applying a threshold to the difference image."""
    _, thresh = cv2.threshold(difference_image, threshold, 255, cv2.THRESH_BINARY)
    return thresh

def main():
    # Step 1: Capture the first image
    print("Capturing first image...")
    image1 = capture_image()

    # Wait for a short interval (e.g., 1 second)
    time.sleep(1)

    # Step 2: Capture the second image
    print("Capturing second image...")
    image2 = capture_image()

    if image1 is None or image2 is None:
        print("Error: One or both images could not be captured.")
        return

    # Step 3: Convert both images to grayscale
    gray_image1 = convert_to_grayscale(image1)
    gray_image2 = convert_to_grayscale(image2)

    # Step 4: Calculate the absolute difference between the two grayscale images
    difference_image = calculate_difference(gray_image1, gray_image2)

    # Step 5: Detect movement by applying a threshold
    movement_mask = detect_movement(difference_image)

    # Display results
    cv2.imshow("Difference Image", difference_image)
    cv2.imshow("Movement Detection", movement_mask)

    # Wait for the user to press a key and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
