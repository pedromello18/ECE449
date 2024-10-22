"""
How the algorithm works:
Image Capture: It captures two sequential images using a camera (you can adjust the time interval between captures with time.sleep).
Grayscale Conversion: The images are immediately converted to grayscale to focus on intensity rather than color.
Difference Calculation: The absolute difference between the two grayscale images is calculated to pinpoint areas of change.
Movement Detection: The detect_movement function applies a threshold to the difference image, isolating the pixels where significant changes (likely due to movement) occurred.
You can adjust parameters like the camera index, threshold value for movement detection, and time interval to suit your specific use case.

Additional Elements Explanation:

Median Blurring: This step reduces noise in the difference image by applying a median blur, which helps smooth out random pixel fluctuations caused by factors like camera noise or subtle lighting shifts.
blurred_image = apply_median_blur(difference_image)

Adaptive Thresholding: Instead of using a fixed threshold, adaptive thresholding adjusts the threshold dynamically based on local variations in the image, making it more effective in varying lighting conditions.
binary_image = apply_adaptive_threshold(blurred_image)

Contour Detection: Contours are extracted from the binary image using cv2.findContours. These contours represent the regions of the image where movement is detected. The contours are then drawn on the original image for visualization.
contours = detect_contours(binary_image)

Contour Visualization: The algorithm draws contours on the original image to show the areas where movement was detected.
cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)
"""

import RPi.GPIO as GPIO
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
    print(frame.shape)
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

def apply_median_blur(image, kernel_size=5):
    """Apply median blur to reduce noise in the difference image."""
    return cv2.medianBlur(image, kernel_size)

def apply_adaptive_threshold(image):
    """Apply adaptive thresholding to create a binary image from the difference image."""
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

def detect_contours(binary_image):
    """Detect contours in the binary image."""
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def main():
    # Step 1: Capture the first image
    cap = cv2.VideoCapture(0)
    ret, image1 = cap.read() # first image
    time.sleep(1)
    ret, image2 = cap.read()
    cap.release()
    image3 = image2.copy()

    if image1 is None or image2 is None:
        print("Error: One or both images could not be captured.")
        return

    # Step 3: Convert both images to grayscale
    gray_image1 = convert_to_grayscale(image1)
    gray_image2 = convert_to_grayscale(image2)

    # Step 4: Calculate the absolute difference between the two grayscale images
    difference_image = calculate_difference(gray_image1, gray_image2)

    # Step 5: Apply median blurring to reduce noise
    blurred_image = apply_median_blur(difference_image)

    # Step 6: Apply adaptive threshold to create a binary mask
    binary_image = apply_adaptive_threshold(blurred_image)
    binary_image = cv2.bitwise_not(binary_image)
    # Step 7: Detect contours in the binary mask to identify movement regions
    contours = detect_contours(binary_image)

    # # Step 8: Draw contours on the original image for visualization
    image_with_contours = image2.copy()
    # cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    for i, c in enumerate(contours): 
        area = cv2.contourArea(c)
        print(area)
        if area < 1000: 
            continue
        cv2.drawContours(image3, contours, i, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(c)
        if (x, y, w, h) == (0, 0, 640, 480): continue
        cv2.rectangle(image3, (x, y), (x+w, y+h), (0, 0, 255), 2)
        text = "Detected"
        cv2.putText(image3, f"{area}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0))
        cv2.putText(image3, "Motion: {}".format(text), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # Set up the GPIO pin
        LED_PIN = 17
        GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
        GPIO.setup(LED_PIN, GPIO.OUT)  # Set the pin as an output

        # Turn on the LED
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED is ON")

        # Wait for 5 seconds
        time.sleep(5)

        # Turn off the LED
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED is OFF")

        # Clean up GPIO settings
        GPIO.cleanup()

    # # Display results
    # cv2.imshow("Difference Image", difference_image)
    # cv2.imshow("Blurred Difference Image", blurred_image)
    cv2.imshow("Binary Image", binary_image)
    cv2.imshow('First', image1)
    # cv2.imshow("Contours Detected", image_with_contours)
    cv2.imshow("Contour Boxes", image3)
    # Wait for the user to press a key and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()