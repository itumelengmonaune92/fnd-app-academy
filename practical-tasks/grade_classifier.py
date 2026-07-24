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
subjects['Math   '] = float(input("Enter total marks for Math: "))
subjects['Science'] = float(input("Enter total marks for Science: "))
subjects['CompSci'] = float(input("Enter total marks for CompSci: "))

total_average = sum(subjects.values()) / len(subjects)
# Display Student name and report card details
print()
print("=" * 45)
print("STUDENT REPORT CARD - BSc IT (1st Year)")
print(f"Student Name: {student_name}")
print("=" * 45)

# Display student total average and marks for all subjects
print(f"Total average: {total_average:.2f}%")
print("=" * 45)
for subject, marks in subjects.items():
    if marks >= 80:
        print(f"{subject}: A ({marks}%)")
    elif marks >= 70:
        print(f"{subject}: B ({marks}%)")
    elif marks >= 60:
        print(f"{subject}: C ({marks}%)")
    elif marks >= 50:
        print(f"{subject}: D ({marks}%)")
    else:
        intervene = f"{subject}: F ({marks}%)"
        if marks < 40:
            print(f"{intervene} -> (Needs Intervention)")
        else:
            print(f"{subject}: F ({marks}%)")

print("=" * 45)
# Determine student status
if total_average >= 50:
    status = "Pass"
    print(f"Status : {status}")
else:
    status = "Fail"
    print(f"Status : {status}")
print("=" * 45)
print()