from flask import Flask, render_template, request
import requests, re, datetime
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    result = dict(request.form)
    Ntime = result['date']
    day = Ntime[:4] + Ntime[5:7] + Ntime[8:10]
    Mcode = result['time']
    req = requests.get("https://stu.jne.go.kr/sts_sci_md01_001.do?schulCode=Q100000188&schulCrseScCode=4&schulKndScCode=04&"+"schMmealScCode="+f"{Mcode}"+"&schYmd="+f"{day}")
    week = datetime.datetime.strptime(Ntime, '%Y-%m-%d').weekday() + 1
    print(week)
    if(week==7):
        week = 0
    if(Mcode=='1'or Mcode=='2' or Mcode=='3'):
        if(Mcode=='1'):
            NJtime = '아침'
        elif(Mcode=='2'):
            NJtime = '점심'
        else:
            NJtime = '저녁'
        soup = BeautifulSoup(req.text, "html.parser")
        datas = soup.find_all("tr")
        datas = datas[2].find_all('td')
        datas = str(datas[int(f'{week}')])
        datas = datas.replace('<br/>','\n')
        datas = re.sub(r"\d", "", datas)
        for i in ['<br>','<td class="textC">','</td>','<td class="textC last">','.','&amp;']:
            datas = datas.replace(f'{i}','')
    else:
        datas = '잘못된 입력입니다'
        NJtime = ''

    return render_template("result.html",result=datas,date=Ntime,NJtime=NJtime)


if __name__ == '__main__':
   app.run()