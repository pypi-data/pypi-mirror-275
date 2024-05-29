from flask import Flask, render_template, send_from_directory, request, jsonify
import requests
from sys import platform

app = Flask(__name__)

static_dir = ""
template_dir = ""

if platform == "linux" or platform == "linux2":
    static_dir = "app/static"
    template_dir = "app/templates"
elif platform == "win32":
    static_dir = "Backend/app/static"
    template_dir = "Backend/app/templates"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(static_dir, filename)


@app.route('/query/', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get('question')
    document = data.get('document')
    ml_service_url = "http://localhost:8001/query/"
    response = requests.post(ml_service_url, json={"question": question, "document": document})
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
