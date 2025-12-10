def continueGrading(): #A helper function to check if the user wishes to continue using the program
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
        self.grades = [] #A grades list to store the grades inputted by the user
        self.average = 0 #A default average. It will be updated when calculating average
        self.grade_letter = "?" #A default grade letter. It will be updated when getting grade letter

    def add_grades(self, grade): #A method to append the user's input inside the grades list
        self.grades.append(grade)
    
    def calculate_average(self): #A method to calculate the average and updates the average attribute
        self.average = sum(self.grades) / len(self.grades)
    
    def display_info(self): #Returns the summary of the student, including the average and grade letter
        return f"Name: {self.name}\nID: {self.ID}\nAverage: {round(self.average, 2)}\nGrade Letter: {self.grade_letter}\n"
    
    def get_grade_letter(self): #Takes the average and checks the conditions on where it belongs
        if self.average >= 90:
            self.grade_letter = "A"
        elif self.average >= 80:
            self.grade_letter = "B"
        elif self.average >= 70:
            self.grade_letter = "C"
        elif self.average >= 60:
            self.grade_letter = "D"
        else:
            self.grade_letter = "F"
    
if __name__ == "__main__":
    while True: #Main loop for program looping
        print("STUDENT GRADING SYSTEM\n")
        name = input("Student Name: ")

        while True: #A loop to force the user to enter a valid ID
            try:
                ID = int(input("Student ID: "))
                break
            except ValueError:
                print("Invalid Input!")

        student = Student(name, ID) #Creates the object

        print("\nSUBJECT GRADE LIST")
        subject_list = ["1st", "2nd", "3rd"] #Default list of subjects

        for subject in subject_list: #Loops the whole subject list
            while True: #A loop to force the user to enter a valid grade.
                try:
                    grade = float(input(f"Enter {subject} subject grade: "))
                    if grade < 0 or grade > 100: #A conditional statement to invalidate negative numbers and input greater than 100
                        print("Invalid Input! 0-100 only!")
                        continue

                    student.add_grades(grade) #Usage of appending the grade input into the grades list
                    break
                except ValueError:
                    print("Invalid Input!")

        student.calculate_average() #Usage of calculating the grade average

        student.get_grade_letter() #Usage of getting the grade letter based on the average

        print("\nSTUDENT GRADING")
        print(student.display_info()) #Usage of displaying the student info

        if continueGrading(): #Usage of checking if the user wishes to continue grading or not
            print("")
            continue
        else:
            print("Thank you and come again!")
            break



