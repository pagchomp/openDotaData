# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:24:48 2017

@author: brett
"""

#import gzip
#
#with gzip.open('E:/Projects/openDotaData/player_matches.gz', 'rb') as f:
#    for line in f:
#        print(f)
import pandas as pd
data = pd.read_csv('E:/Projects/openDotaData/player_matches.gz', compression='gzip',
                   error_bad_lines=False)
print(data)