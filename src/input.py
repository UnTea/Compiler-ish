def foo(x, y, z):
    return (x * 2 + y / z) * x + z


def main():
    for i in range(3):
        foo(1, 1, i)

        for j in range(2):
            foo(1, j, 1)

    for i in range(4):
        foo(i, 1, 1)


if __name__ == "__main__":
    main()
