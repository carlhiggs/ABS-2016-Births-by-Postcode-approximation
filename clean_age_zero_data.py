# Carl Higgs, 28 April 2023
# Cleaning persons aged zero by postcode dataset
# Evaluating if this is a fair approximation for births by postcode
# by evaluating similarity with Queensland birth by mothers postcode data


import pandas as pd
import matplotlib.pyplot as plt

# import data (prepared using ABS Table Builder Pro on 28 April 2023)
# probably could get this data from an official release, but on this occasion
# The table was prepared for POA (UR) rows (thats postal codes for 2016 and State, eg "7250, TAS")
# with columns of persons aged zero (Age==0) by place of usual residence
# under the assumption that this is approximately equivalent to 'birth by postcode' or by "mother's postcode".
file = 'data/ABS 2016 Census TableBuilder - Counting Persons, Place of Usual Residence (MB) - Age Zero by Postcode.csv'


# unnecessary header and footer rows are skipped, and only first two columns are retained
df = pd.read_csv(file, header=7, skipfooter=11,usecols=[0,1], engine='python',index_col=False,names=['POA_2016, State','Age==0'])

# ensure the "postcode, state" column is consistently formatted with seperation as ', '
df['POA_2016, State'] = df['POA_2016, State'].str.replace(' crosses ',', ')

# split postcode and state
df[['POA_2016', 'State']] = df['POA_2016, State'].str.split(', ', expand=True)

# restrict to useful columns
df = df[['POA_2016','State','Age==0']]

# cast data to int64
df = df.astype(
    {
    'POA_2016': 'int64',
    'State': 'object',
    'Age==0': 'int64',
    }
)

# save cleaned data
df.to_csv(file.replace('.csv',' - cleaned.csv'))

## Simple validation analysis
# Using births by mothers postcode data
# https://www.data.qld.gov.au/dataset/610e7ac0-ba60-4c67-8e99-7c57f3659f6a/resource/4abc0175-7f8c-49d1-b997-765267539af6/download/20170119_bdm_births-by-mothers-postcode-2016.csv

births = pd.read_csv('data/QLD - 20170119_bdm_births-by-mothers-postcode-2016.csv')

# join datasets on postcode, and restrict to Queensland postcodes for fair comparison
# (as some queensland births were to mothers in other states, but those are not full counts for those locations)
comparison = pd.concat([df.set_index('POA_2016'),births.set_index('Postcode')],axis=1)\
    .query('State=="QLD"')
    
comparison.plot.scatter(y='Transactions',x='Age==0')

comparison.corr()
#                  Age==0  Transactions
# Age==0        1.000000      0.996237
# Transactions  0.996237      1.000000
