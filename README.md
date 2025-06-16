# Mass WhatsApp Messages Sender

This project allows you to send bulk WhatsApp messages automatically using Python and [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit). It reads phone numbers from a CSV file and sends your custom message to each number via WhatsApp Web.

## Features

- Send WhatsApp messages to multiple numbers automatically
- Read numbers from a CSV file (one number per line)
- Easy setup and usage

## Requirements

- Python 3.8+
- Google Chrome (or your default browser)
- WhatsApp account (logged in on WhatsApp Web)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Frederick-Teye/mass_whatsapp_messages.git
   cd mass_whatsapp_messages
   ```

2. **Create and activate a virtual environment (recommended):**

   - **On Linux/macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **On Windows:**
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare your numbers:**

   - Create a file named `numbers.csv` in the project directory.
   - Add one phone number per line ( e.g., `024XXXXXXXXXX`).

   Example:

   ```
   0247132272
   0501234567
   024XXXXXXX
   ```

2. **Edit your message:**

   - Open `main.py` and change the `message` variable to your desired message.

3. **Edit the path to the image:**

   - Place the image in the directory where main.py is located.
   - Change the value of `image_path` variable to the name of your image. Example:

   ```python
   image_path = "invitation.png"
   ```

4. **Run the script:**

   ```bash
   python main.py
   ```

   - The script will open WhatsApp Web in your browser and send messages to each number.
   - **Do not close the browser** while messages are being sent.

## Notes

- Each message is sent one after another, not all at once.
- Make sure your computer stays connected to the internet.
- After a message is sent, the tab where whatsapp web was opened in will be closed.

## Disclaimer

This project is for educational purposes only. Use responsibly and respect WhatsApp's terms of service.
