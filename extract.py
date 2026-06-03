# %%
from bs4 import BeautifulSoup
import requests as rq

class Extractor:
    def __init__(self):
        self.url = 'https://store.steampowered.com/search/'

    def extract_html_from_url(self,params=None):
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) "
                "Gecko/20100101 Firefox/117.0"
            )
        }

        return rq.get(self.url,headers=headers,params=params,timout=10).text

    def get_table(self):

        page = 1
        lista = []

        while True:

            params = {
                'filter': 'globaltopsellers',
                'page': page,
            }
            soup_list = BeautifulSoup(self.extract_html_from_url(params=params),'html.parser').find_all('a',class_='search_result_row ds_collapse_flag')
            lista.extend(soup_list)
            print(f'Foram coletados: {len(soup_list)} jogos')
            if not soup_list:
                print('Fim da lista')
                break
            
            page+=1
        
        return lista




