import pywhatkit
import csv
from datetime import datetime


# Read numbers from CSV file (one column, no header)
numbers = []
with open("numbers.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row is not None and len(row) > 0:
            numbers.append("+233" + row[0][1:].strip())


message = """Hello, this is a test message sent using pywhatkit."""
image_path = "path/to/your/image.jpg"  # Replace with your image path

for number in numbers:
    pywhatkit.sendwhats_image(
        receiver=number,
        img_path=image_path,
        caption=message,
        wait_time=15,
        tab_close=True,
        close_time=5,
    )
    print(f"Message sent to {number} at {datetime.now().strftime('%H:%M')}")
