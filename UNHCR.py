#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


# Loading the dataset:
df=pd.read_csv('dataset.csv')

# Selecting columns for the subset:
columns=[df.columns[4:9].tolist()+df.columns[11:16].values.tolist()][0]


# Main data subset for this visualization:
subset=df[columns] 

# Size values for the pie chart inner wedges:
sizes=subset.values[0]

# Labels for the pie chart inner wedges:
labels=[
    'Female infants',
    'Female children',
    'Female adolescents',
    'Female adults',
    'Female elderly',
    'Male infants',
    'Male children',
    'Male adolescents',
    'Male adults',
    'Male elderly']

# Data subset to display proportion of most vulnerable individuals:
vul = [subset[columns[:8]].values.sum()+subset[columns[9]].values.sum(),subset[columns[8]].values.sum()]

# Data subset to display proportion of children:
age_groups=[subset[columns[:3]].values.sum(),subset[columns[3:5]].values.sum(),subset[columns[5:8]].values.sum(),subset[columns[8:]].values.sum()]

# Labels for "children" subset:
childLbl=["Female children","","Male children",""]


# Color palette for the inner doughnut:
cs=[
    "lavenderblush",
    "mistyrose",
    "pink",
    "lightcoral",
    "palevioletred",
    "azure",
    "lightcyan",
    "paleturquoise",
    "powderblue",
    "lightskyblue"]

# Preparing the plot:
fig1, ax1 = plt.subplots()
ax1.axis('equal')

# Outer doughnut:
mypie1, _ , autotexts = ax1.pie(vul,radius=2.6,autopct='%1.1f%%', labels=["Most vulnerable",""], colors=['firebrick','none'], startangle=-2.9, pctdistance=0.92)
plt.setp( mypie1, width=0.4, edgecolor='white')
autotexts[0].set_color('white')
autotexts[1].set_color('none')

# Inner doughnut:
mypie2, _ , _ = ax1.pie(sizes, radius=2.2-0.6,colors=cs, autopct='%1.1f%%', pctdistance=0.8)
plt.setp(mypie2, width=0.7, edgecolor='white')

# Mid doughnut:
mypie3, _  = ax1.pie(age_groups, labels=childLbl, labeldistance=0.9, radius=2.5-0.6, colors=['grey','none','grey','none'])
plt.setp(mypie3, width=0.2, edgecolor='white')

# Legend:
ax1.legend(mypie2, labels, loc="lower right", bbox_to_anchor=(1.6, 0, 0, 0))

# Display plot:
plt.show()

# Save plot as JPEG: 
fig1.savefig('output.jpg',bbox_inches='tight')
