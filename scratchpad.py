



	#################################
	
	second_combi = second_data[0]
	
	print (second_combi)
	print (data[1][1])
	second_combi.append(second_data[1][1])
	print (second_combi)
	second_predictions = rf.predict([second_combi])
	
	# form new array embed the result from first combination into it 
	# and also the subject id so we can easily identify and pick for display
	
	# Print prediction
	print("              ")
	print("              ")
	print("HERE IS OUR PREDICTIONS OVER 300 percent")
	print(second_predictions)
	print("HERE IS OUR PREDICTIONS devided by 300")
	
	second_pred = (second_predictions//3)
	second_pred = second_pred.tolist()
	print(second_pred)
	
	
	second_pred.append(data[1][1])
	
	
	#####################################
	
	
	##########################################
	
	third_combi = data[0]
	
	print (third_combi)
	print (data[1][2])
	third_combi.append(data[1][2])
	print (third_combi)
	third_predictions = rf.predict([third_combi])
	
	# form new array embed the result from first combination into it 
	# and also the subject id so we can easily identify and pick for display
	
	# Print prediction
	print("              ")
	print("              ")
	print("HERE IS OUR PREDICTIONS OVER 300 percent")
	print(third_predictions)
	print("HERE IS OUR PREDICTIONS devided by 300")
	
	third_pred = (third_predictions//3)
	third_pred = third_pred.tolist()
	print(third_pred)
	
	
	third_pred.append(data[1][2])
	
	
	
	#####################################
	
	###   first line 
	
	########################################
	
	
	
	
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
	
	top_courses = []
	course_count = 3 
	for k in range(course_count):
		temp_course = course_predictions[0][0]
		for course in course_predictions:
			if course[1] > temp_course and course[0] not in top_courses:
				temp_course = course[0]
		top_courses.append(temp_course)			
	
	print("top_courses")
	print(top_courses)
	

	return json.dumps(top_courses), 200, {'ContentType':'application/json'}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
