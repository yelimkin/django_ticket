import requests
from bs4 import BeautifulSoup
import telegram

from alarm.models import SendMssg
from . import tele_info as ei
from datetime import datetime, timedelta

tlgm_bot = telegram.Bot(ei.TLGM_BOT_TOKEN)

url = "http://ticket.interpark.com/webzine/paper/TPNoticeList.asp"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

items = soup.select("#ticketOpen_bn > div.list > ul:nth-child(3) > li > a")
# print(items)
# print(len(items))

during_date = 2

def run():
    row, _ = SendMssg.objects.filter(c_date__lte = datetime.now() - timedelta(minutes=during_date)).delete()
    print(row, "deals deleted")

    for item in items:
        try:
            # print(item)
            img_url = item.select("span.poster > img")[0].get("src").strip()
            # print(img_url)

            title = item.select("span.info > span.tit > strong")[0].text.strip()
            # print(title)

            link = item.get("href")
            link = "http://ticket.interpark.com/webzine/paper/" + link
            # print(link)

            open_date = item.select("span.info > span.date")[0].text.strip()
            # print(open_date)

            cur_stat = item.select("span.info > span.txt")[0].text.strip()
            # print(cur_stat)

            db_link_cnt = SendMssg.objects.filter(link__iexact=link).count()
            if(db_link_cnt == 0):

                message = f"{title} -- {open_date} -- {cur_stat}"
                tlgm_bot.sendMessage(ei.chat_id, message)

                SendMssg(img_url=img_url, title=title, link=link, open_date=open_date, cur_stat=cur_stat).save()

        except Exception as e:
            continue