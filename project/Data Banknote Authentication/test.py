import numpy as np
from sklearn.preprocessing import Imputer

np.set_printoptions(threshold='nan')
f = open('breast-cancer-wisconsin.data', 'r')
data = []
answer = []
for line in f:
        line = line.replace("?","NaN");
        line = line.replace("\n","");
        data.append( [  float(n) for n in line.split(",")[1:10]]);
        answer.append(line.split(",")[-1:][0])
        

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
nparray = np.array(data)
imp.fit(nparray)
nparray_new = imp.transform(nparray)

data_rows, data_cols = nparray_new.shape
train_range = int(0.8*data_rows)

train_set_X = nparray_new[0:train_range]
train_set_y = answer[0:train_range]

test_set_X = nparray_new[train_range:]
test_set_y = answer[train_range:]

#Finished reading the data ... 
#need to train on train_imp data

from sklearn.svm import SVC
model = SVC()
model.fit(train_set_X,train_set_y)

y_pred = model.predict(test_set_X)

from sklearn.metrics import confusion_matrix
print "Confusion matrix:"
print(confusion_matrix(test_set_y, y_pred))

from sklearn.metrics import accuracy_score
print "Accuracy: " + str(accuracy_score(test_set_y, y_pred))
