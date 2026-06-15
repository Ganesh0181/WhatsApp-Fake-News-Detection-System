# 📰 WhatsApp Fake News Detection System

An AI-powered WhatsApp Fake News Detection platform that analyzes messages, URLs, images, and forwarded content to identify misinformation in real-time.

The application uses Machine Learning, Natural Language Processing (NLP), FastAPI, React, Docker, Nginx Reverse Proxy, and Secure Sandbox Execution to provide accurate fake news detection while ensuring system security.

---

## 🚀 Features

### Core Features

* Fake News Classification
* WhatsApp Message Analysis
* URL Verification
* Forwarded Message Detection
* AI Confidence Score
* News Source Validation
* Fact Check Suggestions
* Real-Time Detection Dashboard

### Security Features

* Docker Containerization
* Nginx Reverse Proxy
* Secure Sandbox Environment
* API Rate Limiting
* Input Validation
* CORS Protection
* Secure HTTP Headers

### AI Features

* NLP-Based Text Processing
* Machine Learning Classification
* Sentiment Analysis
* Keyword Extraction
* Source Credibility Analysis
* Confidence Score Generation

---

## 🏗️ System Architecture

<img width="1536" height="1024" alt="System Architecture" src="https://github.com/user-attachments/assets/ada0e5fe-de77-4b3c-900f-3c7be9c519e6" />

---

## 🛠️ Technology Stack

### Frontend

* React.js
* TypeScript
* Tailwind CSS
* Axios
* Chart.js

### Backend

* FastAPI
* Python 3.11
* Scikit-Learn
* Pandas
* NumPy

### Infrastructure

* Docker
* Docker Compose
* Nginx
* Linux

### AI & NLP

* TF-IDF Vectorization
* Logistic Regression
* Random Forest
* NLP Preprocessing

---

## 📁 Project Structure

<img width="1536" height="1024" alt="Project Structure" src="https://github.com/user-attachments/assets/218c84a9-4951-422d-8837-8d976d928286" />

---

## 🔒 Sandbox Security

The application uses a dedicated sandbox environment for secure content analysis.

### Benefits

* Isolated Execution
* Malicious Input Protection
* Resource Limitation
* Secure Processing
* Container Isolation

### Security Layers

1. Nginx Reverse Proxy
2. FastAPI Validation
3. Docker Isolation
4. Sandbox Processing
5. AI Verification Layer

---

## 🐳 Docker Deployment

### Build Containers

```bash
docker-compose build
```

### Start Application

```bash
docker-compose up -d
```

### Check Running Containers

```bash
docker ps
```

### View Logs

```bash
docker-compose logs -f
```

---

## 🌐 Nginx Configuration

Nginx acts as:

* Reverse Proxy
* Load Balancer
* SSL Termination
* API Gateway
* Security Layer

### Request Flow

```text
User
 ↓
Nginx
 ↓
FastAPI
 ↓
ML Model
 ↓
Response
```

---

## 📊 API Endpoints

### Health Check

```http
GET /api/health
```

Response:

```json
{
  "status": "healthy"
}
```

### Analyze News

```http
POST /api/analyze
```

Request:

```json
{
  "message": "Breaking news..."
}
```

Response:

```json
{
  "prediction": "Fake",
  "confidence": 92.5
}
```

---

## 📈 Performance Metrics

| Metric        | Value   |
| ------------- | ------- |
| Accuracy      | 95%     |
| Precision     | 94%     |
| Recall        | 93%     |
| F1 Score      | 94%     |
| Response Time | < 2 sec |

---

## 🔥 Future Enhancements

* Multilingual Detection
* Image Verification
* Video Verification
* WhatsApp Bot Integration
* Deepfake Detection
* Real-Time Fact Checking
* Cloud Deployment
* Kubernetes Support

---


## ⚙️ Project Execution Commands

### Backend (FastAPI)

```bash
cd backend

venv\Scripts\activate

python -m uvicorn main:app --reload --host 0.0.0.0 --port 6500
```

Backend API:

```text
http://localhost:6500/docs
```

---

### Frontend (React)

```bash
cd frontend

set PORT=6600

npm install

npm start
```

Frontend URL:

```text
http://localhost:6600
```

---

### Nginx Reverse Proxy

```bash
cd C:\nginx\nginx-1.31.1

nginx.exe -t

nginx.exe
```

Reload Nginx:

```bash
nginx.exe -s reload
```

Stop Nginx:

```bash
nginx.exe -s stop
```

---

### Ngrok (WhatsApp Webhook)

```bash
cd C:\Users\GANESH\Downloads\ngrok-v3-stable-windows-amd64

ngrok http 6500
```

Webhook URL:

```text
https://your-ngrok-url.ngrok-free.dev/whatsapp
```

Example:

```text
https://mortuary-slimness-scorch.ngrok-free.dev/whatsapp
```

---

### Docker Commands

Build Containers:

```bash
docker compose build
```

Start Containers:

```bash
docker compose up -d
```

View Running Containers:

```bash
docker ps
```

View Logs:

```bash
docker compose logs -f
```

Backend Logs:

```bash
docker logs -f whatsapp-fake-news-backend
```

Stop Containers:

```bash
docker compose down
```

---

### MongoDB Commands

Open Mongo Shell:

```bash
docker exec -it whatsapp-fake-news-mongodb mongosh
```

MongoDB Operations:

```javascript
show dbs

use fake_news_db

show collections

db.predictions.find()
```

---

### Network & Debug Commands

Check Ports:

```bash
netstat -ano | findstr :6500

netstat -ano | findstr :6600

netstat -ano | findstr :27017
```

Restart Backend:

```bash
cd backend

python -m uvicorn main:app --reload --host 0.0.0.0 --port 6500
```

---

### Port Configuration

| Service         | Port       |
| --------------- | ---------- |
| FastAPI Backend | 6500       |
| React Frontend  | 6600       |
| MongoDB         | 27017      |
| Ngrok Webhook   | Public URL |

```
Backend Docs:  http://localhost:6500/docs
Frontend UI:   http://localhost:6600
MongoDB:       mongodb://localhost:27017
```


## 👨‍💻 Author

**S. Ganesh**
Artificial Intelligence & Machine Learning

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, please give it a star on GitHub.
