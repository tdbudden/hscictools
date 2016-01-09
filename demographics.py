'''
Simple module to provide access to demographic data downloaded from

- https://apps.nhsbsa.nhs.uk/infosystems/home/homepage.do (guest login)


'''

from hscictools.refdata import refdata
import pandas as pd
import re

header='Regional Office Name,Regional Office Code,Area Team Name,Area Team Code,PCO Name,PCO Code,Practice Name,Practice Code,Male 0-4,Female 0-4,Male 5-14,Female 5-14,Male 15-24,Female 15-24,Male 25-34,Female 25-34,Male 35-44,Female 35-44,Male 45-54,Female 45-54,Male 55-64,Female 55-64,Male 65-74,Female 65-74,Male 75+,Female 75+'.split(',')

refdatadir='/'.join(refdata.__file__.split('/')[:-1])
with open(refdatadir+'/20151113_1447444074938_Patient_List_Size_Information.csv') as f:
  df_=pd.read_csv(f)
  df_['CCG ID']=df_['PCO Code'].apply(lambda x:x[:3])
  df_.set_index([col for col in df_.columns if not ('Male' in col or 'Female' in col)],inplace=True)
  df_.columns=pd.MultiIndex.from_tuples([tuple(col.split(' ')) for col in df_.columns],
                                        names=['Gender','Age Band'])

def by_CCG():
  pos=[i for i,x in enumerate(df_.index.names) if 'CCG' in x or 'PCO Name' in x] #position of CCG ID col
  return df_.groupby(level=pos).sum().sort_index(axis='columns')

def by_Practice():
  pos=[i for i,x in enumerate(df_.index.names) if 'Practice' in x or 'PCO Name' in x] #positions of practice cols
  return df_.groupby(level=pos).sum().sort_index(axis='columns')

def by_Nation():
  return df_.sum()

def gender_age_series(text):
  rows=list()
  for x in text.split('\n'):
    [a,m,f]=re.split('\s+',x)
    rows.append([a,float(m),float(f)])
  result=pd.DataFrame(rows,columns=['Age Band','Male','Female']).set_index('Age Band').stack()
  result.index=result.index.swaplevel(0,1)
  result.index.set_names(['gender','age'],inplace=True)
  return result


def astro_pu_cost_based():
  # Cost-based
  # ASTRO PU 2013   
  # Age Band  Male  Female
  text='''0-4 1.0 0.9
5-14  0.9 0.7
15-24 1.2 1.4
25-34 1.3 1.8
35-44 1.8 2.6
45-54 3.1 3.7
55-64 5.3 5.4
65-74 8.7 7.6
75+ 11.3  9.9'''
  return gender_age_series(text)
    
def astro_pu_item_based():    
  # Item-based    
  # ASTRO PU 2013   
  # Age Band  Male  Female
  text='''0-4 5.2 4.6
5-14 2.8 2.5
15-24 2.5 4.6
25-34 2.9 6.0
35-44 4.9 8.3
45-54 8.7 12.3
55-64 16.6  19.1
65-74 29.9  30.4
75+ 44.9  48.5'''
  return gender_age_series(text)


import matplotlib.pyplot as plt
from matplotlib import gridspec
import re

def normalise(df,baseline):
    result=baseline.join(df,lsuffix='_baseline')
    result.columns=['baseline','specific']
    total=result.sum()
    result['index']=result['specific']/total['specific']/result['baseline']*total['baseline']
    return result

def age_gender_tornado(df,figsize=(10,5),title='Age-Gender Tornado'):
    fig = plt.figure(figsize=figsize)
    fig.suptitle(title+"\n")
    gs = gridspec.GridSpec(1, 2, width_ratios=[1,1])
    axes=map(plt.subplot,gs)
    age_gender_tornado_(df,axes)

def age_gender_tornado_with_index(df,baseline,figsize=(15,6),indexlim=(0.4,2.5),title='Age-Gender Tornado'):
    fig = plt.figure(figsize=figsize)
    fig.suptitle(title+"\n")
    gs = gridspec.GridSpec(1, 3, width_ratios=[1,1,1])
    axes=map(plt.subplot,gs)
    age_gender_tornado_(df,axes)
    age_gender_index_(normalise(df,baseline),axes,indexlim=indexlim)

def age_gender_tornado_(df,axes):
    dfu=df.unstack(0) # unstack the gender values into columns
    dfu['Lowest Age']=dfu.index.map(lambda x: int(re.split('[-+]',x)[0]))
    dfu=dfu.sort(columns=['Lowest Age'])
    max_xlim=max(dfu['Female'].max(),dfu['Male'].max())
    female_subplot=dfu['Female'].plot(kind='barh',ax=axes[0],color='pink',alpha=0.8,xlim=(max_xlim,0))
    male_subplot=dfu['Male'].plot(kind='barh',ax=axes[1],color='mediumblue',alpha=0.8,xlim=(0,max_xlim))
    axes[0].set_xlabel('Females')
    axes[1].set_xlabel('Males')
    axes[1].set_ylabel('')
    axes[1].set_yticklabels(['' for item in axes[1].get_yticklabels()]) 
    for i in (0,1):
        for j in axes[i].xaxis.get_major_ticks():
            j.label.set_rotation(30)

def age_gender_index_(df,axes,indexlim):
    dfu=df['index'].unstack(0)
    dfu['Lowest Age']=dfu.index.map(lambda x: int(re.split('[-+]',x)[0]))
    dfu=dfu.sort(columns=['Lowest Age']).reset_index()
    dfu['Age Rank']=dfu.index
    dfu.plot(kind='scatter',alpha=1,marker='o',x='Male', y='Age Rank',s=300,c='mediumblue',ax=axes[2],
            ylim=(-0.5,len(dfu)-0.5),xlim=indexlim)
    dfu.plot(kind='scatter',alpha=0.6,marker='o',x='Female', y='Age Rank',s=300,c='pink',ax=axes[2])
    axes[2].set_ylabel('')
    axes[2].set_xlabel('index')
    axes[2].set_yticklabels(['' for item in axes[2].get_yticklabels()])
