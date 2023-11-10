# app.py
from flask import Flask, render_template, request, jsonify
from multithreading_module import resize_images_parallel
import os

app = Flask(__name__)

# Configure upload and resized image folders
app.config['UPLOAD_FOLDER'] = 'uploads/temp_upload'
app.config['RESIZED_FOLDER'] = 'static/resized_images'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

# Ensure the upload and resized folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESIZED_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Get width and height parameters from the form
        width = int(request.form['width'])
        height = int(request.form['height'])

        # Resize the image
        resize_images_parallel([file_path], width, height)

        # Provide a response with the resized image path
        resized_image_path = os.path.join(app.config['RESIZED_FOLDER'], os.path.basename(file_path))
        return jsonify({'resized_image_path': resized_image_path}), 200

if __name__ == '__main__':
    app.run(debug=True)
