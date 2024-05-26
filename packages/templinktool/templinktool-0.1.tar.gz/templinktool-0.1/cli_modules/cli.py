# cli_modules/cli.py

import subprocess
import fcntl
import os
import multiprocessing
import time
from daemon.pidfile import TimeoutPIDLockFile
import daemon
from cli_modules.utils import start_ngrok, store_pid, is_process_running, printUrls
from cli_modules.app import app

PID_FILE = os.path.join(os.path.dirname(__file__), 'flask_pid.txt')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'output.log')

# start_ngrok()
# app.run(host='0.0.0.0', port=5000)
# printUrls()
def start_ngrok_wrapper():
    with open(OUTPUT_FILE, 'a') as f:
        f.write("Starting ngrok...\n")
    start_ngrok()

def start_flask_app():
    with open(OUTPUT_FILE, 'a') as f:
        f.write("Starting Flask app...\n")
    app.run(host='0.0.0.0', port=5000)

def print_urls():
    with open(OUTPUT_FILE, 'a') as f:
        f.write("Printing URLs...\n")
    printUrls()

def start():
    # Start ngrok in a subprocess
    p1 = multiprocessing.Process(target=start_ngrok_wrapper)
    p1.start()

    # Start Flask app in a subprocess
    p2 = multiprocessing.Process(target=start_flask_app)
    p2.start()

    # Start printUrls in a subprocess
    p3 = multiprocessing.Process(target=print_urls)
    p3.start()

    # Wait for user input to stop the subprocesses
    input("Press Enter to stop the subprocesses...")

    # Terminate the subprocesses
    p1.terminate()
    p2.terminate()
    p3.terminate()
# def start():
#     if os.path.exists(PID_FILE):
#         with open(PID_FILE, 'r') as f:
#             pid = int(f.read().strip())
#             if is_process_running(pid):
#                 print("Flask server is already running." + endpoint)
#                 return

#     # Create output file if it doesn't exist
#     if not os.path.exists(OUTPUT_FILE):
#         open(OUTPUT_FILE, 'w').close

#     context = daemon.DaemonContext(
#         pidfile=TimeoutPIDLockFile(PID_FILE),
#         working_directory=os.path.dirname(os.path.abspath(__file__)),
#         stdout=open(OUTPUT_FILE, 'w+'),
#         stderr=open(OUTPUT_FILE, 'w+'),
#     )

#     with context:
#         start_ngrok()
#         app.run(host='0.0.0.0', port=5000)
#         printUrls()

def stop():
    print("Stopping Flask server...")
    try:
        with open(PID_FILE, 'r') as f:
            flask_pid = int(f.read().strip())
            os.kill(flask_pid, 15)  # Send SIGTERM signal
            print("Flask server stopped.")
    except FileNotFoundError:
        print("Flask PID file not found. Flask server may not be running.")
    except ProcessLookupError:
        print("Flask server process not found. It may have already stopped.")
    finally:
        try:
            os.remove(PID_FILE)  # Remove the PID file
        except FileNotFoundError:
            pass  # PID file may have been already removed