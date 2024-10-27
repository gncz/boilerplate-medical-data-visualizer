import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv", header = 0)

# 2
df['overweight'] = None

# 3
df["cholesterol"] = df["cholesterol"].astype(int)
df["gluc"] = df["gluc"].astype(int)


#data wrangling for gluc
df.loc[df["gluc"]==1, "gluc"] = 0  
df.loc[df["gluc"]> 1, "gluc"] = 1 

#data wrangling for cholesterol , experimenting with mapping
df["cholesterol"] = df['cholesterol'].map( lambda x:1 if x>1 else 0 )

# 4
def draw_cat_plot():
    # 5
    df_cat = sns.catplot( data= df, x= "sex", y= "height")


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
