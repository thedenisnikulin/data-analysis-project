import csv
import numpy
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

# prepare data
with open('coefs.csv', newline='') as csvfile:
    target = list(csv.reader(csvfile))
    target = [float(target[t][0]) for t in range(len(target))]
    target = numpy.array(target)

with open('users_cash.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
    for d in range(len(data)):
        for nested_d in range(len(data[d])):
            data[d][nested_d] = int(float(data[d][nested_d]))
    data = numpy.array(data)
    

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)
yy = preprocessing.LabelEncoder().fit_transform(y_train)
knn = RandomForestClassifier(n_estimators=200)
knn.fit(X_train, yy)

# X_new = numpy.array([input('users: '), input('cash: ')])

y_pred = knn.predict(X_test)
print(y_pred)
print(y_test)
print(X_test)
print('правильность: {:.2f}'.format(numpy.mean(y_pred < y_test)))

plt.show(plt.plot(target))
plt.show(plt.plot([data[i][0] for i in range(len(data))]))
plt.show(plt.plot([data[i][1] for i in range(len(data))]))