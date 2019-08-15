############# Please! give credit when used	##############

import pandas as pd
from sklearn.model_selection import train_test_split # for spliting training and test data
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn import metrics # for calculating accuracy


#importing the dataset
dataset = pd.read_csv('data.csv')
# seprating columns
outlook = dataset.iloc[:, 0].values # all rows of column 1 of dataset
temperature = dataset.iloc[:, 1].values 
humidity = dataset.iloc[:, 2].values 
windy = dataset.iloc[:, 3].values 
play = dataset.iloc[:, 4].values # all rows of column 5 of dataset

# encoding string 
le = preprocessing.LabelEncoder()

encoded_outlook = le.fit_transform(outlook) # overcast = 0; rainy = 1, sunny = 2;
encoded_temperature = le.fit_transform(temperature) # cool = 0; hot = 1; mild = 2;
encoded_humidity = le.fit_transform(humidity) # high = 0; normal = 1;
encoded_windy = le.fit_transform(windy) # false = 0; true = 1;

# print(encoded_outlook)
# print(encoded_temperature)
# print(encoded_humidity)
# print(encoded_windy)


X = zip(encoded_outlook, encoded_temperature, encoded_humidity, encoded_windy)
features = []
for x in X:
	features.append(x)
# print(features)

target = le.fit_transform(play)
# print(target)

classifier = GaussianNB()

classifier.fit(features, target)

predicted = classifier.predict([(2,0,0,1)]) # [sunny,cool,high,true] 
# i.e can we play if outlook is sunny, temperature is cool, humidity is high and windy is true ?

print(predicted) # if predicted is 0 => No if 1 => Yes


# X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0) # 80% training and 20% test
# classifier.fit(X_train, y_train)
# y_pred = classifier.predict(X_test)
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))