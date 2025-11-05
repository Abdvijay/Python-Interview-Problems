class Besant_Technology:
    amount = 25000
    courses = {
        1: [
            "Python Full Stack",
            {1:"9AM - 10AM",2:"10AM - 11AM"}
        ],
        2: [
            "Java Full Stack",
            {1:"11AM - 12PM",2:"1PM - 2PM"}
        ],
        3: ["Data Analyst",
           {1:"8AM - 9AM",2:"6PM - 7PM",3:"7PM - 8PM"}
        ]
    }
    modes = ["offline", "online"]

    def __init__(self, name, course, mode):
        self.name = name
        self.course = course
        self.mode = mode

    def putdata(self):
        print("-" * 10 + " DETAILED BROCHURE " + "-" * 10)
        print(f"YOUR NAME      : {self.name.upper()}")
        print(f"CHOOSEN COURSE : {self.courses[self.course][0].upper()}")
        print(f"TIME SLOT      : {self.courses[self.course][1][self.slot]}")
        print(f"CHOSEN MODE    : {self.mode.upper()}")
        print(f"TOTAL AMOUNT   : ₹{self.amount}")
        print("")

    def display(self):
        print(
            f"\nThanks {self.name} for purchasing {self.courses[self.course][0].upper()} "
            f"in {self.mode.capitalize()} mode with an amount of ₹{self.amount}.\n"
        )
        self.putdata()

    def get_time_data(self,course):
        print("")
        self.course_num = course
        while True:
            print("-" * 20 + " Available Slots " + "-" * 20)
            for num,time_slot in self.courses[self.course_num][1].items():
                print(f"{num} : {time_slot}")
            try:
                self.slot = int(input("\nChoose the time slot in number : "))
                if self.slot > len(self.courses[self.course_num][1]) and self.slot != 0:
                    self.choosen_time_slot = self.courses[self.course_num][self.slot]
            except ValueError:
                print("❌ Invalid input! Please enter a number.\n")
                continue
            except IndexError:
                print("❌ Invalid input! Please choose a number within this slot.\n")
                continue
            break
        # return self.choosen_time_slot
        

def get_course_data():
    name = input("Enter your name: ").strip().title()
    print("")

    while True:
        print("-" * 20 + " Available Courses " + "-" * 20)
        for num, cr in Besant_Technology.courses.items():
            print(f"{num}. {cr[0]}")

        try:
            course = int(input("\nChoose one course among them (Enter number): "))
            if course not in Besant_Technology.courses:
                print("❌ Please choose a valid course number!\n")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")
            continue
        
        while True:
            mode = input("Choose mode (Online/Offline): ").strip().lower()
            if mode not in Besant_Technology.modes:
                print("❌ Please choose a valid mode (Online or Offline)!\n")
                continue
            break
        break

    return name, course, mode


if __name__ == "__main__":
    print("-" * 25 + " Welcome to Besant Technology " + "-" * 25)
    name, course, mode = get_course_data()
    user = Besant_Technology(name, course, mode)
    user.get_time_data(course)
    user.display()