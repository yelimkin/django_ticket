import requests
from bs4 import BeautifulSoup
import telegram

from alarm.models import SendMssg
from . import tele_info as ei
from datetime import datetime, timedelta

tlgm_bot = telegram.Bot(ei.TLGM_BOT_TOKEN)

url_al = "http://ticket.interpark.com/webzine/paper/TPNoticeList.asp"
res_al = requests.get(url_al)

# url_da = "http://ticket.interpark.com/contents/Ranking/RankList?pKind=01011&pType=D&pCate=01011"
# res_da = requests.get(url_da)

soup_al = BeautifulSoup(res_al.text, "html.parser")
# soup_da = BeautifulSoup(res_da.text, "html.parser")
# print(soup)

items_al = soup_al.select("#ticketOpen_bn > div.list > ul:nth-child(3) > li > a")
# items_da = soup_da.select("body > div.rankingDetailBody")
# print(items_da)
# print(len(items))

during_date = 2

def run():
    row, _ = SendMssg.objects.filter(c_date__lte = datetime.now() - timedelta(minutes=during_date)).delete()
    print(row, "deals deleted")

    for item in items_al:
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
            open_date_m = open_date.split('.')[1]
            open_date_d = open_date.split('.')[-1].split('(')[0]
            open_date_dn = open_date_d + 1 
            # print(open_date_d)

            cur_stat = item.select("span.info > span.txt")[0].text.strip()
            # print(cur_stat)

            db_link_cnt = SendMssg.objects.filter(link__iexact=link).count()
            if(db_link_cnt == 0):

                message_al = f"{title} -- {open_date} -- {cur_stat}"
                tlgm_bot.sendMessage(ei.chat_id, message_al)

                SendMssg(img_url=img_url, title=title, link=link, open_date=open_date, open_date_m=open_date_m, open_date_d=open_date_d, open_date_dn=open_date_dn, cur_stat=cur_stat).save()

        except Exception as e:
            continue
