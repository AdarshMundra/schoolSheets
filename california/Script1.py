from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
url ='https://goredsgo.ca/information/directory/index'
def LINKTOCSV(url):
    path=url
    path=path.replace('https://','')
    # path=path.split('.com')[0]
    path = path.split('.ca')[0]
    # path = path.split('.net')[0]
    # path=path.split('.org')[0]
    # path=path.split('.edu')[0]
    
    
    

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page,'html.parser')
    table = soup.find_all('table')
    Header = soup.find_all("h2")
    df_list0 = pd.read_html(str(table[0]))
    FallSports=df_list0[0]
    FallSports = FallSports.dropna(how='all')
    FallSports.reset_index(drop=True, inplace=True)
    l,m=[],[]
    l=[Header[1].text]
    l=pd.DataFrame(l)
    m=l.append(FallSports)
    for i in range(1,len(table)):
        l=[Header[i+1].text]
        l=pd.DataFrame(l)
        m=m.append(l)
        df_list0 = pd.read_html(str(table[i]))
        FallSports1=df_list0[0]
        FallSports1 = FallSports1.dropna(how='all')
        FallSports1.reset_index(drop=True, inplace=True)
        result = m.append(FallSports1)
        m = result
    FallSports.to_csv(path+'.csv',  index=False)
LINKTOCSV(url)