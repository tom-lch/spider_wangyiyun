import pandas as pd
import spider_total_music


def main():
    music_lists_0_1500 = pd.read_csv('music_lists_0_1500.csv', names=['url', 'title', 'play_num', 'user'])
    for url in music_lists_0_1500['url']:
        spider_total_music.main(url)


if __name__ == '__main__':
    main()
    print('OK')
