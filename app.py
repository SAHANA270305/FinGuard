from flask import Flask, request, jsonify
import os
from fraud_model import check_for_anomalies

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return "FinGuard backend is running!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file found'})
    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return jsonify({'message': 'File uploaded successfully', 'filepath': filepath})


@app.route('/analyze', methods=['POST'])
def analyze_data():
    data = request.get_json()
    result = check_for_anomalies(data)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

