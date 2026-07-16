"""
Compound Boolean Expression are used to show if two or more condition are TRUE or 
FALSE if at least one condition is FALSE

Use compound boolean to write a simple program to grade students 
with score.

Grading system:
F -> Fail       (0 -39)
E -> Pass       (40 -49)
C -> Good       (50 -59)
B -> Very Good  (60 -69)
A -> Excellent  (70 -100)

"""
# Use Boolean short-circuit routing Evaluation (inline conditional assignment)
student_score = int(input("Enter student score: "))

results =   (student_score >= 70 and student_score <=100 and f" Total score = {student_score}: A -> Excellent!")\
        or  (student_score >=60 and student_score <=69 and f"Total score = {student_score}: B -> Very Good!")\
        or  (student_score >=50 and student_score <=59 and f"C -> Good: Total score = {student_score}: C -> Good")\
        or  (student_score >=40 and student_score <=49 and f"Total score = {student_score }: E -> Pass")\
        or  (student_score >= 0 and student_score <=39 and f"Total score = {student_score}: F -> Fail") 

print(results)
            