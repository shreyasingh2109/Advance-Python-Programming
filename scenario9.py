class Course:
    def __init__(self, name, duration, fee, category):
        self.name = name
        self.duration = duration
        self.fee = fee
        self.category = category


class Institute:
    def __init__(self):
        self.course_list = []

    def add_course(self):
        name = input("Enter Course Name: ")
        duration = input("Enter Course Duration: ")
        fee = float(input("Enter Course Fee: "))
        category = input("Enter Course Category (Short-Term/Long-Term): ")

        c = Course(name, duration, fee, category)
        self.course_list.append(c)

        print("Course Added Successfully")

    def display_courses(self):
        if len(self.course_list) == 0:
            print("No Course Available")
        else:
            print("\nCourse Details")
            print("------------------------------------------------------------")
            print("Course Name\tDuration\tFee\tCategory")
            print("------------------------------------------------------------")

            for c in self.course_list:
                print(c.name, "\t", c.duration, "\t", c.fee, "\t", c.category)


obj = Institute()

while True:
    print("\nCourse Management System")
    print("1. Add Course")
    print("2. Display All Courses")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        obj.add_course()

    elif choice == 2:
        obj.display_courses()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")