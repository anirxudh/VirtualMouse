import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math

# Video capture
cap = cv2.VideoCapture(0)

# Mediapipe Hand Detector
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

# Variables for cursor movement
prev_x, prev_y = 0, 0
smoothing = 2  
# Scroll threshold
scroll_threshold = 30

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flipping
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert frames to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detection of hands
    result = hand_detector.process(rgb_frame)
    hand_landmarks = result.multi_hand_landmarks

    if hand_landmarks:
        for landmarks in hand_landmarks:
            drawing_utils.draw_landmarks(frame, landmarks)

            # Finding the coordinates of the index finger, thumb, and middle finger
            index_finger_tip = landmarks.landmark[8]
            thumb_tip = landmarks.landmark[4]
            middle_finger_tip = landmarks.landmark[12]

            index_x = int(index_finger_tip.x * frame_width)
            index_y = int(index_finger_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)
            middle_x = int(middle_finger_tip.x * frame_width)
            middle_y = int(middle_finger_tip.y * frame_height)

            # Marking the index, thumb, and middle fingers
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 255), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 255), -1)
            cv2.circle(frame, (middle_x, middle_y), 10, (0, 255, 255), -1)

            screen_x = np.interp(index_x, (0, frame_width), (0, screen_width))
            screen_y = np.interp(index_y, (0, frame_height), (0, screen_height))

            # Smoothen cursor movement
            smooth_x = prev_x + (screen_x - prev_x) / smoothing
            smooth_y = prev_y + (screen_y - prev_y) / smoothing

            # Move the cursor
            pyautogui.moveTo(smooth_x, smooth_y)
            prev_x, prev_y = smooth_x, smooth_y

            # Checking for left click
            if abs(index_y - thumb_y) < 20 and abs(index_x - thumb_x) < 20:
                pyautogui.click()
                pyautogui.sleep(0.1)  

            # Checking for right click
            if abs(middle_y - thumb_y) < 20 and abs(middle_x - thumb_x) < 20:
                pyautogui.click(button='right')
                pyautogui.sleep(0.1)  
            # Checking for scroll
            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
            if distance > scroll_threshold:
                if index_y < thumb_y:
                    pyautogui.scroll(-5) 
                else:
                    pyautogui.scroll(5)  

    # Display the frame
    cv2.imshow('Virtual Mouse', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
