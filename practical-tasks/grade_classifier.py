"""
Build a student grade classifier called grade_classifier.py 
that takes a learner’s name and marks for three subjects, 
calculates an average, assigns a grade and a status (Pass/Fail), 
and displays a full report card. The program must correctly 
use conditionals for all grade and status logic.
"""

subjects = {}
# Request student data from user
student_name = input("Enter student name: ").title()
subjects['Math'] = float(input("Enter total marks for Math: "))
subjects['Science'] = float(input("Enter total marks for Science: "))
subjects['CompSci'] = float(input("Enter total marks for CompSci: "))

total_average = sum(subjects.values()) / len(subjects)
print(total_average)



for subject in subjects.values():
    if subject >= 80:
        print("A")
    elif subject >= 70 and subjects <=79:
        print("B")
    elif subject >= 60 and subjects <=69:
        print("C")
    elif subject >= 50 and subjects <=59:
            print("D")
    else:
         print("F")

if total_average >= 50:
    print("Pass")
else:
    print("Fail")