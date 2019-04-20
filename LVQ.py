import math

learning_rate = 0.5
#dataset
dataset = [
    [1, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 1, 1]
          ]

target = [1, 3, 1, 2, 2, 3, 3, 2]

#training_1 dengan 2 data
traning = [
    [0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 1]
          ]
target_traning = [2, 2]
#training_2 dengan 10 data
data = [
        [1, 0, 0, 1,  1, 1, 1, 1],
        [0, 1, 1, 0,  0, 0, 1, 1],
        [1, 0, 0, 1,  0, 1, 1, 1],
        [0, 0, 1, 0,  1, 1, 1, 0],
        [0, 0, 1, 0,  1, 0, 0, 0],
        [1, 0, 1, 0,  0, 0, 0, 1],
        [0, 1, 1, 0,  1, 0, 1, 1],
        [0, 1, 1, 0,  1, 0, 1, 1],
        [0, 0, 1, 0,  0, 0, 0, 1],
        [0, 0, 0, 1,  1, 1, 1, 1]
       ]
target_data = [1, 3, 1, 2, 2, 3, 3, 2, 1, 2]

wight = [dataset[0], dataset[1], dataset[2]]
temp = [[1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 1]]
d=[0, 0, 0]

#training
print("Trainning Data: ")
for x in range(0, 10):
    print("\nEpoch ke:", x)
    for i in range(0, len(dataset)):
        d[0] = 0
        d[1] = 0
        d[2] = 0
        J = 0
        for j in range(0, len(dataset[0])):
            d[0] += (dataset[i][j] - wight[0][j])**2
            d[1] += (dataset[i][j] - wight[1][j])**2
            d[2] += (dataset[i][j] - wight[2][j])**2

        d[0] = math.sqrt(d[0])
        d[1] = math.sqrt(d[1])
        d[2] = math.sqrt(d[2])
        print("Cetak Distance: ", d)
        if (d[0] < d[1] and d[0] < d[2]):
            print("J: ", d[0], "-> 1")
            J = 1
            if (target[i] == J):
                print('J1 == Target')
                for k in range(0, len(wight[1])):
                    wight[0][k] = wight[0][k] + learning_rate * (dataset[i][k] - wight[0][k])

            elif (target[i] != J):
                print('J1 != Target')
                for k in range(0, len(wight[1])):
                    wight[0][k] = wight[0][k] - learning_rate * (dataset[i][k] - wight[0][k])
        elif (d[1] < d[0] and d[1] < d[2]):
            print("J: ", d[1], "-> 2")
            J = 2
            if (target[i] == J):
                print('J2 == Target')
                for k in range(0, len(wight[0])):
                    wight[1][k] = wight[1][k] + learning_rate * (dataset[i][k] - wight[1][k])

            elif (target[i] != J):
                print('J2 != Target')
                for k in range(0, len(wight[0])):
                    wight[1][k] = wight[1][k] - learning_rate * (dataset[i][k] - wight[1][k])

        elif (d[2] < d[1] and d[2] < d[0]):
            print("J: ", d[2], "-> 3")
            J = 3
            if (target[i] == J):
                print('J3 == Target')
                for k in range(0, len(wight[1])):
                    wight[2][k] = wight[2][k] + learning_rate * (dataset[i][k] - wight[2][k])

            elif (target[i] != J):
                print('J3 != Target')
                for k in range(0, len(wight[1])):
                    wight[2][k] = wight[2][k] - learning_rate * (dataset[i][k] - wight[2][k])

        print('W1, W2, W3: ', wight)
    learning_rate = learning_rate * 0.8

#testing 2 data
print("\n\n Testing Data 2 Data")
for x in range (0, 2):
    print(traning[x])
    for j in range(0, len(traning[x])):
        d[0] += (traning[x][j] - wight[0][j])**2
        d[1] += (traning[x][j] - wight[1][j])**2
        d[2] += (traning[x][j] - wight[2][j])**2

    d[0] = math.sqrt(d[0])
    d[1] = math.sqrt(d[1])
    d[2] = math.sqrt(d[2])
    print("Cetak Distance: ", d)
    if (d[0] < d[1] and d[0] < d[2]):
        J=1
    elif (d[1] < d[0] and d[1] < d[2]):
        J=2
    elif (d[2] < d[1] and d[2] < d[0]):
        J=3
    print("->", J)

#testing 10 data
print("\n\n Testing Data 10 Data")
for x in range (0, 10):
    print(data[x])
    for j in range(0, len(data[x])):
        d[0] += (data[x][j] - wight[0][j])**2
        d[1] += (data[x][j] - wight[1][j])**2
        d[2] += (data[x][j] - wight[2][j])**2

    d[0] = math.sqrt(d[0])
    d[1] = math.sqrt(d[1])
    d[2] = math.sqrt(d[2])
    print("Cetak Distance: ", d)
    if (d[0] < d[1] and d[0] < d[2]):
        print("J: ", d[0])
        J=1
    elif (d[1] < d[0] and d[1] < d[2]):
        print("J: ", d[1])
        J=2
    elif (d[2] < d[1] and d[2] < d[0]):
        print("J: ", d[2])
        J=3
    print("->", J)