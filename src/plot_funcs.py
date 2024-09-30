# ----- Plots for Financial History -----
# Creating plots to display financial history
# --------------------------------

import os
import sys
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10') 

import pandas as pd
import numpy as np
sys.path.append("../")

import src
from src.Additional_funcs import check_file


def PlotFunc(in_doc):
    path = os.path.abspath(os.getcwd()) # path to directory of script
    
    # ----- Input File -----
    in_doc = str(path) + "/" + in_doc # path to bank statement (input file)
    empty_file = check_file(in_doc,"xlsx")
    
    if empty_file == 1:
        print("Error: input statement,",in_doc,", is empty")
        exit()

    df = pd.read_excel(in_doc) # dateframe of financial overview

    # ----- Balance History -----
    print(df[df.columns[1:3]])

    fig1, ax1 = plt.subplots()
    x_vals = df[df.columns[1]]
    y_vals = df[df.columns[2]]
    ax1.plot(x_vals,y_vals)

    ax1.set_title("Balance over time")

    ax1.set_xlabel("Date")
    ax1.set_xticklabels(ax1.get_xticklabels(),rotation=45)

    ax1.set_ylabel("Balance")

    fig1.savefig("balance_plt.jpg",bbox_inches="tight")

    # ----- Categories Pie Chart -----
    print(df[df.columns[4:]])

    print(df.columns[4:])
    print(df[df.columns[4:]].sum())

    fig2, ax2 = plt.subplots()
    ax2.pie(df[df.columns[4:]].sum(),labels=df.columns[4:])
    
    ax2.legend(title="Category",loc="lower right", bbox_to_anchor=(0.2, 0.8))

    fig2.savefig("pie_plt.jpg",bbox_inches="tight")

    return 0