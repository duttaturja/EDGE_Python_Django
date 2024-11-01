given_list = []
prime_number_list = []
def display_prime_numbers(list):
    for i in list:
        if i == 1:
            continue
        is_prime = True
        for j in range(2,i):
            if i%j == 0:
                is_prime = False
        
        if is_prime:
            prime_number_list.append(i)

n=input("Enter Your list length: ")
n= int(n)
for i in range(0,n):
    x = input(f"{i+1}th element: ")
    x=int(x)
    given_list.append(x)

display_prime_numbers(given_list)
print(prime_number_list)