students = ["ram" , "shyam" , "kishan" , "shradha" , "radha"]

for student in students:
    if student == "shradha":
        break;
    print(student)

for student in students:
    if student == "kishan":
        continue;
    print(student)