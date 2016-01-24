'''
Simple module to provide access to practice names from the epraccur file here:

- http://systems.hscic.gov.uk/data/ods/datadownloads/gppractice/index_html


'''

from hscictools.refdata import refdata
import pandas as pd
import re
from collections import defaultdict

# header info is from pdf file in the dowloaded zip
header='''1 Organisation Code
2 Name 
3 National Grouping 
4 High Level Health Geography 
5 Address Line 1 
6 Address Line 2
7 Address Line 3
8 Address Line 4 
9 Address Line 5 
10  Postcode
11  Open Date 
12  Close Date
13  Status Code 
14  Organisation Sub- Type Code
15  Commissioner 
16  Join Provider/Purchaser Date
17  Left Provider/Purchaser Date 
18  Contact Telephone Number
19  Null
20  Null
21  Null
22  Amended Record Indicator 
23  Null
24  Provider/Purchaser 
25  Null
26  Prescribing Setting
27  Null '''.split('\n')

columns=list()
for x in header:
    i,ignore,col=x.partition(' ')
    col=col.strip()
    if col=='Null':
        col=i
    columns.append(col)

refdatadir='/'.join(refdata.__file__.split('/')[:-1])
with open(refdatadir+'/epraccur.csv') as f:
  df_=pd.read_csv(f,names=columns)
  df_.set_index('Organisation Code',inplace=True)

known_practices=set(df_.index)

def name(x):
  if x in known_practices:
    return "%s (%s); %s" % (df_.ix[x]['Name'],x,df_.ix[x]['Postcode'])
  else:
    return x

def ccg(x):
  if x in known_practices:
    return df_.ix[x]['Commissioner']

status_map=defaultdict(str)
for i in '''A = Active
B = Retired
C = Closed
D = Dormant 
P = Proposed'''.split('\n'):
    a,sep,b=i.partition(' = ')
    status_map[a]=b
def status(x):
  if x in known_practices:
    return status_map[df_.ix[x]['Status Code']]

setting_map=defaultdict(str)
for i in '''0 = Other
1 = WIC Practice
2 = OOH Practice
3 = WIC + OOH Practice
4 = GP Practice
8 = Public Health Service
9 = Community Health Service
10 = Hospital Service
11 = Optometry Service
12 = Urgent & Emergency Care
13 = Hospice
14 = Care Home / Nursing Home 15 = Border Force
16 = Young Offender Institution
17 = Secure Training Centre
18 = Secure Children's Home
19 = Immigration Removal Centre 20 = Court
21 = Police Custody
22 = Sexual Assault Referral Centre (SARC)
24 = Other - Justice Estate
25 = Prison'''.split('\n'):
    a,sep,b=i.partition(' = ')
    setting_map[int(a)]=b
def prescribing_setting(x):
  if x in known_practices:
    return setting_map[df_.ix[x]['Prescribing Setting']]

def active_gp_practices():
  return list(sorted(df_[(df_['Status Code']=='A') & (df_['Prescribing Setting']==4)].index))


