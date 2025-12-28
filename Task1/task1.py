from sys import argv


def circular_array(n, m):
    array = [i for i in range(1, n + 1)]
    path = ""

    start = 0
    while True:
        path += str(array[start])

        end = start + m - 1
        if end >= n:
            end = end % n

        if array[end] == 1:
            break

        start = end

    return path


if __name__ == "__main__":
    if len(argv) != 5:
        raise Exception("Ожидаются аргументы: n1 m1 n2 m2")

    n1, m1 = int(argv[1]), int(argv[2])
    n2, m2 = int(argv[3]), int(argv[4])

    result = circular_array(n1, m1) + circular_array(n2, m2)
    print(result)
