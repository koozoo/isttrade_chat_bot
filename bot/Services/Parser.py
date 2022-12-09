import asyncio
import time

import async_timeout
import lxml
from bs4 import BeautifulSoup
import requests
from bot.database.models import *
from bot.database.methods import *

add_db = InsertDataBase()
get_db = GetDataBase()
update_db = UpdateDataBase()


async def create_product(url, cat):
    # PARSE PRODUCT
    print(cat)
    headers = {
        "accept": "* / *",
        "accept - encoding": "gzip, deflate, br",
        "accept - language": "ru - RU, ru; q = 0.9, en - US; q = 0.8, en; q = 0.7"
    }
    base_url = "https://isttrade.ru"
    r = requests.get(f"{base_url}{url}", headers=headers)
    s = BeautifulSoup(r.text, "lxml")

    item = []
    title = s.find(class_="major-heading").text
    img = f'{base_url}{s.find(class_="box-product-img").find("a").get("href")}'
    # description = s.find("box-product-text").text

    raw_docs = s.find(id="tab4").find_all(class_="content-inset")
    item.append(title)
    item.append(img)
    # item.append(description)

    docs = []
    for d in raw_docs:
        doc_title = d.find(class_="pdf-text").find_all("p")[0].text
        doc_link = f'{base_url}{d.find("a").get("href")}'

        docs.append((doc_title, doc_link))
    item.append(docs)
    print(item)
    await asyncio.sleep(1)

    # ADD DB
    id_category = [item.id for item in await get_db.get_category_where_title(cat)]
    print(id_category)
    item_prod = Products(title=item[0], img=item[1], is_active=True, category=id_category[0])

    await add_db.add_item_autoincrement(item_prod)

    id_prod = [item.id for item in await get_db.get_product_wher_title(item[0])]

    for link in item[2]:
        print(link)
        item_link = Links(id_prod[0], link=link[1])
        await add_db.add_item_autoincrement(item_link)

    return item


async def update_catalog():
    url = "https://isttrade.ru"
    headers = {
        "accept": "* / *",
        "accept - encoding": "gzip, deflate, br",
        "accept - language": "ru - RU, ru; q = 0.9, en - US; q = 0.8, en; q = 0.7"
    }

    category = [("Суперавтоматические кофемашины", "/catalog/171", "/images/isttrade.jpg"),
                ("Традиционные кофемашины", "/catalog/33", "/images/traditional_top.jpg"),
                ("Фильтр-кофемашины", "/catalog/172", "/images/filter-top.jpg"), ("Кофемолки", "/catalog/34",
                                                                                  "/images/coffeemill_top.jpg")]  # ("QR-системы", "/catalog/351", "/images/qr_big.jpg")

    all_item_cat = {}

    for i in category:
        r = requests.get(f"{url}{i[1]}", headers=headers)
        s = BeautifulSoup(r.text, "lxml")

        print(f"Сбор инфы категории {i[0]}")

        cat = s.find(class_="menu-group-category1").find_all(class_="active2")

        for item in cat:
            l = item.find("a").get("href")
            l_text = item.find("a").text

            if l == "#":
                sub_l = item.find("ul").find_all(class_="active3")

                for s_l in sub_l:

                    print(f"Product: {l_text}")

                    sub_prod_link = s_l.find("a").get("href")
                    await create_product(sub_prod_link, i[0])

                    try:
                        all_item_cat[f"{l_text}"] += [sub_prod_link]
                    except:
                        all_item_cat[f"{l_text}"] = [sub_prod_link]
            else:
                print(f"Product: {l_text}")
                await create_product(l, i[0])
                try:
                    all_item_cat[f"{i[0]}"] += [l]
                except:
                    all_item_cat[f"{i[0]}"] = [l]
            await asyncio.sleep(1)


