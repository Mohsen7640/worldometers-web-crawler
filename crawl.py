import requests

from bs4 import BeautifulSoup

from parser import Parser
from config import BASE_URL
from storage import MongoStorage



class DataCrawler:
    def __init__(self):
        self.parser = None
        self.storage = self.__set_storage()

    @staticmethod
    def __set_storage():
        return MongoStorage()

    @staticmethod
    def get_page(url):
        try:
            response = requests.get(url)
        except requests.HTTPError:
            return None
        return response

    @staticmethod
    def get_rows_table(html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        get_table_tag = soup.find(
            'table',
            attrs={'id': 'main_table_countries_today'}
        )
        get_tbody_tag = get_table_tag.find('tbody')
        get_rows_table = get_tbody_tag.find_all('tr', attrs={'class': ''})

        return get_rows_table

    def store(self, data, collection_name='coronavirus'):
        self.storage.store(data, collection_name)

    def start(self, store=False):
        response = self.get_page(BASE_URL)
        rows = self.get_rows_table(response.text)

        for row in rows:
            self.parser = Parser(row)
            data = self.parser.parse()

            if store:
                self.store(
                    data=data
                )
        print('- Complete Store Data In Database')
