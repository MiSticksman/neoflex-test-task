

def move_zeros(arr: list) -> list:
    zero_position = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[zero_position], arr[i] = arr[i], arr[zero_position]
            zero_position += 1
    return arr
