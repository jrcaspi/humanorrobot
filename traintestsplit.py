#defining the outcome variable as outcome
from sklearn import datasets
y = df1.loc[:,'outcome']
df1.dtypes

#Splitting the dataset into 70% train set and 30% test set. We also transform the data to avoid giving specific data more weight.
from sklearn.model_selection import train_test_split
X = df1.loc[:,['bidder_id_cat','auction_cat','merchandise_cat','device_cat','country_cat','ip_cat','url_cat','payment_account_cat','address_cat']]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
