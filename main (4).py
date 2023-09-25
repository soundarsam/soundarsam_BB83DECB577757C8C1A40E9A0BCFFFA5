class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of students in descending order of cgpa
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=true)
  # syntax - lambda arg:exp
  return sorted_students


# example usage:
students = [
    student("hari", "a123", 7.8),
    student("srikanth", "a124", 8.9),
    student("saumya", "a125", 9.1),
    student("mahidhar", "a126", 9.9),
]

sorted_students = sort_students(students)

# print the sorted list of students
for student in sorted_students:
  print("name: {}, roll number: {}, cgpa: {}".format(student.name,                                                  student.roll_number,                                                    student.cgpa)) 