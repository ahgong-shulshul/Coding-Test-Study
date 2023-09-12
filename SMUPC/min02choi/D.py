import math

def print_room(k):
    height = math.ceil(math.log2(k + 1))

    sub = 2 ** (height - 1) - 1

    room_floor = str(height)
    room_num = str(k - sub)
    zeros = "0" * (18 - len(room_num))

    room_full = room_floor + zeros + room_num
    return room_full


t = int(input())


for i in range(t):
    n = int(input())
    while (n >= 1):
        print(print_room(n))
        n = math.floor(n / 2)
