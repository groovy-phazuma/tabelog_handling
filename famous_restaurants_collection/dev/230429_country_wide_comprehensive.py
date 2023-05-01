#!/usr/bin/env python3
"""
Created on 2023-04-29 (Sat) 23:37:23

Comprehensive analysis for country-wide genres.

@author: I.Azuma
"""
#%%
import pprint
import pandas as pd
from tqdm.auto import tqdm

import sys
sys.path.append('C:/github/tabelog_handling/')

from famous_restaurants_collection import basic_info_collection as bic

#%%
cwide_url = pd.read_pickle('C:/github/tabelog_handling/famous_restaurants_collection/data/cwide_url_list.pkl')
pprint.pprint(cwide_url)

#%%
for url in cwide_url:
    genre = url.split('/')[-1]
    print(genre)
    dat = bic.BasicInfoCollection(url=url)
    dat.collect()
    res_df = dat.res_df
    res_df.to_csv('C:/github/tabelog_handling/famous_restaurants_collection/results/2022_'+str(genre)+'_top_100.csv',index=False,encoding='utf_8_sig')