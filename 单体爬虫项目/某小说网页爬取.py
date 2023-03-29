import os
import re

import requests
from bs4 import BeautifulSoup
import chardet

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Content-Type': 'text/html; charset=UTF-8'
}

URL_INIT = 'https://www.biqugehxs.com/html/xiuxianjiushizheyangzide/'
# URL_INIT = 'https://www.biqugehxs.com/html/mamadejururenqiguimi/'
# URL_INIT = 'https://www.biqugehxs.com/html/daizhoumeiyanyimuchuangmoshi/'

select_text = '#content > div'
select_starting = 'body > div.container > div.row.row-section > div > div:nth-child(4) > ul > li:nth-child(1) > a'
select_ending = 'body > div.container > div.row.row-section > div > div:nth-child(2) > ul > li:nth-child(1) > a'
select_list = 'body > div.container > div.row.row-section > div > div:nth-child(4) > ul'
select_title = '#container > div > div > div.reader-main > h1'


def replace_str(s):
    s = s.replace('<div align="center">', '')
    s = s.replace('<br>', '\n')
    s = s.replace("<br/>", "\n")
    s = s.replace("\n\n", "\n")
    s = s.replace("\n\n", "\n")
    s = s.replace("    ", " ")
    s = s.replace('<!--script language="javascript" type="text/javascript" src="/css/js/txt.js"></script>', '')
    s = s.replace('<script language="javascript">', '')
    s = s.replace('</script-->\n</br></div>', '')
    return s


def initialize_soup(url, headers=None):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content.decode("gbk"), 'html.parser')
    return soup


def get_title(url, select, headers=None):
    soup = initialize_soup(url, headers=headers)
    title = soup.select_one(select).text.strip()
    replace_str(title)
    return title


def get_number_list(url, select):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for item in soup.select(select):
        for link in item.find_all('a'):
            href = link.get('href')
            href = re.sub('\D', '', href) if href else ''
            links.append(href)
    return links


def get_text(url, select, headers=None):
    soup = initialize_soup(url, headers=headers)
    content = soup.select_one(select)
    target_str = str(content)
    formatted_str = replace_str(target_str)
    return formatted_str


def write_to_many_file(string, name):
    folder = './param_dir'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    name = name + ".txt"
    path = os.path.join(folder, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(string)


def write_to_one_file(string, name):
    folder = './param_dir'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    dir_name = name.split("【")[1].split("】")[0] + ".txt"
    path = os.path.join(folder, dir_name)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(name)
        f.write('\n')
        f.write(string)


if __name__ == '__main__':
    links = get_number_list(URL_INIT, select_list)
    print(links)
    for i in links:
        url = URL_INIT + i + '.html'
        title = get_title(url, select_title, HEADERS)
        # print(url)
        test = get_text(url, select_text, HEADERS)
        # write_to_many_file(test, title)
        write_to_one_file(test, title)
        print(title)
