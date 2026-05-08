from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Bias detection keywords
bias_keywords = {
    "confirmation bias": ["only believe", "ignore other", "biased toward"],
    "anchoring bias": ["first impression", "initial number"],
    "overgeneralization": ["always", "never", "everyone"],
    "emotional bias": ["feel like", "hate", "love"],
}

# Home route (opens frontend)
@app.route("/")
def home():
    return render_template("index.html")

# API route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "").lower()
    
    detected = []
    for bias, keywords in bias_keywords.items():
        for word in keywords:
            if word in text:
                detected.append(bias)
                break

    return jsonify({
        "input": text,
        "biases": detected if detected else ["No bias detected"]
    })

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
