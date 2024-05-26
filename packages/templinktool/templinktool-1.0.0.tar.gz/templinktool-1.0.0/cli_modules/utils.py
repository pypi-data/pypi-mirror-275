# cli_modules/utils.py

import os
import shutil
import sqlite3
import subprocess
import fcntl
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

Storage_FOLDER = os.path.join(os.path.dirname(__file__), 'storage')
DB_FILE = os.path.join(os.path.dirname(__file__), 'file_expiration.db')
# Path to the PID file
PID_FILE = os.path.join(os.path.dirname(__file__), 'flask_pid.txt')

DEFAULT_EXPIRATION_TIME = 3600

if not os.path.exists(Storage_FOLDER):
    os.makedirs(Storage_FOLDER)

def create_temp_link(file_path, expiration_time=DEFAULT_EXPIRATION_TIME):
    """Copy the file to the storage folder and store its information in the database."""
    filename = secure_filename(os.path.basename(file_path))
    destination = os.path.join(Storage_FOLDER, filename)
    os.makedirs(Storage_FOLDER, exist_ok=True)
    shutil.copy(file_path, destination)
    
    # Add file information to the database
    add_file_to_database(filename, expiration_time)
    
    # Return the download link
    return f"http://127.0.0.1:5000/download/{filename}"

def start_ngrok():
    # Check if NGROK_AUTH_TOKEN environment variable is set
    ngrok_auth_token = os.environ.get('NGROK_AUTH_TOKEN')
    if ngrok_auth_token:
        # Set ngrok auth token
        ngrok_token(ngrok_auth_token)
    else:
        print("NGROK_AUTH_TOKEN environment variable is not set. Ngrok will run without authentication.")

    # Start ngrok to expose the local Flask server
    try:
        ngrok_process = subprocess.Popen(["ngrok", "http", "--log=stdout", "http://localhost:5000"])

        # Set the stdout file descriptor to non-blocking mode
        flags = fcntl.fcntl(ngrok_process.stdout.fileno(), fcntl.F_GETFL)
        fcntl.fcntl(ngrok_process.stdout.fileno(), fcntl.F_SETFL, flags | os.O_NONBLOCK)

        print("Ngrok started successfully.")
    except Exception as e:
        print("Error starting ngrok:", e)

def is_process_running(pid):
    """Check if a process with the given PID is running."""
    try:
        os.kill(pid, 0)  # Check if the process exists
    except OSError:
        return False
    else:
        return True

def store_pid(pid):
    if os.path.exists(PID_FILE):
        with open(PID_FILE, 'r') as f:
            pid = int(f.read().strip())
            if is_process_running(pid):
                print("Flask server is already running.")
                return
    """Store the Flask server PID in a file."""
    with open(PID_FILE, 'w') as f:
        f.write(str(pid))

def initialize_database():
    """Initialize the SQLite database."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS files
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           filename TEXT NOT NULL,
                           expiration_time DATETIME NOT NULL)''')
        conn.commit()

def add_file_to_database(filename, expiration_time):
    """Add file information to the database."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO files (filename, expiration_time) VALUES (?, ?)", (filename, expiration_time))
        conn.commit()

def delete_expired_files():
    """Delete expired files and their entries from the database."""
    now = datetime.now()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, filename FROM files WHERE expiration_time <= ?", (now,))
        expired_files = cursor.fetchall()
        for file_info in expired_files:
            filename = file_info[1]
            file_path = os.path.join(Storage_FOLDER, filename)
            try:
                os.remove(file_path)
                print(f"File {filename} has been deleted.")
            except Exception as e:
                print(f"Error deleting file {filename}: {e}")

        # Delete expired records from the database
        expired_ids = [file_info[0] for file_info in expired_files]
        cursor.execute("DELETE FROM files WHERE id IN ({})".format(','.join('?' * len(expired_ids))), expired_ids)
        conn.commit()

def printUrls():
    log_file_path = os.path.join(os.path.dirname(__file__), 'output.log')

    if not os.path.exists(log_file_path):
        print("Ngrok log file not found.")
        return

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if "addr" in line:
                url = line.strip().split()[-1]
                print("Ngrok URL:", url)