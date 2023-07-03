##11print("Welcome in our dance academy")

class DanceAcademy:
    def __init__(self):
        self.classes = []

    def add_class(self, dance_class):
        self.classes.append(dance_class)

    def get_classes(self):
        return self.classes

    def enroll_student(self, dance_class, student_name):
        dance_class.add_student(student_name)

    def display_menu(self):
        print("Welcome to the Dance Academy!")
        print("1. View available classes")
        print("2. Enroll for a class")
        print("3. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_available_classes()
            elif choice == "2":
                self.enroll_for_class()
            elif choice == "3":
                print("Thank you for using Dance Academy. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_available_classes(self):
        print("Available classes:")
        for dance_class in self.classes:
            print(f"- {dance_class.name} ({dance_class.level})")

    def enroll_for_class(self):
        self.view_available_classes()
        class_name = input("Enter the name of the class you want to enroll in: ")
        student_name = input("Enter your name: ")

        for dance_class in self.classes:
            if dance_class.name.lower() == class_name.lower():
                self.enroll_student(dance_class, student_name)
                print(f"Enrolled {student_name} in {dance_class.name}.")
                return

        print("Invalid class name. Please try again.")


class DanceClass:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)


# Creating dance academy instance
dance_academy = DanceAcademy()

# Creating dance classes
dance_class1 = DanceClass("Ballet", "Beginner")
dance_class2 = DanceClass("Hip Hop", "Intermediate")
dance_class3 = DanceClass("Contemporary", "Advanced")

# Adding dance classes to the academy
dance_academy.add_class(dance_class1)
dance_academy.add_class(dance_class2)
dance_academy.add_class(dance_class3)

# Running the dance academy program
dance_academy.run()


