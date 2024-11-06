# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:23:50 2024

@author: tomke
"""

import pandas as pd
import plotly.express as px

data = pd.read_csv('sunspotsbyyear.csv')
px.line(data,x='Year',y='Sunspots')