from threading import Thread
 
def print_numbers():
    for i in range(10):
        print(i)

thread = Thread(target=print_numbers)
thread.start()
thread.join()