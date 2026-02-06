import json
import random
import time
USERNAME ="admin"
PASSWORD = "1234"
def login():
    attempts=0
    max_attempts=5
    while attempts < max_attempts:
        user = input("Enter username: ")
        pw = input("Enter password: ")

        if user == USERNAME and pw == PASSWORD:
            print("Welcome " + user + "!")
            return True
        else:
            attempts += 1
            print(f"Wrong username or password. Attempts left {max_attempts-attempts }")

    print("Wrong username or password. No Attempts left")
    print ("Locked for 60 seconds")

    time.sleep(60)
    return False

students = []
def generate_id ():
    while True:
        student_id = random.randint(1000,9999)
        if all(student.id!=student_id for student in students):
            return student_id


class Student:
    def __init__(self, name, age, grades,student_id,password):
        self.name = name
        self.age = age
        self.grades = grades
        self.id = student_id
        self.password = password

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def show_info(self):
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")
        print("------------------")

def save_student():
    data = []
    for student in students:
        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "grades": student.grades,
            "password": student.password
        })
    with open("Student.json", "w") as file:
        json.dump(data, file, indent=4)

def load_student():
    try:
        with open("Student.json", "r") as file:
            data = json.load(file)

            for item in data:
                students.append(Student(
                    name=item["name"],
                    age=item["age"],
                    grades=item["grades"],
                    student_id=item["id"],
                    password=item.get("password")
                ))
    except FileNotFoundError:
        pass

def add_student():

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    num_grades = int( input ("Enter how many grades:" ))
    grades = []
    for i in range(num_grades):
        grade = float(input(f"Grade {i+1}: "))
        grades.append(grade)
    password = input("Enter password: ")
    new_student = Student(name, age, grades,generate_id(),password)
    students.append(new_student)
    save_student()
    print(" Student added successfully!")

def show_students():
    if not students :
        print(" No students added ")
        return

    print(" Students List:")
    for student in students:
        student.show_info()


def search_student():
    student_id = int(input("Enter student ID to search: "))

    for student in students:
        if student.id == student_id:
            print(" Student Found")
            student.show_info()
            return

    print(" Student not found!")


def calculate_average():
    if not students:
        print(" No students added.")
        return

    print(" Students Averages:")
    for student in students:
        print(f"{student.name} (ID:{student.id}) Average = {student.get_average():.2f}")
    print()

def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    for student in students:
        if student.id == student_id:
            students.remove(student)
            save_student()
            print(" Student deleted!")
            return

    print(" Student not found!")

def update_student():
    student_id = int(input("Enter student ID to update: "))
    for student in students:
        if student.id == student_id:
            print(" Student found ,enter new data to update!")
            student.name = input("Enter new name: ")
            student.age = int(input("Enter new age: "))
            student.grades = []
            num_grades=int(input("Enter how many grades: "))
            for i in range(num_grades):
                grade = float(input(f"Grade {i+1}: "))
                student.grades.append(grade)
            save_student()
            print(" Student updated successfully!")
            return
    print(" Student not found!")

def show_highest_average():
    if not students:
        print(" No students added yet.")
        return
    highest_student=max(students, key=lambda student: student.get_average())
    print("Student with highest average is: ")
    highest_student.show_info()

def show_lowest_average():
    if not students:
        print(" No students added yet.")
        return
    lowest_student=min(students, key=lambda student: student.get_average())
    print("Student with lowest average is: ")
    lowest_student.show_info()

def sort_student():
    if not students:
        print(" No students added yet.")
        return

    choice = input(" Sort by average (1- Highest -> lowest , 2- Lowest -> highest)")
    if choice == "1":
        sorted_list = sorted(students, key=lambda s: student.get_average(),reverse=True)
        print(" Sorted from highest to lowest : ")
    elif choice == "2":
        sorted_list = sorted(students, key=lambda s: student.get_average())
        print("Sorted from lowest to highest :")
    else :
        print("Invalid choice!")
        return

    for student in sorted_list:
        print(f"{student.name} (ID:{student.id} -> Average: {student.get_average():.2f})")

def main_menu():
    load_student()

    while True:
        print("Welcome to Student Manager")
        print("1. Add Student")
        print("2. show Students")
        print("3. Search Student by ID")
        print("4. Calculate average")
        print("5. Delete Student")
        print("6. Update Student Data")
        print("7. Sort Students")
        print("8. Show highest average")
        print("9. Show lowest average")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()

        elif choice == 2:
            show_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            calculate_average()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            update_student()

        elif choice == 7:
            sort_student()

        elif choice == 8:
            show_highest_average()

        elif choice == 9:
            show_lowest_average()

        elif choice == 0:
            print("Thank you for using Student Manager")
            break
        else:
            print("Invalid Choice")

if login():
    print(" Login Successful")
    main_menu()
else:
    print(" Login Failed")