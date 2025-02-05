# Keylogger with Screenshot Capture

## Description
This project is a keylogger that records user keystrokes and captures screenshots at regular intervals. The recorded data is saved to files and automatically sent via email.

## Features
- **Captures all keystrokes** typed by the user and saves them to a text file.
- **Takes screenshots** periodically and saves them as image files.
- **Sends the collected data** (text files and screenshots) via email.
- **Automatically deletes files** after sending to maintain stealth.
- **Uses multi-threading** to run both keystroke logging and screenshot capturing simultaneously.

## Requirements
Make sure you have the following Python libraries installed:
```bash
pip install keyboard pyscreenshot smtplib
```

## How It Works
1. The program starts **two threads**:
   - One for **capturing keystrokes** and saving them in a text file.
   - Another for **taking screenshots** at regular intervals.
2. Both files are **sent via email** after a specified time.
3. After sending, the recorded files are **deleted** to avoid storage accumulation.

## Setup Instructions
### Clone this repository:
```bash
git clone https://github.com/yourusername/keylogger.git
cd keylogger
```

### Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Update the email credentials in `Sending_via_gmail()` function:
- Replace `fromaddr` with **your email**.
- Replace `toaddr` with **the recipient email**.
- Generate an **App Password** from your email provider and replace it in `s.login()`.

### Run the script:
```bash
python keylogger.py
```

##  Important Note
> **This project is intended for educational and ethical use only. Using it without permission is illegal and violates privacy laws.**

