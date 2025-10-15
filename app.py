from flask import Flask, request, jsonify
from includes.ollama_client import OllamaClient
from includes.redis import Cache

app = Flask(__name__)

@app.route("/api/v1/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    cached = Cache.get(prompt)
    if cached:
        return jsonify({"cached": True, "response": cached})

    try:
        response = OllamaClient.chat(prompt)
        Cache.set(prompt, response)
        return jsonify({"cached": False, "response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)