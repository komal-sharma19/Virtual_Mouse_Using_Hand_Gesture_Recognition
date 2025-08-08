# Virtual_Mouse_Using_Hand_Gesture_Recognition

### Hand Gesture Controlled Mouse using OpenCV & MediaPipe


This project lets you **control your mouse cursor and perform actions** such as left click, right click, double click, and taking screenshots **just using your hand gestures** detected via webcam.

The implementation uses **OpenCV** for video capture, **MediaPipe Hands** for real-time hand landmark detection, and **PyAutoGUI** to control the mouse and keyboard functions.

---

## 📌 Features

- **Move mouse cursor** using index finger.
- **Left Click** gesture.
- **Right Click** gesture.
- **Double Click** gesture.
- **Take Screenshot** gesture.
- Works in **real time** with minimal latency.
- Customizable gesture detection logic.

## Left Click ##
<p align="center">
  <img src="https://github.com/komal-sharma19/Virtual_Mouse_Using_Hand_Gesture_Recognition/blob/main/images/Screenshot%202025-08-08%20152311.png?raw=true" width="400" />
</p>

## Right Click ##
<p align="center">
  <img src="https://github.com/komal-sharma19/Virtual_Mouse_Using_Hand_Gesture_Recognition/blob/main/images/Screenshot%202025-08-08%20152325.png?raw=true" width="400" />
</p>

## Double Click ##
<p align="center">
  <img src="https://github.com/komal-sharma19/Virtual_Mouse_Using_Hand_Gesture_Recognition/blob/main/images/Screenshot%202025-08-08%20152338.png?raw=true" width="400" />
</p>

## Screenshot Taken ##
<p align="center">
  <img src="https://github.com/komal-sharma19/Virtual_Mouse_Using_Hand_Gesture_Recognition/blob/main/images/Screenshot%202025-08-08%20152459.png?raw=true" width="400" />
</p>



---

## 🛠️ Technologies Used

- [Python 3.8+](https://www.python.org/)
- [OpenCV](https://opencv.org/) – Video capture and image processing
- [MediaPipe](https://developers.google.com/mediapipe) – Hand landmark detection
- [PyAutoGUI](https://pyautogui.readthedocs.io/) – Mouse and keyboard automation
- [pynput](https://pynput.readthedocs.io/en/latest/) – Mouse and keyboard control
- [NumPy](https://numpy.org/) – Mathematical calculations

  ## ❓ Why Use Both PyAutoGUI and pynput?

This project uses **both libraries** because they complement each other’s strengths and cover their limitations.

### PyAutoGUI

**Advantages:**  
- Simple, easy-to-use API for mouse and keyboard automation.  
- Built-in screenshot functionality.  
- Works cross-platform and widely supported.  

**Limitations:**  
- Not optimized for very fast, real-time continuous control.  
- Limited ability to hold mouse buttons down (clicks are usually quick press-release).  
- Can be slower or less smooth in rapid cursor movements.

### pynput

**Advantages:**  
- Provides low-level, fine-grained control over mouse and keyboard input.  
- Supports holding and releasing mouse buttons, ideal for drag and hold gestures.  
- Better suited for real-time, smooth cursor movement and gesture control.  
- Can listen to input events (useful for extensions).

**Limitations:**  
- More complex API compared to PyAutoGUI.  
- Does not have built-in screenshot functionality.  
- Slightly less beginner-friendly.

---

### Combining Both

Using PyAutoGUI and pynput together allows this project to:

- Use PyAutoGUI’s simplicity for quick clicks and screenshots.  
- Use pynput’s precision for smooth cursor movement and hold-based gestures.  

This combination ensures **responsive, accurate, and feature-rich hand gesture control** for the virtual mouse.

---

## 🛠️ Libraries and Tech Stack Used

### Programming Language
- **Python 3.8+** – Main language used for development.

### Computer Vision & Hand Tracking
- **OpenCV** – For capturing webcam video frames and image processing.
- **MediaPipe Hands** – Google's framework for real-time hand landmark detection and tracking.

### Mouse and Keyboard Control
- **PyAutoGUI** – High-level mouse and keyboard automation (clicks, double clicks, screenshots).
- **pynput** – Low-level, precise mouse and keyboard control for smooth cursor movement and button hold actions.

### Mathematical and Utility Libraries
- **NumPy** – For numerical computations like calculating distances and angles between hand landmarks.

### Optional / Others
- (Add any other libraries if you use them, e.g., `random` for randomness, `time` for delays.)

---

This tech stack enables the project to capture live video, detect and interpret hand gestures, and translate them into accurate and responsive mouse control commands.





---


## 📦 Requirements

Install the dependencies before running the project:

```bash
pip install opencv-python mediapipe pyautogui numpy
