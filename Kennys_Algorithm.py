# This is a Python Dictionary that contains all of the students in Kenny's class as well as their grades.
student_grades = {"Jeremy" : 87,
 "Kyla" : 82,
 "Ayesha" : 90,
 "Aleida" : 94,
 "Todd" : 79,
 "Maxwell" : 98,
 "Yolonda" : 81,
 "Kiyoko" : 71,
 "Dagmar" : 73,
 "Laura" : 91,
 "Shimeah" : 81,
 "Songqiao" : 92,
 "Frankie" : 87,
 "Natalia" : 95,
 "Gonzalo" : 82,
 "Pavel" : 78

 }
# these are ALL the grades of ALL STUDENTS 
# step 1 -  creating a list of students who are not paired yet which are unpaired students



# This is a function that determines the student with the highest grade given a dictionary
def highest_grade(grades): 
	top_of_class = list(grades.keys())[0]
	for student_a in grades:
		for student_b in grades:
			if (grades[student_a] > grades[student_b]) and (grades[student_a] > grades[top_of_class]):
				top_of_class = student_a
			elif (grades[student_b] > grades[student_a]) and (grades[student_b] > grades[top_of_class]):
				top_of_class = student_b
	return top_of_class
# this is a customized built function to churn out the top scores among ALL students
# step 3 -until list of paired students in list "student grades" is empty, following steps will be repeated 
# 4. Determines student with highest grade



# This is a function that determines the student with the lowest grade given a dictionary
def lowest_grade(grades):
	bottom_of_class = list(grades.keys())[0]
	for student_a in grades:
		for student_b in grades:
			if (grades[student_a] < grades[student_b]) and (grades[student_a] < grades[bottom_of_class]):
				bottom_of_class = student_a
			elif (grades[student_b] < grades[student_a]) and (grades[student_b] < grades[bottom_of_class]):
				bottom_of_class = student_b
	return bottom_of_class
# step 3 -until list of paired students in list "student grades" is empty, following steps will be repeated 
# 5.  Determine student with lowest grade 



# This is Kenny's Algorithm! It sorts the students into pairs based on their grades.
def kennys_algorithm(grade_dict): 
	student_pairs = []
	while len(grade_dict) > 0:
		student_pairs.append([highest_grade(grade_dict), lowest_grade(grade_dict)]) # list of paired students -- step 6 is applied here 
		grade_dict.pop(highest_grade(grade_dict)) # STEP 7 IS APPLIED HERE
		grade_dict.pop(lowest_grade(grade_dict)) # STEP 7 IS APPLIED HERE
	print(student_pairs)

# STEP 2 - this is the so called empty list of paired students that will be sorted into here 





# Paste the code below!
kennys_algorithm(student_grades)

# 8. list of paried students is printed 