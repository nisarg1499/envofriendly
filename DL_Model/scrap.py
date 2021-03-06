#!/usr/bin/env python3

import json
import pickle
from pprint import pprint

import bs4
import requests
from tqdm import trange


def scrap() -> None:
    # urls = [298369, 10000148, 10000153]
    # 10000148-10000224
    # 10000226-10000360
    # 10000362
    # 10000365-10000574

    baseurl = 'https://www.bigbasket.com/pd/'
    items = {}
    for i in trange(40042542, 40052549):

        try:
            url = baseurl + str(i)
            page = requests.get(url)

            soup = bs4.BeautifulSoup(page.content, 'html.parser')

            res = {}

            res['name'] = soup.find('h1', class_='GrE04').text.strip()
            res['price'] = soup.find(
                'td', class_='IyLvo').text.split('Rs')[-1].strip()
            res['img'] = soup.findAll('img', class_='_3oKVV')[-1]['src']
            res['about'] = soup.find(id='about_0')
            res['ing'] = soup.find(id='about_1')
            res['category'] = soup.findAll(
                'a', class_='_3WUR_ _3bj9B rippleEffect')[2].text.split('>')[0]

            res['about'] = soup.find('div', class_='_26MFu').find('div').text

            if res['ing'].find('span').text != 'INGREDIENTS':
                res['ing'] = res['name']
            else:
                res['ing'] = res['ing'].find('div',
                                             class_='_26MFu').find('div').text
        except Exception:
            continue

        items[res['name']] = res

    return items
    # pprint(items)


if __name__ == '__main__':
    pickle.dump(scrap(), open('items-1.pkl', 'wb'))
