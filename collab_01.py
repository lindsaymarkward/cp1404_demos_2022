"""
get number_of_gifts, number_of_students
number_of_gifts_per_student = number_of_gifts / number_of_students
number_of_gifts_leftover = number_of_gifts % number_of_students
print number_of_gifts_per_student, number_of_gifts_leftover
"""

starting_number_of_gifts = int(input("number_of_gifts: "))
number_of_students = int(input("number_of_students: "))
number_of_gifts_per_student = starting_number_of_gifts // number_of_students
number_of_gifts_leftover = starting_number_of_gifts % number_of_students
print(number_of_gifts_per_student, number_of_gifts_leftover)
