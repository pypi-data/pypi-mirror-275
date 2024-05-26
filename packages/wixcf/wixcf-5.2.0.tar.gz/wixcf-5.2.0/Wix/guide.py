import requests
from bs4 import BeautifulSoup

url = "https://iplocation.io/my-location"
list1 = []
response = requests.get(url)
if response.status_code == 200:
    # BeautifulSoup ile web sayfasının içeriğini çıkaralım
        soup = BeautifulSoup(response.content, "html.parser")

        # Başlıkları çekmek için uygun HTML etiketlerini kullanalım (örn. <h1>, <h2>, <h3>)
        # Burada örnek olarak sadece h2 başlıklarını alalım
        headers = soup.find_all("div")

        # Başlıkları ekrana yazdıralım
        for header in headers:
            list1.append(header.text)
        for i in list1:
            print(i)