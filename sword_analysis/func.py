import pandas as pd
import numpy as np

HARPY = 'harpy.co'
WESTEROS = 'westeros.inc'

def read_data(file='data/Base4.xlsx'):
    data = pd.read_excel(file)
    
    return data

def total_sword_number(data):
    swords_sum = data[data.supplier == HARPY].produced.sum()
    defects_sum = data[data.supplier == HARPY].defects.sum()
    print(swords_sum, defects_sum)
