from datetime import time
import json
import pickle, numpy as np, pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
from copy import copy
from functools import reduce
from common import *
from bokeh.models.widgets import Button, Slider, Div, DataTable, Paragraph
from bServer import *
from bokeh.io import show
from bokeh.models import Button, CustomJS
from bokeh.events import ButtonClick
from bokeh import model
from bokeh.layouts import  column, row, layout

class O:

    def __init__(self):
        self.files = sorted(grabFiles())
        self.d = loadPickle(self.files[-1])
        self.d['xs'] = self.d['time']
        self.last = None
        """"['time', 'timeStamp', 'buyPressure', 'sellPressure', 'nnBuy', 'nnSell', 'totalValue']"""
        self.keys = list(self.d.keys())
        self.n = len(self.d[self.keys[0]])
        self.isRunning = False
        self.runingTime = 0

        self.d['xs'] = mmap(extractTime2, self.d['time'])
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
        self.d['xs'] = mmap(extractTime2, self.d['time'])
        self.n = len(self.d['xs'])
        self.compare()
        print(f"\rListening, up for {self.runingTime} seconds, last file: "
              f"{self.files[-1].split('2020_')[1]}, #{self.n} data point", end="")
        threading_func_wrapper(self.update, 1)

if "o" in globals(): o.stop()
o = O()

#%%


def makePlot():
    import numpy as np
    from bokeh.plotting import figure, output_file, show
    x = np.linspace(0, 4 * np.pi, 100)
    y = np.sin(x)
    p = figure(plot_width=1400, plot_height=600)
    p.line(x, y, legend_label="sin(x)")
    p.line(x, 2 * y, legend_label="2*sin(x)",
           line_dash=[4, 4], line_color="orange", line_width=2)
    p.legend.location = "top_left"
    p.line(x, 3 * y, legend_label="3*sin(x)", line_color="green")
    p.legend.click_policy = "hide"
    return p


def makeTop(p):
    button = Button(label="Foo", button_type="success")
    button.on_click(callBack)
    return row(column(p,
                  button), Div(text='App has been created successfuly'),)


def modify_doc(self, doc): # this will create a Plot and hook up handlers(doc, root, plot) to the server
    self.p = makePlot()
    self.top = makeTop(self.p)
    self.doc = doc
    doc.add_root(self.top)
    self.doc = doc
    print(doc)


Base_server.modify_doc = modify_doc
s = Serv(run=True, view=True)
server = s.server
curdoc = s.doc

""""['time', 'timeStamp', 'buyPressure', 'sellPressure', 'nnBuy', 'nnSell', 'totalValue']"""
def callBack():
    print('I was clicked')


#%%
def update(top, doc, plot):
    return

s.doc.add_next_tick_callback(lambda: update(s.top, s.doc, s.p))

