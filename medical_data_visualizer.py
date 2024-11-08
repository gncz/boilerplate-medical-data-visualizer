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
sns.catplot( data= df, x= "sex", y= "height")



df.info()

def draw_cat_plot():
    # 5
    vals = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    ids = ["id", "age", "sex", "height", "weight", "ap_hi", "ap_lo", 'cardio']
    df_cat = pd.melt(df, 
                     id_vars = 'cardio', 
                     value_vars = vals)


    # 6
    df_cat = df_cat.groupby(["cardio", "variable"]).count()
    df_cat = df_cat.reset_index()
    
    # 7
    df_cat["value"] = pd.to_numeric(df_cat["value"] )

    # 8
    fig = sns.catplot(data = df_cat, 
                      x = "variable", 
                      y = "value",
                      hue = "cardio", 
                      kind= "bar")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[ (df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df.weight <= df.weight.quantile(0.975)) & (df.weight >= df.weight.quantile(0.025)) & ( df.height <= df.height.quantile(0.975)) ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()