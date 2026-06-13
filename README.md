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

## 👨‍💻 Author

**S. Ganesh**
Artificial Intelligence & Machine Learning

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, please give it a star on GitHub.
