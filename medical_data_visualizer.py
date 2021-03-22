import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

BMI=df['weight']/((df['height'])/100)**2
df['overweight'] = BMI
df.loc[BMI>25, 'overweight']=1
df.loc[BMI<=25, 'overweight']=0

#print(df['overweight'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0.
#If the value is more than 1, make the value 1.
'''df.loc[df['cholesterol']==1,'cholesterol']=0
df.loc[df['cholesterol']>1,'cholesterol']=1
df.loc[df['gluc']==1,'gluc']=0
df.loc[df['gluc']>1,'gluc']=1'''

df['cholesterol']=np.where((df['cholesterol']<=1), 0, 1)
df['gluc']=np.where((df['gluc']<=1),0,1)


#print(df)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    df_cat= pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

# Group and reformat the data to split it by 'cardio'. Show the counts of each feature.

    print(df_cat)

#You will have to rename one of the collumns for the catplot to work correctly.
#df_cat = None

# Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(x='variable', col='cardio',palette='colorblind',data=df_cat, kind='count', hue='value')
    graph.set(xlabel='variable',ylabel='total')
    graph.set_xticklabels(['active','alco','cholesterol','gluc','overweight', 'smoke',])
    
    fig=graph.fig
    #plt.show()
#plt.figure().show()
#ax=fig.axes[0].legend()



# Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
# Clean the data

    """df_pressure = df[df['ap_lo']>df['ap_hi']].index
    df.drop(df_pressure, inplace=True)
#print(df)

    df_height=df[df['height']<df['height'].quantile(0.025)].index
    df.drop(df_height,inplace=True)
#print(df_height)
#print(df)

    df_height2=df[df['height']>df['height'].quantile(0.975)].index
    df.drop(df_height2, inplace=True)
#print(df_height2)
#print(df)

    df_weight=df[df['weight']<df['weight'].quantile(0.025)].index
    df.drop(df_weight, inplace=True)
#print(df_weight)
#print(df)

    df_weight2= df[df['weight']>df['weight'].quantile(0.975)].index
    df.drop(df_weight2, inplace=True)
#print(df_weight2)
#print(df)"""

    df_heat=df[(df['ap_lo']<=df['ap_hi'])
           & (df['height']>=df['height'].quantile(0.025)) & (df['height']<=df['height'].quantile(0.975))
           & (df['weight']>=df['weight'].quantile(0.025)) & (df['weight']<=df['weight'].quantile(0.975))]


    #df_heat=pd.DataFrame(df)

# Calculate the correlation matrix

    corr = (df_heat.corr()).round(1)

# Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
#plt.plot()
    fig, ax = plt.subplots(figsize=(10,8))

# Draw the heatmap with 'sns.heatmap()'

    f=sns.heatmap(corr, mask=mask, annot=True, vmax=.3, center=0, square=True, linewidths=.5, fmt='.1f')
    fig=f.get_figure()
    fig.show()
# Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig





