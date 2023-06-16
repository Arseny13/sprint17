def get_circle():
    circle = []
    for i in range(-20, 21):
        for j in range(-20, 21):
            if i**2 + j**2 <= 400:
                circle.append((i, j))
    return circle


def get_data():
    count_subway = int(input())
    subway = [tuple(map(int, input().split())) for _ in range(count_subway)]
    count_bus_stop = int(input())
    bus = {}
    for i in range(count_bus_stop):
        bus_coord = tuple(map(int, input().split()))
        if bus_coord in bus:
            bus[bus_coord] += 1
        else:
            bus[bus_coord] = 1
    return subway, bus


def find_best_exit():
    subway, bus = get_data()
    circle = get_circle()
    max_count = 0
    best_exit = 0
    for i, (x, y) in enumerate(subway):
        count = 0
        for dx, dy in circle:
            curr_coord = (x + dx, y + dy)
            if curr_coord in bus:
                count += bus[curr_coord]
        if count > max_count:
            max_count = count
            best_exit = i
    return best_exit + 1


if __name__ == '__main__':
    print(find_best_exit())
