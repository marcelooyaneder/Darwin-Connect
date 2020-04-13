#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

#dataframe,label,bar_kind,bar_title
class dwc_stats():
    def __init__(self):
        super().__init__()

    def make_graph(self,dataframe,label,bar_kind,graph_title,figsize_x,figsize_y):
        if bar_kind == "Barras":
            bar_kind=f"bar"
        elif bar_kind=="Barras horizontales":
            bar_kind=f"bar"
        if graph_title=="":
            graph_title=f"{label}"
        else:
            pass
        if figsize_x=="" or figsize_y=="":
            plt.figure();
            dataframe[label].value_counts().plot(kind=f"{bar_kind}",title=graph_title)
        else:
            plt.figure();
            dataframe[label].value_counts().plot(kind=f"{bar_kind}",title=graph_title,figsize=(figsize_x,figsize_y))