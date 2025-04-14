from flask import Flask, render_template, request, jsonify
import easyocr
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

reader = easyocr.Reader(['en'], gpu=False)

def get_tablet_row(image_path):
    results = reader.readtext(image_path)

    if results:
        tablet_name = results[0][1]
        if tablet_name:
            first_letter = tablet_name[0].upper()
            if 'A' <= first_letter <= 'Z':
                row_number = ord(first_letter) - ord('A') + 1
                return tablet_name, row_number
    return None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    tablet_name, row_number = get_tablet_row(filepath)
    os.remove(filepath)

    if tablet_name and row_number:
        return jsonify({'tablet_name': tablet_name, 'row': row_number})
    else:
        return jsonify({'row': None})

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
