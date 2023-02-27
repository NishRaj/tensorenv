import os
import shutil

import gdown
import numpy as np
import pandas as pd

# Download files from Google Drive
# Based on data from: http://insideairbnb.com/get-the-data/
file_id_1 = "1m185vTdh-u7_A2ZElBvUD4SCO6oETll2"
file_id_2 = "1w41V1oWHJrBdaNJJQ4oxVBuml5CO7MQX"
downloaded_file_1 = "listings_project.pkl"
downloaded_file_2 = "calendar_project.parquet"
# Download the files from Google Drive
# gdown.download(id=file_id_1, output=downloaded_file_1)
# gdown.download(id=file_id_2, output=downloaded_file_2)

# Show all columns (instead of cascading columns in the middle)
pd.set_option("display.max_columns", None)
# Don't show numbers in scientific notation
pd.set_option("display.float_format", "{:.2f}".format)
df_list = pd.read_pickle("listings_project.pkl")
df_cal = pd.read_parquet("calendar_project.parquet")
#print(df_list.info(show_counts=True))
# print(df_list.loc[:5, 'discount_per_10_days_booked'])
df_list['discount_per_5_days_booked'] = df_list['discount_per_5_days_booked'].\
    str.replace("%", "", regex=True).astype(float)*.01
print(df_list.loc[:4, 'discount_per_5_days_booked'])
print(df_list[['host_is_superhost', 'instant_bookable', 'has_availability']].head(20))
df_list = df_list.replace(to_replace={'has_availability': {'f': False, 't': True},
                                      'host_is_superhost': {'f': False, 't': True},
                                      'instant_bookable': {'f': False, 't': True}})
df_list['has_availability'].astype(bool)
df_list['host_is_superhost'].astype(bool)
df_list['instant_bookable'].astype(bool)
print(df_list.loc[:50, ['service_cost', 'minimum_price', 'price_per_person', 'price']])

df_list = df_list.replace(to_replace={'service_cost': {'$': '', ',': ''},
                                      'minimum_price': {'$': '', ',': ''},
                                      'price_per_person': {'$': '', ',': ''},
                                      'price': {'$': '', ',': ''}},  regex=True)
df_list['service_cost'].astype(float)
df_list['minimum_price'].astype(float)
df_list['price_per_person'].astype(float)
df_list['price'].astype(float)


print(df_list.info(show_counts=True))