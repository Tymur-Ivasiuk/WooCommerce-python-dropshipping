from woocommerce import API

from itertools import *
from tqdm import tqdm
from idlecolors import *

from bs4 import BeautifulSoup
import requests

import base64
import re


# WooCommerce API Tokens
wcapi = API(
    url="https://jumpman.com.ua/",
    consumer_key="ck_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    consumer_secret="cs_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    timeout=50
)


# Функции загрузки изображений
def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json

def upload_image_to_wordpress(file_path, url, header_json):
    media = {'file': open(file_path,"rb"),'caption': ''}
    responce = requests.post(url + "wp-json/wp/v2/media", headers = header_json, files = media)
    return responce.json()['id']

hed = header("login","XXXX XXXX XXXX XXXX")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
URL_SETKA = 'https://setkashop.com/'
URL_JUMP = 'https://jumpman.com.ua/'

CATS_setka = [
    'muzhchinam/obuv',
    'muzhchinam/odezhda',
    'muzhchinam/aksessuary_man_ru',
]
JORDAN_mark = '?rdrf[man][]=17'
NIKE_mark = '?rdrf[man][]=15'

ROZMIRI = {
    '35.5': '3.5us/22см 35.5eur',
    '36.5': '4.5us/23.5см 36.5eur',
    '37.5': '5us/23.5см 37.5eur',
    '38': '5.5us/24см 38eur',
    '38.5': '6us/24см 38.5eur',
    '39': '6.5us/24.5см 39eur',
    '40': '7us/25см 40eur',
    '40.5': '7.5us/25.5см 40.5eur',
    '41': '8us/26см 41eur',
    '42': '8.5us/26.5см 42eur',
    '42.5': '9us/27см 42.5eur',
    '43': '9.5us/27.5см 43eur',
    '44': '10us/28см 44eur',
    '44.5': '10.5us/28.5см 44.5eur',
    '45': '11us/29см 45eur',
    '45.5': '11.5us/29.5см 45.5eur',
    '46': '12us/30см 46eur',
    '47': '12.5us/30.5см 47eur',
    '47.5': '13us/31см 47.5eur',
    '48.5': '14us/32см 48.5eur',
    '49.5': '15us/33см 49.5eur',
}
CATS = {
    'ХУДИ' : [{'id': 17}, {'id': 135}], 
    'Кроссовки' : [{'id': 16}, {'id': 128}], 
    'Сумка' : [{'id': 73}, {'id': 114}], 
    'Майка' : [{'id': 33}, {'id': 135}], 
    'Панама' : [{'id': 271}, {'id': 114}], 
    'Ветровка' : [{'id': 91}, {'id': 135}], 
    'Кофта' : [{'id': 17}, {'id': 135}], 
    'Парка' : [{'id': 123}, {'id': 135}], 
    'МЯЧ' : [{'id': 137}, {'id': 114}], 
    'Тапочки' : [{'id': 20}, {'id': 128}], 
    'Шапка' : [{'id': 266}, {'id': 114}], 
    'Шорты' : [{'id': 116}, {'id': 135}], 
    'Жилет' : [{'id': 131}, {'id': 135}], 
    'Толстовка' : [{'id': 17}, {'id': 135}], 
    'Кепка' : [{'id': 270}, {'id': 114}], 
    'Штаны' : [{'id': 126}, {'id': 135}], 
    'Куртка' : [{'id': 123}, {'id': 135}], 
    'Носки' : [{'id': 136}, {'id': 114}], 
    'Бейсболка' : [{'id': 270}, {'id': 114}], 
    'Jordan' : [], 
    'Свитшот' : [{'id': 17}, {'id': 135}], 
    'Лонгслив' : [{'id': 91}, {'id': 135}], 
    'Рюкзак' : [{'id': 72}, {'id': 135}], 
    'Рубашка' : [{'id': 33}, {'id': 135}], 
    'ФУТБОЛКА' : [{'id': 33}, {'id': 135}], 
    'Футболка' : [{'id': 33}, {'id': 135}], 
    'Бананка' : [{'id': 119}, {'id': 114}], 
    'Бомбер' : [{'id': 122}, {'id': 135}], 
    'Безрукавка' : [{'id': 131}, {'id': 135}], 
    'Брюки' : [{'id': 126}, {'id': 135}], 
    'Худи' : [{'id': 17}, {'id': 135}],
    
    'Костюм' : [{'id': 115}, {'id': 135}],
    'Жилетка' : [{'id': 131}, {'id': 135}],
    'ХУДИ' : [{'id': 17}, {'id': 135}],
    'РЮКЗАК' : [{'id': 72}, {'id': 114}],
    'Парка' : [{'id': 123}, {'id': 135}],
    'Сандали' : [{'id': 20}, {'id': 135}],
    'Полотенце' : [{'id': 114}],
    'Шорти' : [{'id': 116}, {'id': 135}],
    'КЕПКА' : [{'id': 270}, {'id': 114}],
    'МЯЧ' : [{'id': 137}, {'id': 114}],
    'Мессенджер' : [{'id': 72}, {'id': 114}],
    'Футболки' : [{'id': 33}, {'id': 135}],
    'Снуд' : [{'id': 114}],
    'Шкарпетки' : [{'id': 136}, {'id': 114}],
    'Трусы' : [{'id': 612}, {'id': 114}],
    'Ботинки' : [{'id': 127}, {'id': 128}],
    'Штани' : [{'id': 126}, {'id': 135}],
    'БРЮКИ' : [{'id': 126}, {'id': 135}],
    'ШОРТЫ' : [{'id': 116}, {'id': 135}],
    'ТОЛСТОВКА' : [{'id': 17}, {'id': 135}],
    'КРОССОВКИ' : [{'id': 16}, {'id': 128}],
    'Безрукавка' : [{'id': 131}, {'id': 135}]
}

