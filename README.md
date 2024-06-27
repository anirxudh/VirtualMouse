# EzCursor

# Virtual Mouse Using Hand Gestures

This project implements a virtual mouse using hand gestures detected via a webcam. It uses OpenCV for video processing, MediaPipe for hand tracking and finger detection, and PyAutoGUI for controlling the mouse.


## Introduction

The Virtual Mouse project enables users to control their computer's mouse pointer using hand gestures captured by the webcam. This innovative approach to human-computer interaction can be particularly useful for presentations, accessibility, and hands-free control of a computer. I have implemented this project to learn the concepts and impact of OpenCV

## Features

- Real-time hand-finger detection using MediaPipe
- Smooth cursor movement with OpenCV
- Click actions based on the distance between the thumb and index finger
- Easy-to-setup and use

## Requirements

- Python 3.x
- OpenCV
- MediaPipe 3.20.x
- PyAutoGUI

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/anirxudh/VirtualMouse.git
    ```
2. Navigate to the project directory:
    ```sh
    cd virtual-mouse
    ```
3. Install the required packages:
    ```sh
    pip install opencv-python
    pip install mediapipe 3.20.0
    pip install PyAutoGUI
    ```

## Usage

1. Run the virtual mouse script:
    ```sh
    python EzCursor.py
    ```
2. Use your hand gestures in front of the webcam to control the mouse pointer.
3. For simple cursor control use your index finger and for clicks one may use pick gesture(thumb and index finger are close)

## How It Works

The application uses the following steps to function:

1. **Capture Video**: The webcam captures video frames in real-time.
2. **Hand Detection**: MediaPipe processes each frame to detect hand landmarks.
3. **Gesture Recognition**: Specific landmarks (index finger tip and thumb tip) are identified.
4. **Cursor Movement**: The position of the index finger tip is mapped to the screen coordinates to move the cursor.
5. **Click Detection**: The distance between the thumb tip and index finger tip is calculated to determine click actions.

## Building Components

1. **OpenCV**: Used for capturing video frames and processing images.
2. **MediaPipe**: Used for detecting and tracking hand landmarks.
3. **PyAutoGUI**: Used for controlling the mouse pointer and performing click actions.
4. **Numpy**: Used for efficient numerical operations and smoothing cursor movements.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
