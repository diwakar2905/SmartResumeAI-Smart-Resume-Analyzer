# 🧠 Smart Resume Analyzer - Production Ready

A powerful, AI-driven resume analysis tool that provides comprehensive feedback and scoring for job seekers and recruiters.

## ✨ Features

### Core Features
- **📄 Multi-Format Support**: PDF, DOCX, and DOC files
- **🤖 AI-Powered Analysis**: Advanced NLP using spaCy for text extraction and analysis
- **📊 Comprehensive Scoring**: Industry-standard resume scoring algorithm
- **💡 Actionable Feedback**: Detailed recommendations for improvement
- **🔍 Skill Detection**: Automatic identification and categorization of technical skills
- **📋 Section Analysis**: Detection of resume sections (Experience, Education, Skills, etc.)
- **📱 Modern UI**: Responsive, professional web interface

### Technical Features
- **🚀 Production Ready**: Gunicorn, Nginx, and systemd service configuration
- **🔒 Security**: File validation, secure uploads, and CORS protection
- **📈 Logging**: Comprehensive logging with rotation
- **⚡ Performance**: Optimized for high-throughput processing
- **🛠️ Monitoring**: Health checks and API statistics
- **🧪 Testing**: Comprehensive test suite and validation

## 🛠️ Technology Stack

### Backend
- **Flask 2.3.3**: Web framework
- **spaCy 3.7.2**: Natural Language Processing
- **PyMuPDF 1.23.8**: PDF text extraction
- **python-docx 0.8.11**: DOCX file processing
- **Gunicorn 21.2.0**: Production WSGI server
- **scikit-learn 1.3.0**: Machine learning utilities

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **JavaScript ES6+**: Interactive functionality
- **Font Awesome**: Professional icons

### Infrastructure
- **Nginx**: Reverse proxy and static file serving
- **systemd**: Service management
- **Python 3.8+**: Runtime environment

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd smart-resume-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install spaCy model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open `http://127.0.0.1:5001` in your browser
   - Or open `index.html` directly

## 🏭 Production Deployment

### Automated Setup
Run the deployment script for automatic production setup:
```bash
python deploy.py
```

### Manual Setup

1. **Environment Configuration**
   ```bash
   # Create environment file
   cp .env.example .env
   # Edit .env with your production settings
   ```

2. **Install Production Dependencies**
   ```bash
   pip install gunicorn python-dotenv
   ```

3. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Configure Gunicorn**
   ```bash
   # Use the provided gunicorn.conf.py
   gunicorn --config gunicorn.conf.py app:app
   ```

5. **Set up systemd Service**
   ```bash
   sudo cp smart-resume-analyzer.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable smart-resume-analyzer
   sudo systemctl start smart-resume-analyzer
   ```

6. **Configure Nginx**
   ```bash
   sudo cp nginx.conf /etc/nginx/sites-available/smart-resume-analyzer
   sudo ln -s /etc/nginx/sites-available/smart-resume-analyzer /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl reload nginx
   ```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | `your-secret-key-change-in-production` |
| `DEBUG` | Debug mode | `False` |
| `HOST` | Server host | `127.0.0.1` |
| `PORT` | Server port | `5001` |
| `LOG_LEVEL` | Logging level | `INFO` |
| `CORS_ORIGINS` | Allowed origins | `*` |

## 📊 API Documentation

### Endpoints

#### `GET /`
API information and documentation.

#### `POST /analyze`
Upload and analyze a resume file.

**Request:**
- Content-Type: `multipart/form-data`
- Body: `resume` file (PDF, DOCX, or DOC)

**Response:**
```json
{
  "basic_info": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1-555-123-4567"
  },
  "skills": {
    "Programming Languages": ["Python", "JavaScript"],
    "Web & Frontend": ["React", "HTML", "CSS"]
  },
  "score": 85,
  "feedback": [
    "Great technical skills!",
    "Consider adding more quantifiable achievements"
  ],
  "sections_found": {
    "experience": true,
    "education": true,
    "skills": true
  },
  "analysis_metadata": {
    "file_name": "resume.pdf",
    "processing_time": 2.5,
    "timestamp": "2024-01-01T12:00:00Z"
  }
}
```

