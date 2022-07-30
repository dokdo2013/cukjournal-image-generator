from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from datetime import date, datetime
import calendar
import numpy as np
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta

f = open("config.txt", "r")
text = f.read()
textArray = text.split(' ')

class makeimg:
    def basicImg(self):
        img = Image.new("RGB", (1000, 1000), (197, 198, 199))
        img.paste((12, 46, 134), [20, 20, 980, 170])
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("AROCKET.TTF", 24)
        dt = datetime.now()
        year = dt.strftime("%Y")
        month = dt.strftime("%m")
        dateTitle = year + '년 ' + month + '월 ' + str(self.get_week_of_month()) + '주차'
        dateTitlesize = draw.textsize(dateTitle, font=font)
        draw.text(((1000 - dateTitlesize[0]) / 2, 40), dateTitle, font=font)

        font = ImageFont.truetype("AROCKET.TTF", 65)
        mainTitle = "새로운 기사를 소개합니다"
        mainTitlesize = draw.textsize(mainTitle, font=font)
        draw.text(((1000 - mainTitlesize[0]) / 2, 80), mainTitle, font=font)

        return img

    def get_week_of_month(self):
        calendar.setfirstweekday(6)
        dt = datetime.now()
        year = int(dt.strftime("%Y"))
        month = int(dt.strftime("%m"))
        day = int(dt.strftime('%d'))
        x = np.array(calendar.monthcalendar(year, month))
        week_of_month = np.where(x == day)[0][0] + 1
        return week_of_month

    def imgedit_h(self, url):
        if url == None:
            url = "https://www.catholic.ac.kr/front/imgs/common/simg61.png"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content)).convert("RGBA")
            img = img.crop((0, 54, 490, 246))
            img = img.resize((960, 385))
            mask = Image.new('RGBA', (960, 385), (0, 0, 0, 128))
            return Image.alpha_composite(img, mask)
        else:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content)).convert("RGBA")
            img = img.crop((0, 0, img.size[0], img.size[0]*0.392))
            img = img.resize((960, 385))
            mask = Image.new('RGBA', (960, 385), (0, 0, 0, 128))
            return Image.alpha_composite(img, mask)


    def imgedit_q(self, url):
        if url == None:
            url = "https://www.catholic.ac.kr/front/imgs/common/simg60.png"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content)).convert("RGBA")
            img = img.crop((62, 0, img.size[1] * 1.22 + 62, img.size[1]))
            img = img.resize((470, 385))
            mask = Image.new('RGBA', (470, 385), (0, 0, 0, 128))
            return Image.alpha_composite(img, mask)
        else:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content)).convert("RGBA")
            if img.size[0] > img.size[1]:
                img = img.crop((0, 0, img.size[1] * 1.22, img.size[1]))
                img = img.resize((470, 385))
                mask = Image.new('RGBA', (470, 385), (0, 0, 0, 128))
                return Image.alpha_composite(img, mask)

            if img.size[1] >= img.size[0]:
                img = img.crop((0, 0, img.size[0], img.size[0] * 0.819))
                img = img.resize((470, 385))
                mask = Image.new('RGBA', (470, 385), (0, 0, 0, 128))
                return Image.alpha_composite(img, mask)

    def img_2(self, title, url):
        img = self.basicImg()
        img.paste(self.imgedit_h(url[0]), (20, 190))
        img.paste(self.imgedit_h(url[1]), (20, 595))

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("AROCKET.TTF", 24)

        draw.text((40, 515), title[0], font=font)  # 글씨 제목 1
        draw.text((40, 920), title[1], font=font)  # 글씨 제목 2
        return img

    def img_3(self, title, url):
        img = self.basicImg()
        img.paste(self.imgedit_h(url[0]), (20, 190))
        img.paste(self.imgedit_q(url[1]), (20, 595))
        img.paste(self.imgedit_q(url[2]), (510, 595))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("AROCKET.TTF", 24)

        if len(title[1]) >= 20:
            titleTempString = title[1]
            titleTempArray = titleTempString.split(' ')
            titleWordCnt = len(titleTempArray)
            titleFirstCnt = int(titleWordCnt / 2)
            titleSecondCnt = titleWordCnt - titleFirstCnt
            titleFirstArray = []
            titleSecondArray = []
            for i in range(titleFirstCnt) :
                titleFirstArray.append(titleTempArray[i])
            for i in range(titleSecondCnt) :
                j = i + titleFirstCnt
                titleSecondArray.append(titleTempArray[j])
            titleFirst = " ".join(titleFirstArray)
            titleSecond = " ".join(titleSecondArray)
            draw.text((40, 900), titleFirst, font=font)  # 글씨 제목 2-1
            draw.text((40, 930), titleSecond, font=font)  # 글씨 제목 2-2
        else :
            draw.text((40, 920), title[1], font=font)  # 글씨 제목 3


        if len(title[2]) >= 20:
            titleTempString = title[2]
            titleTempArray = titleTempString.split(' ')
            titleWordCnt = len(titleTempArray)
            titleFirstCnt = int(titleWordCnt / 2)
            titleSecondCnt = titleWordCnt - titleFirstCnt
            titleFirstArray = []
            titleSecondArray = []
            for i in range(titleFirstCnt) :
                titleFirstArray.append(titleTempArray[i])
            for i in range(titleSecondCnt) :
                j = i + titleFirstCnt
                titleSecondArray.append(titleTempArray[j])
            titleFirst = " ".join(titleFirstArray)
            titleSecond = " ".join(titleSecondArray)
            draw.text((530, 900), titleFirst, font=font)  # 글씨 제목 3-1
            draw.text((530, 930), titleSecond, font=font)  # 글씨 제목 3-2
        else :
            draw.text((530, 920), title[2], font=font)  # 글씨 제목 3
        draw.text((40, 515), title[0], font=font)  # 글씨 제목 1
        return img

    def img_4(self, title, url):
        img = self.basicImg()
        img.paste(self.imgedit_q(url[1]), (20, 190))
        img.paste(self.imgedit_q(url[6]), (510, 190))
        img.paste(self.imgedit_q(url[7]), (20, 595))
        img.paste(self.imgedit_q(url[8]), (510, 595))

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("AROCKET.TTF", 24)

        if len(title[1]) >= 20:
            titleTempString = title[1]
            titleTempArray = titleTempString.split(' ')
            titleWordCnt = len(titleTempArray)
            titleFirstCnt = int(titleWordCnt / 2)
            titleSecondCnt = titleWordCnt - titleFirstCnt
            titleFirstArray = []
            titleSecondArray = []
            for i in range(titleFirstCnt) :
                titleFirstArray.append(titleTempArray[i])
            for i in range(titleSecondCnt) :
                j = i + titleFirstCnt
                titleSecondArray.append(titleTempArray[j])
            titleFirst = " ".join(titleFirstArray)
            titleSecond = " ".join(titleSecondArray)
            draw.text((40, 495), titleFirst, font=font)  # 글씨 제목 1-1
            draw.text((40, 525), titleSecond, font=font)  # 글씨 제목 1-2
        else :
            draw.text((40, 515), title[1], font=font)  # 글씨 제목 1

        if len(title[6]) >= 20:
            titleTempString = title[6]
            titleTempArray = titleTempString.split(' ')
            titleWordCnt = len(titleTempArray)
            titleFirstCnt = int(titleWordCnt / 2)
            titleSecondCnt = titleWordCnt - titleFirstCnt
            titleFirstArray = []
            titleSecondArray = []
            for i in range(titleFirstCnt) :
                titleFirstArray.append(titleTempArray[i])
            for i in range(titleSecondCnt) :
                j = i + titleFirstCnt
                titleSecondArray.append(titleTempArray[j])
            titleFirst = " ".join(titleFirstArray)
            titleSecond = " ".join(titleSecondArray)
            draw.text((530, 495), titleFirst, font=font)  # 글씨 제목 2-1
            draw.text((530, 525), titleSecond, font=font)  # 글씨 제목 2-2
        else :
            draw.text((530, 515), title[6], font=font)  # 글씨 제목 2

        if len(title[7]) >= 20:
            titleTempString = title[7]
            titleTempArray = titleTempString.split(' ')
            titleWordCnt = len(titleTempArray)
            titleFirstCnt = int(titleWordCnt / 2)
            titleSecondCnt = titleWordCnt - titleFirstCnt
            titleFirstArray = []
            titleSecondArray = []
            for i in range(titleFirstCnt) :
                titleFirstArray.append(titleTempArray[i])
            for i in range(titleSecondCnt) :
                j = i + titleFirstCnt
                titleSecondArray.append(titleTempArray[j])
            titleFirst = " ".join(titleFirstArray)
            titleSecond = " ".join(titleSecondArray)
            draw.text((40, 900), titleFirst, font=font)  # 글씨 제목 3-1
            draw.text((40, 930), titleSecond, font=font)  # 글씨 제목 3-2
        else :
            draw.text((40, 920), title[7], font=font)  # 글씨 제목 3

        if len(title[8]) >= 20:
            titleTempString = title[8]
            titleTempArray = titleTempString.split(' ')
            titleWordCnt = len(titleTempArray)
            titleFirstCnt = int(titleWordCnt / 2)
            titleSecondCnt = titleWordCnt - titleFirstCnt
            titleFirstArray = []
            titleSecondArray = []
            for i in range(titleFirstCnt) :
                titleFirstArray.append(titleTempArray[i])
            for i in range(titleSecondCnt) :
                j = i + titleFirstCnt
                titleSecondArray.append(titleTempArray[j])
            titleFirst = " ".join(titleFirstArray)
            titleSecond = " ".join(titleSecondArray)
            draw.text((530, 900), titleFirst, font=font)  # 글씨 제목 4-1
            draw.text((530, 930), titleSecond, font=font)  # 글씨 제목 4-2
        else :
            draw.text((530, 920), title[8], font=font)  # 글씨 제목 4

        return img

