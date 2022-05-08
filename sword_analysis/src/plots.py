import matplotlib.pyplot as plt
import numpy as np

class my_bar:
    def __init__(self, label_x='', label_y='', title='my_plot'):
        self.plot = plt
        self.plot.figure(figsize=(9,5))
        self.plot.title(title)
        self.plot.xlabel(label_x)
        self.plot.ylabel(label_y)
    
    def params(self, x_coor, y_harpy, y_wes):
        len_x = len(x_coor)

        ids = np.arange(1, len_x + 1)
        width = 1 / (len_x * (-0.2 * len_x + 1.9)) 

        self.plot.bar(ids - width / 2, y_harpy, width, label='harpy')
        self.plot.bar(ids + width / 2, y_wes, width, label='westeros')
        self.plot.xticks(ids, x_coor, rotation=45)

        plt.legend(fontsize=10)

    def show_plt(self):
        self.plot.show()
        
class my_plot:
    def __init__(self, label_x='', label_y='', title='my_plot'):
        self.plot = plt
        self.plot.figure(figsize=(9,5))
        self.plot.title(title)
        self.plot.xlabel(label_x)
        self.plot.ylabel(label_y)
    
    def params(self, x_coor, y_harpy, y_wes):
        len_x = len(x_coor)

        ids = np.arange(1, len_x + 1)
        width = 1 / (len_x * (-0.2 * len_x + 1.9)) 

        self.plot.plot(x_coor, y_harpy, linestyle='--', color='orange', label='harpy')
        self.plot.plot(x_coor, y_wes, linestyle='--', color='blue', label='westeros')
        self.plot.xticks(ids, x_coor, rotation=45)

        plt.legend(fontsize=10)

    def show_plt(self):
        self.plot.show()