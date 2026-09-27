
import requests
from bs4 import BeautifulSoup
url="https://www.scrapethissite.com/pages/simple/"
response=requests.get(url)
print("URL: ",response.url)
print("Status code: ",response.status_code)
print("Content-Type: ",response.headers.get("Content-Type"))
soup=BeautifulSoup(response.text,"html.parser")
# print(soup)
# find returns first element match
capital_city=soup.find("span",class_="country-capital")
# print(capital_city.text)
#find_all returns all elements matched
capital_cities=soup.find_all("span",class_="country-capital")
# for capital in capital_cities:
#     print(capital.text)

#css selectors
first_country=soup.select_one(".country-name")
# print("First country : ",first_country.get_text(strip=True))
#select all countries with country-name class
# countries=soup.select(".country-name")
# for country in countries:
#     print(country.get_text(strip=True))
