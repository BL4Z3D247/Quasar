from flask import Flask, request
import openai
import os
import requests

app = Flask(__name__)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    try:
        update = request.get_json(force=True)
        print("Received update:", update)
        message = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}]
        )
        reply = response.choices[0].message["content"]
    except Exception as e:
        reply = f"Error from Quasar: {str(e)}"
        print(reply)
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={
        "chat_id": chat_id,
        "text": reply
    })
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443)
