import multiprocessing

import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',

}


def get_content(url):
    path = url.split('/')[-1]
    content = requests.get(url= url,headers = headers)
    content = content.content
    with open('%s'%path,'wb') as f:
        f.write(content)
        print('%s下载成功'%path)


if __name__ == '__main__':

    list_ = []

    for key_ in range(217000, 2171974):
        url = 'https://sohu.com-v-sohu.com/20180830/12209_04e8a79a/800k/hls/9c7a4b3b%s.ts' % key_
        list_.append(url)

    pool = multiprocessing.Pool(80)
    for i in list_:
        pool.apply_async(get_content,args=(i,))

    pool.close()
    pool.join()
    print('全部完成')
