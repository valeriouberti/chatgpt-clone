# 🤖 ChatGPT Clone with Streamlit and Docker Compose

## 📚 Overview

This project is a **ChatGPT Clone** built using **Streamlit** and integrated with **OpenAI's GPT API**. It provides an interactive chat interface where users can communicate with the GPT model seamlessly. The application is containerized using **Docker** and managed via **Docker Compose** for easy deployment.

---

## 🚀 Features

- **Interactive Chat Interface:** User-friendly Streamlit UI.
- **Real-Time Communication:** Responses are fetched from OpenAI's GPT model.
- **Environment Variables:** API keys are securely managed via `.env`.
- **Dockerized Deployment:** Simplified deployment using Docker and Docker Compose.
- **Hot Reloading:** Real-time updates during development.

---

## 🛠️ Tech Stack

- **Backend:** OpenAI GPT API
- **Frontend:** Streamlit
- **Containerization:** Docker, Docker Compose
- **Environment Management:** Python-dotenv
- **Language:** Python 3.13

---

## 📂 Project Structure

```
chatgpt_clone/
├── app.py             # Main Streamlit app
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose configuration
├── .env              # Environment variables
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/valeriouberti/chatgpt_clone.git
cd chatgpt_clone
```

### 2. Add OpenAI API Key

Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
MODEL_ID=gpt-4o-mini
```

### 3. Build and Start the Application

```bash
docker-compose up -d --build
```

### 4. Access the App

Open your browser and navigate to:

```
http://localhost:8501
```

### 5. Stop the Application

```bash
docker-compose down
```

---

## 🧠 Environment Variables

The application uses the following environment variable:

```env
OPENAI_API_KEY=your_openai_api_key_here
MODEL_ID=gpt-4o-mini
```

Ensure this key is valid to interact with the OpenAI API.

---

## ⚙️ Development

- Modify `app.py` for changes.
- Hot-reloading is enabled via Docker volume mapping.
- Restart the container if necessary:

```bash
docker-compose restart
```

---

## 🛡️ Security

- Do not hard-code your API keys.
- Use `.env` to manage sensitive information.
- Avoid exposing `.env` in public repositories.

---

## 🧠 Future Improvements

- **Persistent Chat History:** Store conversation logs in a database.
- **Use other GPT Models:** Experiment with different GPT models.

---

## 🤝 Contributing

Feel free to fork this project, make improvements, and submit pull requests. Ensure you follow best practices.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

- **Author:** Valerio Uberti
- **Email:** valerio.uberti23@gmail.com
- **GitHub:** [yourusername](https://github.com/valeriouberti)

---

Happy Chatting! 🚀🤖✨
