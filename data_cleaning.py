import chompjs
import json


"""this part is to create a list of links to send to the parse method inside the spider.
    """

with open("links.json") as links:
    l = json.load(links)
    m = json.loads(l)

links_for_scrapy = []

for i in m:
    n = i["links"]
    for i in n:
        links_for_scrapy.append(i)

""" this part is to clean the file(data_inmo.json) exported after running the spider  """
with open("data_inmo.json", "r") as file:
    a = file.read()
    b = chompjs.parse_js_object(a)
lst = []
for i in b:
    c = i["data"]
    d = chompjs.parse_js_object(c)
    lst.append(d[0])

data_clean1 = []
for i in lst:
    e = i["classified"]
    data_clean1.append(e)

""" this part is to cosntruct the csv file with the desired data -> see image -> colums_to_pick.png"""

# keys = ["zip", "type", "price", "transactionType"]
# for key in keys:
#     print(data_clean[key])