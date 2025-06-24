import re
import requests
from bs4 import BeautifulSoup

def scrape_data_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        html = soup.prettify()
        text = soup.get_text()

        data = {
            "Website": url,
            "Emails": ", ".join(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))),
            "Phones": ", ".join(set(re.findall(r'\+?\d[\d\s\-().]{7,}\d', text))),
            "Facebook": ", ".join(set(re.findall(r'facebook\.com/[^\s"\'<>]+', html))),
            "LinkedIn": ", ".join(set(re.findall(r'linkedin\.com/[^\s"\'<>]+', html))),
            "Instagram": ", ".join(set(re.findall(r'instagram\.com/[^\s"\'<>]+', html))),
            "WhatsApp": ", ".join(set(re.findall(r'wa\.me/\d+', html))),
        }
        return data
    except Exception as e:
        return {
            "Website": url,
            "Emails": "",
            "Phones": "",
            "Facebook": "",
            "LinkedIn": "",
            "Instagram": "",
            "WhatsApp": "",
            "Error": str(e)
        }
