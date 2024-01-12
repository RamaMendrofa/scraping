#library dan request
import requests
from bs4 import BeautifulSoup 

# URL yang ingin di-scrape
url = 'https://www.coffeshop.com'

# Mengambil halaman HTML menggunakan library requests
response = requests.get(url)

# Mengecek apakah request berhasil (kode status 200)
if response.status_code == 200:
    # Parsing HTML menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Contoh: Mendapatkan semua tag <a> yang memiliki class 'link'
    links = soup.find_all('a', class_='link')
    
    # Menampilkan hasil
    for link in links:
        print(link.get('href'))

else:
    print(f'Gagal mengambil halaman. Kode status: {response.status_code}')
