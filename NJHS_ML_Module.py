import requests
from bs4 import BeautifulSoup
import re
import datetime

def NJHSML(date, time):
    req = requests.get("https://stu.jne.go.kr/sts_sci_md01_001.do?schulCode=Q100000188&schulCrseScCode=4&schulKndScCode=04&"+"schMmealScCode="+f"{time}"+"&schYmd="+f"{date}")
    week = datetime.datetime.strptime(date, '%Y%m%d').weekday() + 1
    if(week==7):
        week = 0
    print(date)
    soup = BeautifulSoup(req.text, "html.parser")
    datas = soup.find_all("tr")
    datas = datas[2].find_all('td')

    datas = str(datas[int(f'{week}')])
    datas = datas.replace('<br/>','\n')
    datas = re.sub(r"\d", "", datas)
    for i in ['<br>','<td class="textC">','</td>','<td class="textC last">','.','&amp;']:
        datas = datas.replace(f'{i}','')
    return datas



