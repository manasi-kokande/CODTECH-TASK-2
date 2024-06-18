# Initialize an empty dictionary to store student information
students = {}

def add_student(name):
    """Add a new student to the tracker."""
    students[name] = []

def add_grade(name, grade):
    """Add a grade to a student's record."""
    if name in students:
        students[name].append(grade)
    else:
        print(f"Student '{name}' not found.")

def calculate_average(name):
    """Calculate the average grade of a student."""
    if name in students:
        grades = students[name]
        if len(grades) > 0:
            average_grade = sum(grades) / len(grades)
            return average_grade
        else:
            print(f"No grades found for student '{name}'.")
            return 0
    else:
        print(f"Student '{name}' not found.")
        return None

def display_student_info(name):
    """Display all information for a student."""
    if name in students:
        grades = students[name]
        average_grade = calculate_average(name)
        print(f"Student: {name}")
        print("Grades:", grades)
        print(f"Average grade: {average_grade}")
    else:
        print(f"Student '{name}' not found.")

# Example usage:
add_student("Alice")
add_grade("Alice", 85)
add_grade("Alice", 90)
add_grade("Alice", 75)

add_student("Bob")
add_grade("Bob", 70)
add_grade("Bob", 65)
add_grade("Bob", 80)

# Displaying information for Alice and Bob
display_student_info("Alice")
print()
display_student_info("Bob")
print()

# Adding a grade for Alice
add_grade("Alice", 95)
display_student_info("Alice")
