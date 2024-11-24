import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv", header = 0)


# 2
df['overweight'] = df.apply(lambda x: 1 if x['weight'] / ( (x['height']/100) ** 2) > 25 else 0, axis = 1)


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
                     id_vars = ('id','cardio'), 
                     value_vars = vals)


    # 6
    df_cat = df_cat.groupby(["cardio", "variable","value"]).count()
    df_cat = df_cat.reset_index()
    
    # 7
    df_cat.rename(columns = {'id':'counts'}, inplace=True )
    
    # 8
    fig = sns.catplot(data = df_cat, 
                      x = "variable", 
                      y = "counts",
                      hue = "value", 
                      col = "cardio",
                      kind= "bar")
    
    fig.savefig('catplot.png')
    
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[ (df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df.weight <= df.weight.quantile(0.975)) & (df.weight >= df.weight.quantile(0.025)) & ( df.height <= df.height.quantile(0.975)) ]

    # 12
    corr = df_heat.corr(method = 'pearson')

    # 13
    mask = np.triu(corr)


    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr[mask])

    # 16
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()