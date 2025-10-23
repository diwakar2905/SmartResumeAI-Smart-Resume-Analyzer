# 🧠 Smart Resume Analyzer

**A powerful, AI-driven resume analysis tool to help job seekers optimize their resumes and stand out to recruiters.**

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://web-production-52705.up.railway.app/)

---

## 📜 Table of Contents

- [✨ Features](#-features)
- [⚙️ How It Works](#️-how-it-works)
- [🛠️ Technology Stack](#️-technology-stack)
- [🚀 Getting Started](#-getting-started)
- [☁️ Deployment](#️-deployment)
- [🔌 API Endpoints](#-api-endpoints)
- [🔧 Configuration](#-configuration)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

- **📄 Multi-Format Support**: Analyzes resumes in both **PDF** and **DOCX** formats.
- **🤖 AI-Powered Analysis**: Uses **spaCy** for advanced Natural Language Processing (NLP) to extract and analyze text.
- **📊 Comprehensive Scoring**: Provides a score based on industry-standard metrics.
- **💡 Actionable Feedback**: Offers detailed, structured recommendations for improvement.
- **🎯 Skill Detection**: Automatically identifies and categorizes technical and soft skills.
- **📋 Section Analysis**: Detects key resume sections like *Experience*, *Education*, and *Skills*.
- **📱 Modern & Responsive UI**: A clean and professional multi-page web interface.
- **📜 PDF Report Generation**: Allows users to download a detailed analysis report in PDF format.

---

## ⚙️ How It Works

1.  **Upload**: The user uploads their resume through the web interface.
2.  **Parsing**: The system extracts text from the uploaded file.
3.  **Analysis**: The extracted text is processed to:
    - Identify skills and categorize them.
    - Detect the presence of important sections.
    - Score the resume based on various factors.
4.  **Feedback Generation**: Based on the analysis, personalized feedback and suggestions are generated.
5.  **Display Results**: The score, feedback, and identified skills are presented to the user on the output page.

---

## 🛠️ Technology Stack

- **Backend**: **Flask**, **spaCy**, **PyMuPDF**
- **Frontend**: **HTML5**, **CSS3**, **JavaScript**
- **Deployment**: **Gunicorn**, **Nginx**

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd smart-resume-analyzer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download spaCy model:**
    ```bash
    python -m spacy download en_core_web_sm
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  Open your browser and navigate to `http://127.0.0.1:5001`.

---

## ☁️ Deployment

This project is configured for production deployment. For detailed instructions on deploying with Gunicorn and Nginx, or on platforms like Render and Vercel, please refer to the `README_PRODUCTION.md` file.

---

## 🔌 API Endpoints

| Method | Endpoint              | Description                               |
| :----- | :-------------------- | :---------------------------------------- |
| `GET`  | `/`                   | Serves the main application page.         |
| `POST` | `/analyze`            | Analyzes the uploaded resume file.        |
| `POST` | `/api/generate-report`| Generates a PDF report of the analysis.   |
| `GET`  | `/health`             | Health check endpoint.                    |

---

## 🔧 Configuration

- **Skills**: To add or modify skill categories, edit the `data/skills.json` file.
- **Scoring**: To adjust the weights for resume scoring, modify the `WEIGHTS` dictionary in `utils/scoring.py`.
- **Feedback**: To change the feedback messages, edit the `utils/feedback.py` file.

---

## 📁 Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt      # Python dependencies
├── static/                # Static assets (CSS, JS, images)
├── templates/             # HTML templates
├── parser/                # Resume parsing logic
├── utils/                 # Analysis and utility scripts
├── data/                  # Data files (e.g., skills.json)
└── README.md              # This file
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request.

1.  Fork the repository.
2.  Create a new feature branch.
3.  Make your changes.
4.  Submit a pull request with a clear description of your changes.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.