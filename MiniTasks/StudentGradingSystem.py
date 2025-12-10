def continueGrading():
    while True:
        choice = input("Continue grading? (y/n): ")
        choice = choice.lower()

        if choice == "y":
            return True
        elif choice ==  "n":
            return False
        else:
            print("Invalid input!")

class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def add_grades(self, grade_list):
        return sum(grade_list)
    
    def calculate_average(self, grade_sum, subject_list):
        average = grade_sum / len(subject_list)
        return round(average, 2)
    
    def display_info(self, average, grade_letter):
        return f"Name: {self.name}\nID: {self.ID}\nAverage: {average}\nGrade Letter: {grade_letter}\n"
    
    def get_grade_letter(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    
if __name__ == "__main__":
    while True:
        print("STUDENT GRADING SYSTEM\n")
        name = input("Student Name: ")

        while True:
            try:
                ID = int(input("Student ID: "))
                break
            except ValueError:
                print("Invalid Input!")

        student = Student(name, ID)

        print("\nSUBJECT GRADE LIST")
        subject_list = ["1st", "2nd", "3rd"]
        grade_list = []

        for subject in subject_list:
            while True:
                try:
                    grade = float(input(f"Enter {subject} subject grade: "))
                    if grade < 0 or grade > 100:
                        print("Invalid Input! 0-100 only!")
                        continue

                    grade_list.append(grade)
                    break
                except ValueError:
                    print("Invalid Input!")

        grade_sum = student.add_grades(grade_list)

        average = student.calculate_average(grade_sum, subject_list)

        grade_letter = student.get_grade_letter(average)

        print("\nSTUDENT GRADING")
        print(student.display_info(average, grade_letter))

        if continueGrading():
            print("")
            continue
        else:
            print("Thank you and come again!")
            break



