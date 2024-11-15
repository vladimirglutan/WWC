arr = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,2,155,1,9,155,0,99,2,0,14,0]

def wwc(arr, noun, verb):
    arr = arr[:]
    arr[1] = noun
    arr[2] = verb
    current_index = 0

    while current_index < len(arr):
        code = arr[current_index]

        if code == 1:
            pos1 = arr[current_index + 1]
            pos2 = arr[current_index + 2]
            pos3 = arr[current_index + 3]
            arr[pos3] = arr[pos1] + arr[pos2]
            current_index += 4

        elif code == 2:
            pos1 = arr[current_index + 1]
            pos2 = arr[current_index + 2]
            pos3 = arr[current_index + 3]
            arr[pos3] = arr[pos1] * arr[pos2]
            current_index += 4

        elif code == 99:
            break

        else:
            return -1  

    return arr[0]


def find_noun_and_verb(arr, target_output):
    for noun in range(100):
        for verb in range(100):
            output = wwc(arr, noun, verb)
            if output == target_output:
                return noun, verb
    return None, None 



#Part 1A
result = wwc(arr, 12, 2)
print(result)

#Part 1B
noun, verb = find_noun_and_verb(arr, 19690720)
print("Noun:", noun)
print("Verb:", verb)


