# Weather App 🌦️

A simple Flask-based weather application that fetches live weather data and displays winter facts. 

## Features
- Get current weather for any city and country.
- Fun winter facts displayed alongside weather information.
- Containerized with Docker for portability.
- CI/CD pipeline for seamless deployment.

---

## Requirements

- Python 3.11
- Flask
- OpenWeatherMap API key
- Docker (for containerization)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yuvalbenar/weather-app.git
cd weather-app

### 2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Add OpenWeatherMap API Key
Update the app.py file:

python
Copy code
API_KEY = "your_openweather_api_key_here"
4. Run the Application
bash
Copy code
python app.py
Access the application at http://127.0.0.1:5000.

Using Docker 🐳
1. Build the Docker Image
bash
Copy code
docker build -t weathertraining-app .
2. Run the Docker Container
bash
Copy code
docker run -p 5000:5000 weathertraining-app
Access the application at http://localhost:5000.


