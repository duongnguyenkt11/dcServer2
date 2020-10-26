from datetime import time
import json
import pickle, numpy as np, pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
from copy import copy
from functools import reduce
from common import *




class O:

    def __init__(self):
        self.files = sorted(grabFiles())
        self.d = loadPickle(self.files[-1])
        self.d['xs']
        self.last = None
        # ['time', 'timeStamp', 'buyPressure', 'sellPressure', 'nnBuy', 'nnSell', 'totalValue']
        self.keys = list(self.d.keys())
        self.n = len(self.d[self.keys[0]])
        self.isRunning = False
        self.runingTime = 0

        [exec3(f"mv {os.path.join( PARSED_DIR,fp)} {CACHED_FOLDER}") for fp in self.files[:-1]]
        self.start()
        return


    def stop(self):
        self.isRunning = False


    def start(self):
        self.isRunning = True
        threading_func_wrapper(self.update, 0.1)


    def compare(self):
        return


    def update(self):
        if not self.isRunning: return
        self.runingTime += 1
        self.files = sorted(grabFiles())
        self.last = self.d
        self.d = loadPickle(self.files[-1])
        self.compare()
        print(f"\rListening, up for {self.runingTime} seconds, last file: "
              f"{self.files[-1].split('2020_')[1]}", end="")
        threading_func_wrapper(self.update, 1)

if "o" in globals(): o.stop()
o = O()
d = o.d


# ['time', 'timeStamp', 'buyPressure', 'sellPressure', 'nnBuy', 'nnSell', 'totalValue']

keys = o.keys
#%%

def plot():
    output_file("/home/sotola/graphs/ApLucMuaBan2.html")
    p = figure(plot_width=PWIDTH, plot_height=PHEIGHT,
               title=f"Áp lực mua bán toàn tt (B:{self.bp[-1]:.1f} S:{self.sp[-1]:.1f} {self.times[-1]})");
    p.line(self.Xs, self.bp, line_width=2, color="green")
    p.line(self.Xs, self.sp, line_width=2, color="red")
    show(p)

plot()












