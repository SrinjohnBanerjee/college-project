import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn import metrics 
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv(r'D:\srinjohn_phishing\output_dataframe.csv')

data

	URL	Label	havingAT	dash	urgentwords	depthhave	numbersinurl	platform_abuse	brandsubdirectory	tld	typo	ipinurl	httpinurl	class
0	nobell.it/70ffb52d079109dca5664cce6f317373782/...	bad	0	10	0	8	20	0	0	40	0	0	20	90
1	www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrc...	bad	0	10	0	4	20	0	20	0	0	0	20	70
2	serviciosbys.com/paypal.cgi.bin.get-into.herf....	bad	0	10	0	10	20	0	20	0	0	0	20	70
3	mail.printakid.com/www.online.americanexpress....	bad	0	0	0	2	0	0	20	0	0	0	20	40
4	thewhiskeydregs.com/wp-content/themes/widescre...	bad	0	10	0	6	20	0	0	0	0	0	20	50
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
549341	23.227.196.215/	bad	0	0	0	1	20	0	0	40	0	0	20	80
549342	apple-checker.org/	bad	0	10	0	1	0	0	20	0	0	0	20	50
549343	apple-iclods.org/	bad	0	10	0	1	0	0	20	0	0	0	20	50
549344	apple-uptoday.org/	bad	0	10	0	1	

data = data.drop(['Label'],axis = 1)
data = data.drop(['URL'],axis = 1)

plt.figure(figsize=(15,15))
sns.heatmap(data.corr(), annot=True)
plt.show()

data=data
df = data[['havingAT', 'dash', 'urgentwords','platform_abuse','brandsubdirectory','tld','typo','class']]
sns.pairplot(data = df,hue="class",corner=True);

data['class'].value_counts().plot(kind='pie',autopct='%1.2f%%')
plt.title("Phishing Count")
plt.show()

X = data.drop(["class"],axis =1)
y = data["class"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
X_train.shape, y_train.shape, X_test.shape, y_test.shape

from sklearn.linear_model import LogisticRegression
#from sklearn.pipeline import Pipeline

# instantiate the model
log = LogisticRegression()

# fit the model 
logimodel=log.fit(X_train,y_train)

y_train_log=logimodel.predict(X_train)
y_test_log=logimodel.predict(X_test)

import pickle
pickle.dump(logimodel,open('logistic_regression.pkl', 'wb'))

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
kneig=knn.fit(X_train,y_train)

y_train_knn = kneig.predict(X_train)
y_test_knn = kneig.predict(X_test)

pickle.dump(kneig,open('kneighbour.pkl','wb'))
