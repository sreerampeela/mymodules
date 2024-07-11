# creating an attendance report for students

std_names = []
n_students = int(input("Enter number of students: "))
for i in range(n_students):
    name = input("Enter student name: ")
    std_names.append(name)
max_name = max(name for names in std_names)
max_char = len(max_name)
print(max_name)
std_names.sort()
print(std_names)
n_days = int(input("Enter number of working days: "))
final_attendance = [0] * n_students
for day in range(n_days):
    for std in std_names:
        attendance = input("Is {} present today? (P for present and A for absent): ".format(std))
        if attendance.lower() == "p":
            attendance_value = 1
        elif attendance.lower() == "a":
            attendance_value = 0
        else:
            print("Not a proper entry for {}".format(std))
        roll_no = std_names.index(std)
        final_attendance[roll_no] += attendance_value

print(final_attendance)
attendance_percent = []
for attend in final_attendance:
    atd_per = (attend / n_days) * 100
    attendance_percent.append(atd_per)

print(atd_per)
for std_out in std_names:
    roll = std_names.index(std_out) + 1
    atd_percent = round(attendance_percent[roll - 1], 2)
    output = str(roll) + " " + std_out + " " * (max_char - len(std_out) + 3) + str(atd_percent)
    print(output)
