# cli_modules/app.py

from flask import Flask, send_file, abort, render_template
from cli_modules.utils import Storage_FOLDER, create_temp_link
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.template_folder = '../templates'  # Specify custom templates folder

@app.route('/', methods=['GET'])
def list_files():
    files = []
    for filename in os.listdir(Storage_FOLDER):
        file_path = os.path.join(Storage_FOLDER, filename)
        file_link = f"http://127.0.0.1:5000/download/{filename}"
        files.append({'filename': filename, 'link': file_link})
    return render_template('index.html', files=files)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(Storage_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        abort(404)
