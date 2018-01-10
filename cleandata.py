import pandas as pd
import numpy as np
bids = pd.read_csv('bids.csv')
train = pd.read_csv('train.csv')
bids.head()
train.head()
get_ipython().magic('logstart projectcode.py')
import pandas as pd
import numpy as np
bids = pd.read_csv('bids.csv')
train = pd.read_csv('train.csv')
bids.head()
train.head()
merged = pd.merge(bids, train, on ='bidder_id')
merged.isnull().sum()
merged = merged.dropna(how='any')
merged.isnull().sum()
merged.to_csv('merged.csv')
len(np.unique(merged.bidder_id))

#getting the dataset model ready

df1 = merged
df1.head()
df1.dtypes
df1["bidder_id"]=df1["bidder_id"].astype("category")
df1["auction"]= df1["auction"].astype('category')
df1["merchandise"]= df1["merchandise"].astype('category')
df1["device"]= df1["device"].astype('category')
df1["country"]= df1["country"].astype('category')
df1["ip"]= df1["ip"].astype('category')
df1["url"]= df1["url"].astype('category')
df1["payment_account"]= df1["payment_account"].astype('category')
df1["address"]= df1["address"].astype('category')
df1["bidder_id_cat"] = df1["bidder_id"].cat.codes
df1["auction_cat"] = df1["auction"].cat.codes
df1["merchandise_cat"] = df1["merchandise"].cat.codes
df1["device_cat"] = df1["device"].cat.codes
df1["country_cat"] = df1["country"].cat.codes
df1["ip_cat"] = df1["ip"].cat.codes
df1["url_cat"] = df1["url"].cat.codes
df1["payment_account_cat"] = df1["payment_account"].cat.codes
df1["address_cat"] = df1["address"].cat.codes