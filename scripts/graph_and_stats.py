#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

#dataframe,label,bar_kind,bar_title
class dwc_graph():
    def __init__(self):
        super().__init__()

    def make_graph(self,dataframe,label,bar_kind,graph_title):
        #Tipos de gráficos a diccionario y obtenerlas con método get
        bar_kind_dict={"Barras":"bar",
        "Barras horizontales":"barh",
        "Torta":"pie"
        }
        bar_kind=bar_kind_dict.get(bar_kind)
        if graph_title=="": graph_title=f"{label}"
        if bar_kind=="pie":
            dataframe[label].value_counts().plot(kind=bar_kind,title=graph_title, autopct='%1.1f%%')
        else:
            dataframe[label].value_counts().plot(kind=bar_kind,title=graph_title)
        plt.tight_layout()
        plt.show()