#### `GET /health`
Health check endpoint.

#### `GET /test`
Test endpoint for connectivity.

#### `GET /stats`
API statistics and system information.

## 🧪 Testing

### Run Tests
```bash
# Basic functionality test
python test_pdf.py

# Frontend test
open test_frontend.html

# Quick test
open quick_test.html
```

### Test with Sample Data
```bash
python test_pdf.py sample_resume.pdf
```

## 🔧 Configuration

### Customizing Skills
Edit `skills.json` to add or modify skill categories:
```json
{
  "Programming Languages": ["Python", "JavaScript", "Java"],
  "New Category": ["Skill 1", "Skill 2"]
}
```

### Adjusting Scoring Weights
Modify `utils/scoring.py` to change section weights:
```python
WEIGHTS = {
    'experience': 30,
    'education': 20,
    'skills': 25,
    'projects': 15,
    'certifications': 10
}
```

### Customizing Feedback
Edit `utils/feedback.py` to modify feedback messages and tips.

## 📁 Project Structure

```
smart-resume-analyzer/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── deploy.py             # Production deployment script
├── requirements.txt      # Python dependencies
├── index.html           # Main frontend interface
├── README.md            # This file
├── .env                 # Environment variables
├── gunicorn.conf.py     # Gunicorn configuration
├── nginx.conf           # Nginx configuration
├── smart-resume-analyzer.service  # systemd service
├── parser/              # Document parsing modules
│   └── resume_parser.py
├── utils/               # Analysis utilities
│   ├── skill_classifier.py
│   ├── section_extractor.py
│   ├── scoring.py
│   └── feedback.py
├── temp_uploads/        # Temporary file storage
├── logs/               # Application logs
└── static/             # Static assets
```

## 🔒 Security Considerations

- **File Validation**: All uploaded files are validated for type and size
- **Secure Filenames**: Files are saved with timestamped, sanitized names
- **Automatic Cleanup**: Temporary files are automatically deleted
- **CORS Protection**: Configurable cross-origin resource sharing
- **Input Sanitization**: All user inputs are properly sanitized
- **Error Handling**: Comprehensive error handling without information leakage

## 📈 Performance Optimization

- **File Size Limits**: 16MB maximum file size
- **Processing Timeout**: 120-second timeout for analysis
- **Memory Management**: Automatic cleanup of temporary files
- **Caching**: Static file caching with Nginx
- **Load Balancing**: Gunicorn worker processes for concurrent requests

## 🐛 Troubleshooting

### Common Issues

1. **spaCy Model Not Found**
   ```bash
   python -m spacy download en_core_web_sm
   ```

2. **Port Already in Use**
   ```bash
   # Change port in .env file or kill existing process
   lsof -ti:5001 | xargs kill -9
   ```

3. **File Upload Fails**
   - Check file size (max 16MB)
   - Verify file format (PDF, DOCX, DOC)
   - Check server logs: `tail -f logs/app.log`

4. **Results Not Displaying**
   - Check browser console (F12)
   - Verify server is running: `curl http://127.0.0.1:5001/health`
   - Check CORS configuration

### Logs
- **Application Logs**: `logs/app.log`
- **Access Logs**: `logs/access.log`
- **Error Logs**: `logs/error.log`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **spaCy**: Natural language processing capabilities
- **PyMuPDF**: PDF text extraction
- **Flask**: Web framework
- **Font Awesome**: Icons
- **Community**: Contributors and feedback

## 📞 Support

For support and questions:
- Check the troubleshooting guide
- Review the API documentation
- Open an issue on GitHub
- Check the logs for detailed error information

---

**Smart Resume Analyzer v2.0.0** - Ready for production deployment! 🚀 