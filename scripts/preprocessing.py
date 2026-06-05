from extract import Extractor
import pandas as pd

def data_clean() -> pd.DataFrame:

    datas = Extractor().extract_to_dict()
    df = pd.DataFrame(datas)

    df['release_date'] = pd.to_datetime(df['release_date'])
    df['price'] = df['price'].apply(lambda x: x.replace(',','.').replace('R$','') if x.startswith('R$') else '0.0').astype('float')
    df['discount_percent_percent'] = df['discount_percent_percent'].fillna('0.0').apply(lambda x: x.replace('%','') if x.endswith('%') else x).astype('float')
    df['price_whitout_discount'] = df['price']/(1 + df['discount_percent_percent']/100)
    df['day_release'] = df['release_date'].dt.day
    df['month_release'] = df['release_date'].dt.month
    df['year_release'] = df['release_date'].dt.year

    return df