no_article = []

def pars():
    m = 0
    for q in CATS_setka:
        general_url = URL_SETKA + q + NIKE_mark + '&' + JORDAN_mark
        responce = requests.get(general_url, headers=headers)
        soup1 = BeautifulSoup(responce.text, 'lxml')

        articles = []
        try:
            page_ico = soup1.find('ul', class_='pagination').findAll('li')[-1].findAll('a')[0].get('href')
            page = int(re.findall(r'&page=([+]?\d+)', page_ico)[0])
        except:
            page = 1
        print(page)

        for i in range(1, page + 1):
            pagenate_url = f'{general_url}&page={i}'
            r = requests.get(pagenate_url, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            items = soup.findAll('div', class_='caption')
            for j in items:
                m += 1
                r = requests.get(j.find('a').get('href'), headers=headers)
                soup = BeautifulSoup(r.text, 'lxml')
                item = soup.findAll('td', class_='description-right')
                name = soup.find('h1', class_='product-title').text
                if item[-1].text=='Есть в наличии':
                    art = item[0].text.strip()
                    articles.append(art)


                    jump_product_url = URL_JUMP + f'?s={art}&post_type=product'
                    req = requests.get(jump_product_url, headers=headers)
                    soup = BeautifulSoup(req.text, 'lxml')
                    item = soup.findAll('li', class_='product')
                    VIDOM = {}
                    VIDOM['cats'] = CATS[BeautifulSoup(r.text, 'lxml').find('h1', class_='product-title').text.split()[0]]
                    
                    if item==[]:
                        printc( red( f'#{m} - {art} - {name}') )

                        #ADD to wp
                        
                        soup = BeautifulSoup(r.text, 'lxml')
                        item3 = soup.find('select', class_ = 'form-control').findAll('option')[1:]
                        rozmiri = []
                        for l in item3:
                            rozmiri.append(l.text.strip().split()[0])
                            
                        VIDOM['title'] = soup.find('h1', class_ = 'product-title').text
                        VIDOM['article'] = soup.findAll('td', class_ = 'description-right')[0].text
                        VIDOM['desc'] = soup.find('div', id='tab-description').text
                        VIDOM['price'] = soup.find('h4').text[:-5]
                        VIDOM['rozmiri'] = rozmiri
                        
                        if len(str(VIDOM['price']))>3:
                            sv_d = 'SV' + str(VIDOM['price'])[:-3] + '-' + str(VIDOM['price'])[-3:] + 'D'
                        else:
                            sv_d = 'SV' + str(VIDOM['price']) + 'D'
                        VIDOM['SV'] = sv_d
                        VIDOM['images'] = []
                            

                        #images
                        item2 = soup.findAll('a', class_ = 'elevatezoom-gallery')
                        c = 0
                        o = []
                        for l in item2:
                            if not l.get('href') in o:
                                o.append(l.get('href'))
                        for l in o:
                            try:
                                response = requests.get(l, stream=True, headers=headers)
                                
                                with open(f".\setka-shop-scraper-master\images\{VIDOM['article']}-{c}.png", "wb") as handle:
                                    for data in tqdm(response.iter_content()):
                                        handle.write(data)
                                    
                                id_image = upload_image_to_wordpress(f".\images\{VIDOM['article']}-{c}.png", 'https://jumpman.com.ua/',hed)
                                VIDOM['images'].append(
                                    {
                                        "id": id_image,
                                        "alt": "product-image"
                                    }
                                )
                                c += 1
                            except:
                                print("IMAGES WRONG")
                        

                        try:
                            if VIDOM['cats'][1]=={'id': 114}:
                                single_product_data = {
                                    "name": VIDOM['title'],
                                    "type": "simple",
                                    "regular_price": VIDOM['price'],
                                    "sku": VIDOM['article'],
                                    "description": VIDOM['desc'],
                                    "categories": VIDOM['cats'],
                                    "images": VIDOM['images'],
                                    
                                    "brands": [38],
                                    "attributes": [
                                        {
                                            "id": 14,
                                            "visible": True,
                                            "variation": False,
                                            "options": ['DR', 'SS']
                                        },
                                        {
                                            "id": 16,
                                            "visible": True,
                                            "variation": False,
                                            "options": VIDOM['SV']
                                        }
                                    ]
                                }
                                wcapi.post('products', single_product_data)

                            else:
                                variable_product_data = {
                                    "name": VIDOM['title'],
                                    "type": "variable",
                                    "sku": VIDOM['article'],
                                    "description": VIDOM['desc'],
                                    "categories": VIDOM['cats'],
                                    "images": VIDOM['images'],
                                    "brands": [38],
                                    "manage_stock": True,
                                    "stock_quantity": 1
                                }
                                
                                if VIDOM['cats'][1]=={'id': 128}:
                                    variable_product_data["attributes"] = [
                                        {
                                            "id": 11,
                                            "visible": True,
                                            "variation": True,
                                            "options": [ROZMIRI[p] for p in VIDOM['rozmiri']]
                                        },
                                        {
                                            "id": 14,
                                            "visible": True,
                                            "variation": False,
                                            "options": ['DR', 'SS']
                                        },
                                        {
                                            "id": 16,
                                            "visible": True,
                                            "variation": False,
                                            "options": VIDOM['SV']
                                        }
                                    ]
                                    response = wcapi.post('products', variable_product_data).json()
                                    for i in VIDOM['rozmiri']:
                                            product_variation_data = {
                                                "regular_price": VIDOM['price'],
                                                "stock_quantity": 1,
                                                "attributes": [
                                                    {
                                                      "id": 11,
                                                      "option": ROZMIRI[i]
                                                    }
                                                ]
                                            }
                                            wcapi.post(f'products/{response["id"]}/variations', product_variation_data)
                                else:
                                    variable_product_data["attributes"] = [
                                        {
                                            "id": 4,
                                            "visible": True,
                                            "variation": True,
                                            "options": VIDOM['rozmiri']
                                        },
                                        {
                                            "id": 14,
                                            "visible": True,
                                            "variation": False,
                                            "options": ['DR', 'SS']
                                        },
                                        {
                                            "id": 16,
                                            "visible": True,
                                            "variation": False,
                                            "options": VIDOM['SV']
                                        }
                                    ]

                                    response = wcapi.post('products', variable_product_data).json()
                                    for i in VIDOM['rozmiri']:
                                            product_variation_data = {
                                                "regular_price": VIDOM['price'],
                                                "stock_quantity": 1,
                                                "attributes": [
                                                    {
                                                      "id": 4,
                                                      "option": i
                                                    }
                                                ]
                                            }
                                            wcapi.post(f'products/{response["id"]}/variations', product_variation_data)
                            printc( green(f'#{m} - SUCCESS - {name}') )        
                        except KeyError:
                            printc( purple(f'#{m} - DONT SUCCESS - {name}') )
                            no_article.append(art)
                    else:
                        try:
                            product = item[0].get('class')[2]
                            id_post = re.findall(r'post-([+]?\d+)', product)[0]
                            data = {
                                    "manage_stock": True,
                                    "stock_quantity": 1
                                }
                            
                            if VIDOM['cats'][1]=={'id': 114}:
                                wcapi.put(f"products/{id_post}", data)
                                
                            else:
                                g = wcapi.get(f'products/{id_post}').json()
                                var_id = g.get('variations')
                                
                                for x in var_id:
                                    wcapi.put(f"products/{id_post}/variations/{x}", data)
                            printc( blue(f'#{m} - {art} - {name}') )
                        except:
                            printc( red(f'#{m} - BAD UPDATE - {name}'))
                else:
                    printc( black(f'#{m} - NOT AVAILABLE - {name}') )


pars()
print(no_article)
