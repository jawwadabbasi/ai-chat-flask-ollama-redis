# AI Chat Flask Ollama Redis

A lightweight **local AI chat API** built with **Flask**, **Ollama**, and **Redis** — enabling you to run and cache **LLM (Large Language Model)** responses locally without relying on external APIs like OpenAI.

---

## 🚀 Features
- ⚡ **Flask-based REST API** for chatting with an LLM
- 🧩 **Ollama integration** for running models locally (e.g. Llama 3, Mistral, Gemma)
- 🧠 **Redis caching** to store and reuse recent responses
- 🔁 **Stateless or contextual chat** options
- 🪶 Lightweight and easy to deploy anywhere

---

## 🛠️ Tech Stack
- **Flask** – web server and routing
- **Ollama** – local model inference engine
- **Redis** – caching for fast repeated queries
- **Python 3.10+**

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/jawwadabbasi/ai-chat-flask-ollama-redis.git
cd ai-chat-flask-ollama-redis
```

### 2️⃣ Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start Redis
If Redis is installed via Homebrew:
```bash
brew services start redis
```

### 5️⃣ Run Ollama
Make sure you have [Ollama](https://ollama.com/) installed and a model pulled:
```bash
ollama pull llama3
```

### 6️⃣ Run the Flask App
```bash
python3 app.py
```

---

## 🧩 API Endpoints

### `POST /api/v1/chat`
Send a message to the local model and receive a generated response.

**Request:**
```json
{
  "prompt": "Explain einstein's theory of relativity in simple terms"
}
```

**Response:**
```json
{
  "cached": false,
  "response": "Albert Einstein developed the Theory of Relativity which is actually two theories: Special and General. Let me explain them simply for you.\n\nSpecial Relativity, published by Einstein in 1905, basically tells us about space and time when we are not dealing with things that have a lot of gravity (like stars or planets). Imagine if everyone saw the world differently based on how fast they were moving – this is what Special Relativity says. There's also an interesting thing called \"time dilation,\" which means two clocks can run at different speeds relative to each other when you move them really fast (close to light speed).\n\nGeneral Relativity, published later in 1915, extends these ideas and tells us about space and time near very massive objects. Think of gravity as a sort of \"dent\" or warp in the fabric of our universe caused by big things like stars and planets – this is General Relativity's idea using what we can now understand to be spacetime being curved around mass.\n\nA famous result from these theories was that Einstein predicted light could bend because it moves through space which gets bent, something called gravitational lensing which has been observed with stars and galaxies far away in the universe when their light passes close by other large objects on its way to Earth."
}
```

---

## 💾 Redis Caching
Responses are automatically cached using the prompt as the key:
- The next time you send the same prompt, it’ll return instantly from Redis.
- To clear cache, run:
```bash
redis-cli FLUSHALL
```

---

## 🧠 Example Curl Command
```bash
curl -X POST http://localhost:8000/api/v1/chat \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Tell me something about the moon"}'
```

---

## 🌐 Example Use Cases
- Build your **own ChatGPT-like API** without internet dependency
- Integrate into a **local research assistant**
- Cache responses for **offline chatbots or CLI tools**
- Extend with **RAG (Retrieval-Augmented Generation)** later

---

## 📁 Project Structure
```
ai-chat-flask-ollama-redis/
│
├── app.py                 # Main Flask app
├── includes/
│   ├── redis.py           # Redis cache handler
│   └── ollama_client.py   # Ollama integration logic
├── requirements.txt
└── README.md
```

---

## 🏁 License
This project is licensed under the **MIT License** — free for personal and commercial use.
"""