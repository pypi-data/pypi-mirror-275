import requests
import re
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import os
translator_en = GoogleTranslator(source='auto',target='en')
translator_ch = GoogleTranslator(source='auto',target='zh-CN')

def ic(root,q):
    res = requests.get("https://www.bing.com/images/search?q="+q)
    soup = BeautifulSoup(res.text, 'html.parser')
    img_blks = soup.find_all(class_="iusc")
    img_urls=[re.sub('.*"murl":"|","turl".*',"", i.get("m")) for i in img_blks]
    print(q+"\nfound:",len(img_urls))
    for url in img_urls:
        try:
            data=requests.get(url).content
            with open(root+"/"+"_".join(url.split("/")[-2:]),"wb") as f:
                f.write(data)
        except:
            print("Error:",url)
    return

def run(query, en_search=True, ch_search=True, max=100):
    # max値は目安量
    os.makedirs(query,exist_ok=True)
    ic(query,query)
    if en_search:
        text_en = translator_en.translate(query)
        ic(query,text_en)
    if ch_search:
        text_ch = translator_ch.translate(query)
        ic(query,text_ch)

def main():
    run("たくさんの猫")

if __name__ == '__main__':
    main()