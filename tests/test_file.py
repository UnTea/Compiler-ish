def main():
    for i in range(3):
        print(f"Outer loop iteration {i}")

        for j in range(2):
            print(f"Inner loop iteration {j}")

    for k in range(4):
        print(f"Another loop iteration {k}")

    foo(4, 1, 3)


def foo(x, y, z):
    return (x * 2 + y / z) * x + z


if __name__ == "__main__":
    main()
