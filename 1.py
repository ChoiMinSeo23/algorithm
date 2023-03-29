import requests
from bs4 import BeautifulSoup

url = "http://www.kma.go.kr/weather/observation/currentweather.jsp"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
temperature = soup.select_one("table.table_develop3 td.temp").text

if int(temperature) <= 18:
    print("현재 기온이 18도 이하입니다.")

