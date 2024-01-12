import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = 'https://www.coffeshop.com'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Lakukan scraping data di sini
        data = soup.find('div', class_='example-class').text
        return data
    else:
        print(f'Failed to fetch data. Status Code: {response.status_code}')
        return None

def import_to_crm(data):
    # Gantilah ini dengan kodenya sesuai dengan API CRM yang digunakan
    print(f'Importing data to CRM: {data}')

if __name__ == "__main__":
    scraped_data = scrape_data()
    if scraped_data:
        import_to_crm(scraped_data)
    else:
        print('Scraping failed.')
