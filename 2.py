import urllib.requests
from bs4 import BeautifulSoup

# 기상청 홈페이지에서 날씨 정보 가져오기
url = "http://www.weather.go.kr/weather/observation/currentweather.jsp"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

# 현재 온도 가져오기
temperatures = soup.find_all("td", attrs={"class": "temperature"})
for temperature in temperatures:
    if temperature.span is None: # 온도 정보가 없는 경우 skip
        continue
    
    # 현재 온도가 18도 이하인 경우 알림 출력
    if float(temperature.span.string) <= 18:
        print("현재 기온이 18도 이하입니다!")
        break
else: # 18도 이하인 온도가 없는 경우
    print("현재 기온이 18도 이하가 아닙니다.")
