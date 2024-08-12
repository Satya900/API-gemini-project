from flask import Flask, request, jsonify, send_from_directory
import os
import google.generativeai as genai

app = Flask(__name__)


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if GOOGLE_API_KEY is None:
    raise ValueError("API key not found in environment variables")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/generate-story', methods=['POST'])
def generate_story():
    data = request.json
    prompt = data.get('prompt', '')
    response = model.generate_content(prompt)
    return jsonify({'story': response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
