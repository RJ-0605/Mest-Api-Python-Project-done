

# for the AI part 
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from joblib import dump, load



# hash these definitions before running app

# Gender -> 1 - female, 2 - male
# race/ethnicity -> 1 - Group A, 2 - Group B, 3 - Group C, 4 - Group D, 5 - Group E
# level of education -> 0 - some high school, 1 - high school, 2 - some college, 3 - associate's degree, 4 - bachelor's degree, 5 - master's degree
# account type -> 0- free/reduced, 1 - standard
# course -> 1 - 50

#   the score is gotten from csv when trainnig and
#   used as the labels for final expected output when trainning 
# score -> derrived variable




# end of AI part 


from flask import Flask, Response ,json, request
app = Flask(__name__)


# this json can be exported to a json file and imported and read  

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})







@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
              <p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def readinternaljson():
    return json.dumps(data)

# this returns the response as a json format .
@app.route('/readjson', methods=['GET'])
def readjsonfile():
     
    with open('sample-python.json', 'r') as f:
    	info = json.loads(f.read())
    return json.dumps(info)
    
    
    
    
@app.route('/postjson', methods=[ 'POST'])
def recievejsonpost():
	data = request.get_json()
	print (data)
	# name = data.get('name', '')
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/postdatajson', methods=[ 'POST'])
def recievejsondatapost():
	data = request.get_json()
	
	print (data)
	# name = data.get('name', '')
	
#############################################################
	rf = load('dumped_model.joblib')
#############################################################

  

# Use the forest's predict method on the test data
# predictions = rf.predict(test_features)

	data.append(0)
	course_predictions = []
	for course in range(1,51):
		data[4] = course
		print(data)
		course_pred = [ course, rf.predict([data]) ]
		course_predictions.append(course_pred)
		print(course_predictions)
		
	top_courses = []
	course_count = 3 
	for k in range(course_count):
		temp_course = course_predictions[0][0]
		temp_pred = course_predictions[0][1]
		
		for course in course_predictions:
			if course[1] > temp_pred and course[0] not in top_courses:
				temp_pred = course[1]
				temp_course = course[0]
		top_courses.append(temp_course)			
	
	print("top_courses")
	print(top_courses)
	

	return json.dumps(top_courses), 200, {'ContentType':'application/json'}



    
@app.route('/writejson', methods=['GET', 'POST'])
def writejsonfile():
     
    with open('sample-write.json', 'w') as f:
    	info = json.dumps(f.write(b'{"text": "success"}' )); f.flush()
    return json.dumps(info)


if __name__ == '__main__':
    app.run(threaded=True, port=5001, debug=True, use_reloader=True)
