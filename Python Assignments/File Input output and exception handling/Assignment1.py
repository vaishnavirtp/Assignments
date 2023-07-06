def ReadFile():
    count = 0
    with open("students.csv","r") as file:
        count = len(file.readlines())
    print(count)

ReadFile()