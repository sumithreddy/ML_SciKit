import numpy as np
from sklearn.preprocessing import Imputer

np.set_printoptions(threshold='nan')
f = open('forestfires.csv', 'r')
data = []
answer = []
f.readline()
dictionary_month = {'': 0, 'mar': 3, 'feb': 2, 'aug': 8, 'sep': 9, 'apr': 4, 'jun': 6, 'jul': 7, 'jan': 1, 'may': 5, 'nov': 11, 'dec': 12, 'oct': 10}
for line in f:
        #line = line.replace("?","NaN");
        line = line.replace("\n","");
        #data.append( [  float(n) for n in line.split(",")[1:10]]);
	arr  = 	line.split(",")
	row =[]
	row.append(int(arr[0]))
	row.append(int(arr[1]))
	row.append(dictionary_month[arr[2]])
	#row.append(arr[3])
	row.append(float(arr[4]))
	row.append(float(arr[5]))
	row.append(float(arr[6]))
	row.append(float(arr[7]))
	row.append(float(arr[8]))
	row.append(float(arr[9]))
	row.append(float(arr[10]))
	row.append(float(arr[11]))
	answer.append(float(arr[12]))	
	data.append(row)
        

#imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
nparray = np.array(data)
#imp.fit(nparray)
#nparray_new = imp.transform(nparray)

from sklearn.cross_validation import train_test_split 
train_set_X, test_set_X, train_set_y, test_set_y = train_test_split(nparray, answer, test_size=0.2, random_state=42)

#Finished reading the data ... 
#need to train on train_imp data

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=False)


#from sklearn import linear_model
#model = linear_model.BayesianRidge()

#from sklearn import tree
#model = tree.DecisionTreeRegressor()

model.fit(train_set_X,train_set_y)

y_pred = model.predict(test_set_X)

from sklearn.metrics import mean_absolute_error
print "Mean Absolute Error :"
print(mean_absolute_error(test_set_y, y_pred))


