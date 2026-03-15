from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyAEmGucsXb4fXXKDIjW4I1PbIwOEUD8AaA")

# Use a supported model name for generate_content. "gemini-2.5-flash" is currently available.
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        # Log the error and return a JSON error response.
        app.logger.exception("Error generating response")
        return jsonify({"error": "Failed to generate response", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)