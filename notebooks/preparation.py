# %%
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os

data_path = '../data/raw/games_best_sellers.csv'

df = pd.read_csv(data_path)
df.head()
df.info()
# %%
df.drop(labels=['name','release_date'],inplace=True,axis=1)
df.head()

# %%
df_cat_features = ['type_review']
df_numerical_features = ['price','discount_percent_percent','price_whitout_discount','day_release','month_release','year_release']

imputer = SimpleImputer(strategy='most_frequent')
df_cat_imputed = imputer.fit_transform(df[df_cat_features])


df_cat_imputed_trans = pd.DataFrame(df_cat_imputed,columns=imputer.get_feature_names_out())

df.drop(df_cat_features,axis=1,inplace=True)

df_preprocessed_feature = pd.concat([df_cat_imputed_trans.reset_index(drop=True),df.reset_index(drop=True)],axis=1)

# %%
onehot = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
df_onehoted = onehot.fit_transform(df_preprocessed_feature[df_cat_features])
df_preprocessed_feature.drop(df_preprocessed_feature,inplace=True,axis=1)

# %%
df_onehoted_pre = pd.DataFrame(df_onehoted,columns=onehot.get_feature_names_out())
df_onehoted_pre.head()

df_categorical_preprocessed = pd.concat([df_onehoted_pre.reset_index(drop=True),df.reset_index(drop=True)],axis=1)
df_categorical_preprocessed.head()
# %%
minmax = MinMaxScaler()
df_minmax = minmax.fit_transform(df_categorical_preprocessed[df_numerical_features])
df_categorical_preprocessed.drop(df_numerical_features,inplace=True,axis=1)

# %%
df_numerical_prep = pd.DataFrame(df_minmax,columns = minmax.get_feature_names_out())

df_preprocessed = pd.concat([df_numerical_prep.reset_index(drop=True),df_categorical_preprocessed.reset_index(drop=True)],axis=1)
df_preprocessed.head()

# %%

if not os.path.exists('../data/raw/preprocessed'):
    os.mkdir('../data/raw/preprocessed')
    df.to_csv(os.path.join('../data/raw/preprocessed/','date_preprocessed.csv'),index=False)
# %%
