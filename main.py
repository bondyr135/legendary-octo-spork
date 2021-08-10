from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
from mail_sender import send_mail
from write_file import write_file
import re

the_humble_URL = 'https://il.iherb.com/c/the-humble-co'
schmidt_URL = 'https://il.iherb.com/c/schmidt-s/deodorant?rank=1'

URLs = [schmidt_URL, the_humble_URL]


def find_products():
    for url in URLs:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        products = soup.find_all('div', class_='product-inner-wide')

        date = datetime.today().strftime("%d-%m-%y")
        list_of_products = []

        for product in products:
            product_name = product.find(
                'div', class_='product-title').text

            prices = product.find('div', class_='product-price-top')
            if prices.find('span', class_='text-danger-lighter'):
                break

            product_price = (prices.find('span', class_='price-olp')
                             or prices.find('span', class_='price')).text
            product_price = re.sub('[^\d\.]', '', product_price) + ' NIS'

            product_price_discount = (prices.find(
                'span', class_='discount-red') or prices.find(
                'span', class_='discount-green')) or None
            product_price_discount = re.sub(
                '[^\d\.]', '', product_price_discount.text) + ' NIS' if product_price_discount else ''

            product_dictionary = {
                'name': f'{product_name}',
                'org_price': f'{product_price}',
                'curr_price': f'{product_price_discount}'
            }
            list_of_products.append(product_dictionary)

        text_to_send = write_file(list_of_products)
        send_mail(text_to_send)


if __name__ == '__main__':
    while True:
        find_products()
        days = 7
        hours = 24
        minutes = 60
        seconds = 60
        print('Another scrape will be executed in one week')
        time.sleep(days * hours * minutes * seconds)
