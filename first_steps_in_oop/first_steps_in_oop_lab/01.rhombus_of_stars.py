def print_triangle(n):
    for i in range(n + 1):
        print(' ' * (n - i), end='')
        print(*['*'] * i)


def print_reverse_triangle(n):
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        print(*['*'] * i)


def print_rhombus(n):
    print_triangle(n)
    print_reverse_triangle(n)


n = int(input())

print_rhombus(n)
