# 🎧 Phishing Call Fraud Detection Application

A Python-based fraud detection application that analyzes WAV audio call recordings to identify potential phishing attempts.

This project provides:
- 🌐 Web Interface (Flask-based)
- 💻 Command-Line Interface (CLI)
- 🔐 OAuth2 Authentication
- 📡 Integration with Fraud Detection API

---

## 📌 Project Overview

This application allows users to upload WAV call recordings and detect phishing attempts using an external fraud detection API.

Workflow:
1. Authenticate using OAuth2 Client Credentials flow.
2. Upload the audio file along with metadata.
3. Receive fraud analysis results in JSON format.
4. Display results in the web app or CLI.

---

## 🏗️ Project Structure

```
├── app.py              # Flask web application
├── fraud.py            # Core API logic + CLI support
├── templates/
│   └── index.html      # Web form UI
├── static/
│   ├── style.css       # Styling
│   └── script.js       # Frontend JS
├── README.md
```

---

## ⚙️ Key Components

### 1️⃣ Web Application (app.py)

- Built using Flask
- Accepts:
  - Client ID
  - Client Secret
  - WAV file upload
  - Date/Time
  - Sender phone number
  - Receiver phone number
  - Locale
- Displays fraud detection results in JSON format

---

### 2️⃣ Core Logic (fraud.py)

Handles:
- OAuth2 authentication
- Bearer token generation
- Audio file upload
- API communication
- Error handling
- CLI-based execution

---

## 🔐 Authentication

OAuth2 Client Credentials Flow is used.

Token Endpoint:
```
POST https://epaycop.xpectro-solutions.com/o/token/
```

Returns:
```
Bearer Access Token
```

---

## 📡 Fraud Detection API

Endpoint:
```
POST https://epaycop.xpectro-solutions.com/api/fraud-detection/call/phishing
```

Request includes:
- WAV audio file
- Date/time metadata
- Sender number
- Receiver number
- Locale

Example Response:
```json
{
  "category": "Phishing",
  "confidence": 0.92,
  "reason": "Caller impersonated bank official and requested OTP"
}
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install flask requests
```

---

## ▶️ Running the Application

### 🌐 Run Web Application

```bash
python app.py
```

Open:
```
http://127.0.0.1:5000
```

---

### 💻 Run CLI Version

Example:

```bash
python fraud.py --client_id YOUR_ID --client_secret YOUR_SECRET --file sample.wav --sender 1234567890 --receiver 9876543210 --locale en-IN
```

---

## 🛡️ Error Handling

The application handles:
- Invalid credentials
- Token generation failure
- API upload errors
- Missing file inputs
- Invalid file formats

---

## 📦 Dependencies

- Python 3.x
- Flask
- requests

Install using:

```bash
pip install flask requests
```

---

## 📄 Output Format

Results are returned in JSON format:

```json
{
  "category": "Phishing / Legitimate",
  "confidence": 0.xx,
  "reason": "Explanation of detection"
}
```

---

## 📌 Use Cases

- Financial institutions
- Telecom fraud monitoring
- Security analysis teams
- Compliance departments
- Call auditing systems

---

## ⚠️ Notes

- WAV format is required.
- Valid API credentials are mandatory.
- Internet connection is required.
- Ensure metadata accuracy for better detection results.

---

## 🧠 Future Enhancements

- Real-time streaming support
- Analytics dashboard
- Database logging
- Multi-language support
- Docker support
- JWT-based session management

---

## 📜 License

Specify your license here (MIT, Apache 2.0, etc.)

---

## 👨‍💻 Author

Your Name  
GitHub: https://github.com/your-username
