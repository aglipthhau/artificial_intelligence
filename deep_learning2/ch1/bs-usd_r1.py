from bs4 import BeautifulSoup
import urllib.request as req
# HTML 가져오기
url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)
# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
# 원하는 데이터 추출하기 --- (※1)
price = soup.select_one("#worldExchangeList > li:nth-child(1) > a.head.jpy_usd > div > span.value").string

print("exchange rate jpy =", price)
