# 🛡️ Keylogger - Task 4 (Prodigy Infotech Internship)

This is a basic Python keylogger created for Task 4 of the Cybersecurity Internship at Prodigy Infotech. It captures keystrokes and logs them to a file, with a timestamp for each session start.

Disclaimer: This tool is intended for educational purposes only. Do not use it on any system without explicit permission. Unauthorized monitoring is illegal and unethical.

##  How to Set It Up and Run

###  1. Install Python virtual environment tool (if not already installed)
sudo apt install python3-venv

###   2. Create a project folder and navigate into it
mkdir keylogger
cd keylogger

###   3. Create and activate the virtual environment
python3 -m venv keyenv
source keyenv/bin/activate

###   4. Install the required package inside the virtual environment
pip install pynput

###  5. Create the Python keylogger file
Create a file named keylogger.py and paste the main.py code from this directory

###  6. Run the keylogger
Make sure you're in the project directory and the virtual environment is activated (you’ll see (keyenv) at the start of the terminal):
python keylogger.py
To stop logging, press Ctrl + C.
###  7. Viewing the log
The log is stored in the same directory with name log.txt.
