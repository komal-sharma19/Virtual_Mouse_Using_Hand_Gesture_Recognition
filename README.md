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
<p align="center">
  <img src="https://github.com/komal-sharma19/Virtual_Mouse_Using_Hand_Gesture_Recognition/blob/main/Screenshot%202025-08-08%20152311.png?raw=true" width="600" />
</p>

---

## 🛠️ Technologies Used

- [Python 3.8+](https://www.python.org/)
- [OpenCV](https://opencv.org/) – Video capture and image processing
- [MediaPipe](https://developers.google.com/mediapipe) – Hand landmark detection
- [PyAutoGUI](https://pyautogui.readthedocs.io/) – Mouse and keyboard automation
- [NumPy](https://numpy.org/) – Mathematical calculations

---

## 📦 Requirements

Install the dependencies before running the project:

```bash
pip install opencv-python mediapipe pyautogui numpy
