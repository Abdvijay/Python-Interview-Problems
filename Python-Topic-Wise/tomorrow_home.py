class Course:
    user = {
        "vijay" : {
            "age" : 20,
            "place" : "Nellai",
            "course" : "Python",
            "degree" : ["bsc","mca"]
        },
        "anandh" : {
            "age" : 20,
            "place" : "coimbatore",
            "course" : "Java",
            "degree" : ["be"]
        }
    }

if __name__ == "__main__":
    obj = Course()
    flag = False
    stop = False
    while True:
        if stop:
            print(f"Thank you for visiting us :)")
            break

        try:
            name = input("Enter the name : ")
            for user_name in obj.user.keys():
                if user_name == name:
                    print(obj.user[name])
                    flag = True
            
        except ValueError as e:
            print(e)

        if flag:
             break
        else:
            print(f"Entered name is not in database so please enter valid name :)")
            stop_flag = input("Do you want check return (yes / no) : ").lower()
            if stop_flag == "yes":
                stop = False
            else:
                stop = True