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

        return rq.get(self.url,headers=headers,params=params).text

    def get_games_infos(self):

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
    
    def preprocessing(self):

        games_structured_list = []
        games_not_structured = self.get_games_infos()

        for row in games_not_structured:
            games = {}

            div_rewiew = row.find('div',class_='search_reviewscore responsive_secondrow')
            div_price = row.find('div',class_='search_price_discount_combined responsive_secondrow')
            div_price_final = div_price.find('div',class_='discount_final_price')
            div_percent = div_price.find('div',class_='discount_pct')


            games['name'] = row.find('span',class_='title').text
            games['release_date'] =  row.find('div',class_='search_released responsive_secondrow').text.strip()
            
            games['type_review'] = (
               div_rewiew.find('span').get('data-tooltip-html').split('<br>')[0]
                if div_rewiew and div_rewiew.find('span') and div_rewiew.find('span').get('data-tooltip-html')
                else None)
            
            games['has_discount'] = 1 if 'discount_pct' in str(div_price) else 0
            games['price'] = div_price_final.text if div_price_final else 'free'
            games['discount_percent_percent'] = div_percent.text if div_percent else None

            games_structured_list.append(games)

        return games_structured_list

