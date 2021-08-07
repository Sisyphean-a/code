from lxml import etree
import requests
text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

html=etree.HTML(text)
result=etree.tostring(html,encoding="utf-8")
print(result.decode('utf-8'))
#result=html.xpath("//li/a/@href")
#result=html.xpath('//a[@href="link1.html"]/../@class')
#result=html.xpath('//li[contains(@class,"item")]//text()')
print(result)
#print(len(result))




