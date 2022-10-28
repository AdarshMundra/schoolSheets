from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

LISTURL=[
# "https://www.fontbonnegriffins.com/athletics/directory/index",
# "https://www.ahcbulldogs.com/athletics/directory/index",
# # "https://lmulions.com/staff-directory",
"https://goseawolves.com/staff-directory",
"https://gobuffsgo.com/sports/general/staff",
# "https://athletics.sierracollege.edu/about/directory/index",
"https://smusaints.com/staff-directory",
"https://goseattleu.com/staff-directory?path=ath"
]

def LINKTOCSV(url):
    path=url
    path=path.replace('https://','')
    
    # path=path.split('.com')[0]

    # path = path.split('.net')[0]
    path=path.split('.org')[0]
    # path=path.split('.edu')[0]
    
    
    

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page,'html.parser')
    table = soup.find_all('table')
    if len(table)==1:
        df_list0 = pd.read_html(str(table[0]))
        FallSports=df_list0[0]
        FallSports = FallSports.dropna(how='all')
        FallSports.reset_index(drop=True, inplace=True)
        FallSports.to_csv(path+'.csv',  index=False)
    if len(table)==2:
        df_list0 = pd.read_html(str(table[1]))
        FallSports1=df_list0[0]
        FallSports1 = FallSports1.dropna(how='all')
        FallSports1.reset_index(drop=True, inplace=True)
        FallSports1.to_csv(path+'.csv',  index=False)
    if len(table)==3:
        df_list0 = pd.read_html(str(table[2]))
        FallSports1=df_list0[0]
        FallSports1 = FallSports1.dropna(how='all')
        FallSports1.reset_index(drop=True, inplace=True)
        FallSports1.to_csv(path+'.csv',  index=False)
    print(len(table))
    print(path)
# LINKTOCSV(url)
for i in LISTURL:
    LINKTOCSV(i)
# import tensorflow as tf
# print(tf.VERSION)