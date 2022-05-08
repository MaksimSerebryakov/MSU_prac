import pandas as pd
import numpy as np
import src.plots as plots

HARPY = 'harpy.co'
WESTEROS = 'westeros.inc'

def read_data(file='data/Base4.xlsx'):
    data = pd.read_excel(file)
    
    return data

def total_sword_number(data, supplier):
    swords_sum = data[data.supplier == supplier].produced.sum()
    defects_sum = data[data.supplier == supplier].defects.sum()

    return swords_sum, defects_sum

def make_plot_sum(data):
    swords_harpy, defects_harpy = total_sword_number(data, HARPY)
    swords_wes, defects_wes= total_sword_number(data, WESTEROS)
    pl = plots.my_bar(
        label_y='swords number',    
        title='Total Swords number and Defects number'
    )
    pl.params(
        pd.Series(['sum', 'defect']), 
        pd.Series([swords_harpy, defects_harpy]),
        pd.Series([swords_wes, defects_wes]),
    )
    pl.show_plt()

    print(
        'Percentage of defects to total swords number from Harpy: {:.2f}%'.format(
            (defects_harpy / swords_harpy) * 100, 
        ),
        'Percentage of defects to total swords number from Westeros: {:.2f}%'.format(
            (defects_wes / swords_wes) * 100, 
        ),
        sep='\n'
    )

def defects_monthly(data):
    harpy_average = []
    wes_average = []

    for i in range(1, 7):
        harpy = data[data.supplier == HARPY]
        harpy = harpy[harpy['report.date'] - harpy['production.date'] == i]
        harpy_mean = harpy[harpy['produced'] == 0].defects.mean()

        wes = data[data.supplier == WESTEROS]
        wes = wes[wes['report.date'] - wes['production.date'] == i]
        wes_mean = wes[wes['produced'] == 0].defects.mean()

        harpy_average.append(harpy_mean)
        wes_average.append(wes_mean)
    
    pl = plots.my_bar(
        'months',
        'swords number',
        'Monthly mean number of Defects'
    )
    pl.params(
        pd.Series(list(range(1, 7))), 
        pd.Series(harpy_average),
        pd.Series(wes_average),
    )
    pl.show_plt()

def life_time(data):
    harpy_life = []
    wes_life = []

    for i in range(1, 7):
        harpy = data[data.supplier == HARPY]
        harpy = harpy[harpy['report.date'] - harpy['production.date'] == i]
        harpy_mean = harpy[harpy['produced'] == 0].defects.sum()

        wes = data[data.supplier == WESTEROS]
        wes = wes[wes['report.date'] - wes['production.date'] == i]
        wes_mean = wes[wes['produced'] == 0].defects.sum()

        harpy_life.append(harpy_mean)
        wes_life.append(wes_mean)
    
    pl = plots.my_plot(
        'months',
        'swords number',
        'LifeTime of defective Swords'
    )
    pl.params(
        pd.Series(list(range(1, 7))), 
        pd.Series(harpy_life),
        pd.Series(wes_life),
    )
    pl.show_plt()