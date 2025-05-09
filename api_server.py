from flask import Flask, request, jsonify
from src.module_loader import run_module
from src.model_router import call_model

app = Flask(__name__)

@app.route("/quasar/text", methods=["POST"])
def handle_text():
    user_input = request.json.get("message", "")
    prompt = [
        {"role": "system", "content": "You are Quasar, a self-improving dev agent. Respond with 'run <module>' only."},
        {"role": "user", "content": user_input}
    ]
    result = call_model(prompt).strip().lower()
    if result.startswith("run "):
        module = result.split(" ")[1]
        run_module(module)
        return jsonify({"status": "executed", "module": module})
    return jsonify({"status": "ignored", "response": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
