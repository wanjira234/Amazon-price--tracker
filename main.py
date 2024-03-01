import requests
from bs4 import BeautifulSoup
import smtplib
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
url_response = requests.get(url=url, headers=headers)
amazon = url_response.text
soup = BeautifulSoup(amazon, "lxml")
# print(soup.prettify())
price = soup.find("span", class_="aok-offscreen").getText()
currency = price.split("$")[1]
float_currency = float(currency)
# print(float_currency)
MY_EMAIL = "example@outlook.com"
MY_PASSWORD = "your_password"
if float_currency < 100:
    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="your_email@gmail.com",
            msg=f"Subject: AMAZON PRICE DEALS\n\n the price is currently:{float_currency} go now to amazon")


else:
    print("Price not found. Please check the HTML structure.")
