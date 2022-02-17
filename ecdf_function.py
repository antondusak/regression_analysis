#!/usr/bin/env python
# coding: utf-8

# In[3]:

from numpy import *
import matplotlib.pyplot as plt

def ecdf(data):
    n=len(data)
    x=sort(data)
    y=arange(1, n+1) / n
    return x, y

def three_ecdf_chart(df_column_1, df_column_2, df_column_3):
    """This function will plot 3 ECDF function charts

    Parameters
    ----------
    column_1 (array): df[column_1]
    column_2 (array): df[column_2]
    column_3 (array): df[column_3]

    Returns
    -------
    2-Dimensional arrays plotted into an ECDF line
    """
    
    x_1, y_1 = ecdf(df_column_1)
    x_2, y_2 = ecdf(df_column_2)
    x_3, y_3 = ecdf(df_column_3)

    fig, axs = plt.subplots(1,3, figsize=(12,4))
    fig.suptitle("Empirical cumulative distribution functions for: ")

    #three ECDF plots
    axs[0].plot(x_1, y_1, color='slateblue')
    axs[0].set(xlabel=df_column_1.name, ylabel='Proportion of countries with a less than or equal x ')
    axs[0].grid()

    axs[1].plot(x_2, y_2, color="steelblue")
    axs[1].set(xlabel=df_column_2.name)
    axs[1].grid()

    axs[2].plot(x_3, y_3, color="peru")
    axs[2].set(xlabel=df_column_3.name)
    axs[2].grid()
    plt.show()

