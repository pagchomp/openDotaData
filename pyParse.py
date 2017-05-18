# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:24:48 2017

@author: brett
"""

#import gzip
#count = 0
#with gzip.open('E:/Projects/openDotaData/player_matches.gz', 'rb') as f:
#    for line in f:
#        count += 1
#print(count)

#import pandas as pd
#data = pd.read_csv('E:/Projects/openDotaData/player_matches.gz', compression='gzip',
#                   error_bad_lines=False)
#print(data)

import pandas as pd
import urllib.request as ur
from bs4 import BeautifulSoup
import requests
#import http.client
import time
#http.client

folder = "E:/Projects/openDotaData/"
basicHeroDF = pd.read_json(folder + "dotapull")
imgDF = pd.read_csv(folder + "heroes.csv")
imgDF.columns = ['localized_name', 'image']
basicHeroDF.join(imgDF, on = "localized_name", how = "left", lsuffix = " ", rsuffix = " ")

heroesDF = basicHeroDF.set_index('localized_name').join(imgDF.set_index('localized_name'))

#import bs4
# https://www.dotabuff.com/heroes/anti-mage
failed = []
currHero = "anti-mage"

try:

#    hdr= { 'User-Agent' : 'my bot' }
#    conn = http.client.HTTPConnection('https://www.dotabuff.com/heroes/' + currHero)
#    for name in lst.split():
#    conn.request('GET', '/r/'+name, headers=hdr)
#    print conn.getresponse().read()
#    time.sleep(2)
#conn.close()
#    r = ur.urlopen('https://www.dotabuff.com/heroes/' + currHero).read()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get('https://www.dotabuff.com/heroes/' + currHero, headers = headers)
#    soup = BeautifulSoup(r.content)
soup = BeautifulSoup(r.content, 'html.parser') 

#'https://www.dotabuff.com/heroes/' + currHero + '/guides'

#    data = []
#    table = soup.find('table')
#    
#    rows = table.find_all('tr')
#    name = rows[4]
#    name.find_all('td')[1].text
#    
#    name = name.prettify().split( )
#    filename = []
#    for n in name:
#        if "<" not in n and ">" not in n:
#            filename.append(n)
#    filename.reverse()
#    filename = ".".join(filename)
#    
#    pdfkit.from_url('https://mce.cc/brookdale/sor.asp?cid=' + currentNum, folder + filename + '.pdf')
#    print('success ' + currentNum)
#except:
#print('failed ' + currentNum)
#failed.append(currentNum)
#
#print('process completed. failed: ')
#for i in failed:
#    print i        