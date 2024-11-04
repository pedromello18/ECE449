import cv2
import time

def detect_frame(cap):
    _, image1 = cap.read()
    time.sleep(.05)
    _, image2 = cap.read()
    end = time.time()
    # Convert to BW
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    # Get Difference Image
    diff = cv2.absdiff(gray1, gray2)
    # Median Blur
    blur = cv2.medianBlur(diff, 5)
    binary = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 11, 2)
    # HACK
    binary = cv2.bitwise_not(binary)
    # Contour Detection
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    motionDetected = False

    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        if area < 1250: continue
        else: motionDetected = True

    return motionDetected

def detect_video(cap):
    start, end = 0, 0
    while(1):
        _, image1 = cap.read()
        time.sleep(.05)
        _, image2 = cap.read()
        end = time.time()
        # Convert to BW
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        # Get Difference Image
        diff = cv2.absdiff(gray1, gray2)
        # Median Blur
        blur = cv2.medianBlur(diff, 5)
        binary = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 11, 2)
        # HACK
        binary = cv2.bitwise_not(binary)
        # Contour Detection
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motionDetected = False
        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            if area < 1250: continue
            else: motionDetected = True
            # Add display imshow here if needed
        fps = 1 / (end - start)
        start = end
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'): break

def run_detection():
    cap = cv2.VideoCapture(-1)
    return detect_frame(cap)
