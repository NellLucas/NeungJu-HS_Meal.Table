import requests
from bs4 import BeautifulSoup
import re
import datetime


Ntime = str(datetime.datetime.now())
day = Ntime[:4] + Ntime[5:7] + Ntime[8:10]
Mcode = input("시간대를 선택해주세요\n(아침:1, 점심:2, 저녁:3): ")
req = requests.get("https://stu.jne.go.kr/sts_sci_md01_001.do?schulCode=Q100000188&schulCrseScCode=4&schulKndScCode=04&"+"schMmealScCode="+f"{Mcode}"+"&schYmd="+f"{day}")
week = datetime.datetime.now().weekday() + 1
if(week==7):
    week = 0
print(day)

soup = BeautifulSoup(req.text, "html.parser")
datas = soup.find_all("tr")
datas = datas[2].find_all('td')

datas = str(datas[int(f'{week}')])
datas = datas.replace('<br/>','\n')
datas = re.sub(r"\d", "", datas)
for i in ['<br>','<td class="textC">','</td>','<td class="textC last">','.']:
    datas = datas.replace(f'{i}','')
print(datas)





