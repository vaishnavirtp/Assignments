def CreateTextFile():
    
    fileName = "assign.txt"
    with open(fileName,"w") as file:
            name = str(input("Enter name to save in a file: "))    
            file.write(name)
    file = open(fileName, "r")
    for line in file:
                print("File Output: ")
                print(line)
        
    try: 
        Newfile = "file.txt"
        with open(Newfile) as f:
            f.read()
    except FileNotFoundError:
        print("No such file name "+Newfile+ " exists")

CreateTextFile()