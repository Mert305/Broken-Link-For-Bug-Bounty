import requests
from bs4 import BeautifulSoup

target_url = "https://www.example.com" # hedef URL adresi

# Sayfa kaynağı alınıyor
response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tüm linkler taranıyor
for link in soup.find_all('a'):
    href = link.get('href')
    
    # Boş linkler kontrol ediliyor
    if href is None:
        continue
        
    # Linklere GET isteği gönderiliyor
    link_response = requests.get(href)
    
    # HTTP yanıt kodu kontrol ediliyor
    if link_response.status_code >= 400:
        print("Bozuk link tespit edildi: " + href)
