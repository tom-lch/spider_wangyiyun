import time
import requests
from bs4 import BeautifulSoup
from config import headers_get_lists


def get_music(url):
    time.sleep(0.5)
    try:
        response = requests.get(url=url, headers=headers_get_lists).text
        soup = BeautifulSoup(response, 'html.parser')
        a_lists = soup.select('.m-sglst a')
        for a in a_lists:
            try:
                music_url = a['href']
                music_name = a.find_all('div')[1].find_all('div')[0].find_all('div')[0].string
                print(music_url, music_name)
                if not music_name:
                    music_name = ''
                with open('music_lists_detail.csv', 'a+', encoding='utf-8') as f:
                    f.write(music_url + ',' + music_name + '\n')
            except Exception as e:
                print('出错了, '+ a)
    except Exception as e:
        print('出错了, '+ url)


# 获取歌单中歌曲的名称和URL
def main(url):
    url = 'https://music.163.com' + url
    get_music(url)
    print('OK')
