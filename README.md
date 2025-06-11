# 💊 PharmAI – Intelligent Tablet Name Recognition & Row Placement System

PharmAI is an OCR-powered system designed to automate the identification and placement of pharmaceutical tablets using image processing, machine learning, and voice feedback. This project aims to enhance pharmacy workflows by reducing manual sorting errors and improving efficiency through AI-driven automation.

---

## 📌 Features

- 📷 **Tablet Image Upload** – Supports image input via camera or file upload.
- 🧠 **OCR-Based Name Recognition** – Uses EasyOCR for high-accuracy text extraction from packaging.
- 🗂️ **Automated Row Placement** – Assigns tablets to rows based on the first letter of the name.
- 🔊 **Voice Feedback** – Announces row placement using Text-to-Speech (TTS) via JavaScript Web Speech API.
- 🌐 **User-Friendly Interface** – Built with Flask (backend) and HTML/CSS/JS (frontend).
- 📈 **High Accuracy** – Achieves 97% OCR accuracy and 99.68% row placement accuracy.

---

## 🧪 Tech Stack

| Component | Technology |
|----------|-------------|
| Language | Python 3.10 |
| OCR | [EasyOCR](https://github.com/JaidedAI/EasyOCR) |
| Voice | JavaScript Web Speech API |
| UI | HTML, CSS, JavaScript |
| Backend | Flask |
| Image Processing | OpenCV, NumPy |
| Text-to-Speech | pyttsx3 (Python) & Web Speech API (JS) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Installation

```bash
git clone https://github.com/Tejas-Noojile/PharmAI-Intelligent_Tablet_Name_Recognition.git
cd PharmAI-Intelligent_Tablet_Name_Recognition
pip install -r requirements.txt

#run locally
python app.py


| Model       | Accuracy | Inference Time | Size     |
| ----------- | -------- | -------------- | -------- |
| Custom CNN  | 68%      | \~25 ms        | \~5 MB   |
| MobileNetV2 | 70%      | \~30 ms        | \~14 MB  |
| VGG16       | 81%      | \~120 ms       | \~528 MB |
| **EasyOCR** | **97%**  | \~45 ms        | \~30 MB  |
