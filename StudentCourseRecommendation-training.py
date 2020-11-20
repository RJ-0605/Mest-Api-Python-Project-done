import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from joblib import dump, load

features = pd.read_csv('StudentsPerformance2.csv')



# hash these definitions before running app

# Gender -> 1 - female, 2 - male
# race/ethnicity -> 1 - Group A, 2 - Group B, 3 - Group C, 4 - Group D, 5 - Group E
# level of education -> 0 - some high school, 1 - high school, 2 - some college, 3 - associate's degree, 4 - bachelor's degree, 5 - master's degree
# account type -> 0- free/reduced, 1 - standard
# course -> 1 - 50

#   the score is gotten from csv when trainnig and
#   used as the labels for final expected output when trainning 
#    score -> derrived variable

# end of hashing the definitions 

# print(features.head(5))
labels = features['math_score'] + features['reading_score'] + features['writing_score']


features = features.drop(['test_preparation_course', 'math_score', 'reading_score', 'writing_score'], axis = 1)
print(features)

# print(features['score'])
# feature_list = list(features.columns)
# print(feature_list)
features = np.array(features)
# exit()
# print(features.shape)


# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

##############################################################
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 200, random_state = 42)

# Train the model on training data
rf.fit(train_features, train_labels)
dump(rf, 'dumped_model.joblib')

#############################################################
# rf = load('dumped_model.joblib')
#############################################################

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)

# predictions = rf.predict([[1, 2, 4, 1]])
# print(predictions//3)
# Calculate the absolute errors
errors = abs(predictions - test_labels)

# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
