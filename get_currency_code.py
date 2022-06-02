import requests
from bs4 import BeautifulSoup

def get_countries_info(url):
  request_iban = requests.get(url)

  html_iban = request_iban.text

  soup = BeautifulSoup(html_iban, 'html.parser')
  
  countries = soup.find('tbody')

  countries_tr = countries.find_all('tr')

  country_infos = []
  list_country = []
  
  for tr in countries_tr:
    tds = tr.find_all('td')
    list_country.append(tds)
    try:
      country = {
        'name': list_country[0][0].text,
        'currency_code': list_country[0][2].text
      }
  
      country_infos.append(country)
  
      list_country.clear()
    
    except:
      list_country.clear()
      continue

  return country_infos