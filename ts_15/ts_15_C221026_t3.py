from multiprocessing import Process
def print_squares(numbers):
    for n in numbers:
        print(f"Square: {n*n}")

def print_cubes(numbers):
    for n in numbers:
        print(f"Cube: {n*n*n}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    process1 = Process(target=print_squares, args=(numbers,))
    process2 = Process(target=print_cubes, args=(numbers,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both processes are complete!")