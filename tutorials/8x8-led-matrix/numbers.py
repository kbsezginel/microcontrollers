

num1 = [[0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 0]]

num2 = [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

num3 = [[1, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0]]

num4 = [[0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 0]]

num5 = [[1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 0]]

num6 = [[0, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]]

num7 = [[1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]]

num8 = [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]]

num9 = [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 0]]

num0 = [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]]

numbers = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

def get_5x8_array(number):
    if len(str(number)) > 2:
        print('Enter number between 0 - 99')
    elif len(str(number)) == 1:
        digit1 = 0
        digit2 = int(number)
    elif len(str(number)) == 2:
        digit1 = int(str(number)[0])
        digit2 = int(str(number)[1])

    array_5x8 = []
    array1 = numbers[digit1]
    array2 = numbers[digit2]
    for a1, a2 in zip(array1, array2):
        array_5x8.append(a1 + a2)

    return array_5x8
