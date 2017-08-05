# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:24:48 2017

@author: brett
"""

import pandas as pd


folder = "E:/Projects/openDotaData/dotaconstants/build/"

heroAbilities  = pd.read_json(folder + "hero_abilities.json")
heroNames = pd.read_json(folder + "hero_names.json")
items = pd.read_json(folder + "items.json")
abilities = pd.read_json(folder + "abilities.json")

#imgDF = pd.read_csv(folder + "heroes.csv")
#imgDF.columns = ['localized_name', 'image']
#basicHeroDF.join(imgDF, on = "localized_name", how = "left", lsuffix = " ", rsuffix = " ")

