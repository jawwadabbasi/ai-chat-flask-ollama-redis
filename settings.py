import os

# Choose which model to run via Ollama
MODEL_NAME = os.getenv("MODEL_NAME", "phi3")

# Redis configuration (optional)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))