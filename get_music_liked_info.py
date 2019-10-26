import time

import pandas as pd
import spider_music_detail


# 从music_lists_detail.csv文件中获取歌曲信息，
# 并将信息提出出来，将URL作为参数调用spider_music_detail.py
def get_detail():
    L = []
    print('读入数据')
    data = pd.read_csv('total_music_liked.csv', names=['music_url', 'music_name', 'music_other'])
    print(data.head())
    for url in data['music_url']:
        print(url)
        try:
            spider_music_detail.main(url)
            print('ok')
        except Exception as e:
            L.append(url)
    with open('error.csv', 'a+') as f:
        f.write(str(L))

if __name__ == '__main__':
    print("开始执行")
    get_detail()
    print('OK')
