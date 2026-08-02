class Patient:
    def __init__(self, pid, name, category, cost):
        self.pid = pid
        self.name = name
        self.category = category
        self.cost = cost


class Hospital:
    def __init__(self):
        self.patient_list = []

    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        category = input("Enter Category (General/Special): ")
        cost = float(input("Enter Treatment Cost: "))

        p = Patient(pid, name, category, cost)
        self.patient_list.append(p)

        print("Patient Added Successfully")

    def display_records(self):
        if len(self.patient_list) == 0:
            print("No Records Found")
        else:
            print("\nPatient Records")
            print("-----------------------------------------------")
            print("ID\tName\t\tCategory\tCost")
            print("-----------------------------------------------")

            for p in self.patient_list:
                print(p.pid, "\t", p.name, "\t\t", p.category, "\t\t", p.cost)


h = Hospital()

while True:
    print("\nHospital Patient Management System")
    print("1. Add Patient")
    print("2. Display Records")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        h.add_patient()

    elif ch == 2:
        h.display_records()

    elif ch == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")