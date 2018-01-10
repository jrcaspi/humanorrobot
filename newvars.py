import pandas as pd
import numpy as np
bids = pd.read_csv("bids.csv")
train = pd.read_csv("train.csv")
bids_train = pd.merge(bids,train,on=['bidder_id'])

#get count of bids per bidder ID and save to training data
bids_per_bidder = bids_train.groupby(['bidder_id'])['bid_id'].count()
bids_per_bidder = bids_per_bidder.to_frame().reset_index()
bids_per_bidder.columns.values[0] = 'bidder_id'
bids_per_bidder.columns.values[1] = 'bid_count'
train2 = pd.merge(bids_per_bidder,train,on=['bidder_id'])  #saved to new file called train2


#unique countries per bidder
country_per_bidder = bids_train.groupby(['bidder_id'])['country'].nunique
country_per_bidder = country_per_bidder.to_frame().reset_index()
country_per_bidder.columns.values[0] = 'bidder_id'
country_per_bidder.columns.values[1] = 'country_cnt'
train2 = pd.merge(country_per_bidder,train2,on=['bidder_id'])


#getting rank of bids by bidder (bidder 1 bid 1, bidder 1 bid 2, etc.)
#next, create a key column to self join data to the next sequential bid for that bidder
#need to figure out why merge code is not working... once we have this we can take the time between each bid
#and save to a new file to get the average and min time between bids for each bidder 

bids_train['rank'] = bids_train.groupby('bidder_id')['time'].rank(ascending=True,method='dense')
bids_train2 = bids_train
bids_train2.drop('rank',axis=1,inplace=True)
bids_train2.columns.values[12] = 'rank'
bids_train_compare = pd.merge(bids_train,bids_train2,on=['bidder_id','rank'],how='left')

#merch_code is a numeric code for each category of merchandise
df.loc[(df.merchandise== 'jewelry'), 'merch_code'] = 1
df.loc[(df.merchandise== 'furniture'), 'merch_code'] = 2
df.loc[(df.merchandise== 'mobile'), 'merch_code'] = 3
df.loc[(df.merchandise== 'sporting goods'), 'merch_code'] = 4
df.loc[(df.merchandise== 'home goods'), 'merch_code'] = 5
df.loc[(df.merchandise== 'office equipment'), 'merch_code'] = 6
df.loc[(df.merchandise== 'computers'), 'merch_code'] = 7
df.loc[(df.merchandise== 'books and music'), 'merch_code'] = 8
df.loc[(df.merchandise== 'auto parts'), 'merch_code'] = 9
df.loc[(df.merchandise== 'clothing'), 'merch_code'] = 10

#For minimum_response_time and mean_response_time
df1 = merged.loc[:,['bidder_id','time']]
df1['diff'] = df1.sort_values(['bidder_id','time']).groupby('bidder_id')['time'].diff(-1)
df1['diff'] = df1['diff'] * -1
df1 = df1.dropna(how='any')
df1 = df1.groupby('bidder_id')['diff'].agg([('Min','min'),('Max','max')])
df1 = df1.groupby('bidder_id')['diff'].min()
df1.head()