# Webcam Alert App Using Python

This project uses OpenCV and a webcam to detect motion or faces. When motion is detected, it captures an image and sends an email alert with the image attached.

## 📌 Features
- Motion detection using OpenCV
- Captures and stores images when motion is detected
- Sends email alerts with captured image
- Automatically deletes stored images after sending
- Multithreaded to avoid lag in video stream

## 🛠️ Requirements

- Python 3.10 or later
- Webcam (internal or external)
- Internet connection (for email functionality)

## 🧪 Libraries Used
- OpenCV (`opencv-python`)
- `smtplib`, `email`, `glob`, `os`, `time`, `threading` (standard libraries)

## 🔧 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/webcam-alert-app.git
    cd webcam-alert-app
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

1. Update your `emailing.py` file with sender credentials and configuration.
2. Run the application:
    ```bash
    python main.py
    ```
3. Press `q` to quit the application.

## 📂 Project Structure

