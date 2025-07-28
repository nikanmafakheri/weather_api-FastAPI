# 🌤 Weather API

🚧 **This project is still under active development.**  
Features, endpoints, and documentation will be expanded over time.

A **FastAPI-based Weather API** that fetches weather data, stores it in PostgreSQL, and uses **Redis caching** for better performance.  

---

## 🚀 Features

- ✅ Fetch real-time weather data from an external API  
- ✅ Cache responses in Redis to reduce API calls  
- ✅ Store weather history in PostgreSQL  
- ✅ Built with **FastAPI** for high performance  
- ✅ Docker support for easy deployment  

---

## 🛠 Tech Stack

- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **Cache:** Redis  
- **HTTP Client:** `httpx` / `requests` (depending on implementation)  
- **Deployment:** Docker & Docker Compose  

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository

git clone https://github.com/nikanmafakheri/E-CommerceAPI.git
cd E-CommerceAPI
2️⃣ Environment Variables
Create a .env file with:

ini
Copy
Edit
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=weather_db
REDIS_HOST=redis
REDIS_PORT=6379
OPENWEATHER_API_KEY=your_api_key_here
3️⃣ Run with Docker
bash
Copy
Edit
docker-compose up --build
The API will be available at:
👉 http://localhost:8000

📡 Example Endpoints
Method	Endpoint	Description
GET	/weather/{city}	Get current weather for a city
GET	/history/{city}	Get stored weather history

Example:

bash
Copy
Edit
curl http://localhost:8000/weather/Tehran
🔮 Roadmap / Future Improvements
🔐 Add authentication (JWT)

📈 Add weather statistics (min/max/avg)

📄 Add Swagger/ReDoc API docs

🌍 Support multiple external weather providers

🤝 Contributing
Since this project is still under development, feel free to fork it and submit pull requests.

📄 License
This project is licensed under the MIT License.

👤 Author
Nikan Mafakheri
🔗 GitHub
