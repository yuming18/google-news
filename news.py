from google import google
from lxml import etree
from pyhanlp import *
import requests
#SHITTTTTTTT
query = ["洗錢", "賄賂", "貪污", "詐欺", "走私", "犯罪", "內線交易", "市場操縱", "毒品"]
#newspaper = ["聯合報", "經濟日報", "台灣蘋果日報", "中國時報", "自由時報", "工商時報", "聯合晚報"]
newspaper = ["聯合晚報", "經濟日報", "聯合報"]

num_page = 3

address = ["https://udn.com/news/story", "https://money.udn.com/money/story"]

hanlp = JClass('com.hankcs.hanlp.HanLP')
Segment = hanlp.newSegment()

NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')

for q in query:
    for n in newspaper:
        num_page = 3
        search_results = google.search(q+" "+n+" 新聞", num_page)

        print("="*30 + q + "="*30)
        for ele in search_results:
            if ele.link is None:
                continue
            if any(target in ele.link for target in address):
#            if "https://udn.com/news/story" or "https://money.udn.com/money/story" in ele.link:
                print(ele.link)
                html = requests.get(ele.link)
                etree_structure = etree.HTML(html.text)
                text = etree_structure.xpath(r'//*[@id="story_body_content"]//p/text()')
                article = " ".join(text)
                article = article.strip()

                # 人名
                #outfile.write(dash+" Person "+dash+"\n")
                print("="*10, "Person", "="*10)
                words = NLPTokenizer.segment(article)
                for word in words:
                    if "nr" in str(word.nature):
                        #outfile.write(word.word+"\n")
                        print(word.word)


        print("="*60 + "\n")
