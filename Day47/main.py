from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage

headers = {
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8"
}

def get(url: str) -> str:
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    return response.text

def send_email(sender: str, receiver: str, subject: str, body: str):
        print(body)
        # password = "gtct rluv ktqg iwvz"

        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=sender, password=password)

        #     msg = EmailMessage()
        #     msg.set_content(body)
        #     msg['Subject'] = subject
        #     msg['From'] = sender
        #     msg['To'] = receiver

        #     connection.send_message(msg)

def main():
    url = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B075CYMYK6/ref=sr_1_3?keywords=Instant%2BPot%2BDuo%2BPlus%2B9-in-1%2BElectric%2BPressure%2BCooker&s=home-garden&sr=1-3&th=1"

    soup = BeautifulSoup(get(url=url), "html.parser")
    offscreen_price = soup.find(name="span", class_="a-offscreen").getText()
    print(f"Today's price is {offscreen_price}")
    price = offscreen_price.split("$")[1]
    
    if float(price) < 100:
        send_email(sender="example@gamil.com", receiver="example@gamil.com", subject="Price Alert!", body=f"Time to buy your product:\n{url}")

if __name__ == "__main__":
    main()