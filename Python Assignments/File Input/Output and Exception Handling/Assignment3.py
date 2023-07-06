def average():
    Sum = 0
    marklist = []
    with open('students.csv', 'r') as f:
        for line in f.readlines():
            l = line.strip().split(',')
            marklist.append(l)

    del marklist[0]
    for term in marklist:
        name = term[0]
        del term[0]
        for i in term:
            Sum += int(i)
        print("Average marks of "+name+" are "+str(Sum/3))
        Sum = 0
average()