def parse():
    global textArray
    txt1 = str(textArray[0])
    txt2 = int(textArray[1])
    #today = datetime.date.today()
    today = datetime.strptime(txt1, '%Y-%m-%d').date()

    chkDate = today + relativedelta(days=txt2)

    url = 'http://www.cukjournal.com/news/articleList.html?view_type=sm'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    articleRaw = soup.findAll('div', {'class':'list-block'})

    title = []
    imgUrl = []

    for i in range(20):
        dateChk = datetime.strptime(articleRaw[i].find('div', {'class':'list-dated'}).text[-16:-6], '%Y-%m-%d').date()
        if dateChk >= chkDate and dateChk < today:
            try:
                imgChk = articleRaw[i].find('div', {'class':'list-image'}).get('style')
            except:
                imgUrl.append(None)
            else:
                imgLinkchk = articleRaw[i].find('div', {'class': 'list-titles'}).find('a').get('href')
                html = requests.get('http://www.cukjournal.com'+imgLinkchk).text
                soup = BeautifulSoup(html, 'lxml')
                imgChk = 'http://www.cukjournal.com' + soup.find('figure', {'data-type': 'photo'}).find('img').get('src')

                imgUrl.append(imgChk)
            title.append(articleRaw[i].find('strong').text[:-1])

    return title, imgUrl

class main:
    m = makeimg()
    def finalimg(self, title, imgUrl, save):
        if len(title) == 2:
            image = self.m.img_2(title, imgUrl)
        elif len(title) == 3:
            image = self.m.img_3(title, imgUrl)
        elif len(title) >= 4:
            image = self.m.img_4(title, imgUrl)
        image.save(save)

if __name__ == '__main__':
    main = main()
    title, imgUrl = parse()
    main.finalimg(title, imgUrl, '/var/www/hakbo/test.png')
