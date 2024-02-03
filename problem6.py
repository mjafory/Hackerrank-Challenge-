def gradingStudents(grades): 
    rounded_grades = []
    for i in grades:
        if i < 38 or i % 5 < 3:
            rounded_grades.append(i)
        else:
            rounded_grades.append(i + (5 - i % 5))

    return rounded_grades

while True:
    uservalue = int(input("Enter your value: "))
    result = gradingStudents([uservalue])
    print(result)
    exit = input("Type exit to quit this program: ")
    if exit == 'exit':
        break
    else:
        continue
