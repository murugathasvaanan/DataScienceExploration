import cv2
import numpy as np

# Read image.
img = cv2.imread('H04_2_q1.jpg', cv2.IMREAD_COLOR)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 35, minRadius = 1, maxRadius = 40)

# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circle", img)

        intensity1 = int(gray[b,a])
        intensity2 = int(gray[b + 1,a])
        intensity3 = int(gray[b - 1,a])
        intensity4 = int(gray[b,a + 1])
        intensity5 = int(gray[b,a - 1])
        avgintensity = str((intensity1+intensity2+intensity3+intensity4+intensity5)/5)

        a = open('intensitylist.txt', 'a')
        a.write(str(intensity1))
        a.write('\n')
        a.write(str(intensity2))
        a.write('\n')
        a.write(str(intensity3))
        a.write('\n')
        a.write(str(intensity4))
        a.write('\n')
        a.write(str(intensity5))
        a.write('\n')
    a.close()
    cv2.waitKey(0)
