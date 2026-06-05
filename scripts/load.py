# %%
import os
import pandas as pd
import preprocessing

data_directory = 'data'
raw_data_directory = 'raw'
df = preprocessing.data_clean()
type(df)

# %%
if os.path.exists(f'../{data_directory}')
