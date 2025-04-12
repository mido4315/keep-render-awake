import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = "muhammedmahmoud088@gmail.com"
# Configuration
# Replace with the target URL
URL = 'https://cageflix.onrender.com/api/nicolas-cage'

# Function to check the page
def check_page():
    response = requests.get(URL)



def cloud_reminder():
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        subject = "AWS Weekly Reminder"
        body = f"keep-render-awake is still running." 
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL, TO_EMAIL, message)

    print("Notification sent!")


check_page()
cloud_reminder()
# Schedule the bot to run hourly
schedule.every(5).minutes.do(check_page)
# schedule.every(20).seconds.do(check_page)
schedule.every().week.do(cloud_reminder)

# Keep the bot running
while True:
    schedule.run_pending()
    time.sleep(1)
