'''
The purpose of this program is to find all prime numbers in a range specified by the user, which  also 
belong to the Fibonacci numbers. 
Note: After 1000000 this algorithm takes longer to execute
'''
'''
The first function determines if a number is prime. 2 is the only even prime number; 0,1 and all other even
numbers are excluded in the elif statement. For the odd numbers from 3 up to ther sq root value + 1 if its
divisible by any other number then it's not prime and any further processing is stopped with the break statement
The function returns boolean True or False value
'''
def is_prime(n):
    b = True
    if n == 2:
        b = True
    elif n < 2 or n%2 == 0:
        b = False
    else:
        for x in range(3,(int(n**0.5) + 1), 2):
            if n%x == 0:
                b = False
                break
    return b
'''
Then we create a function that creates a list of all fibonacci numbers in specified range
0 and 1 are the seed numbers in the fibonacci list. Any other number can be inferred from the
sum of its last two predecessors. It's then added to the list and then the function returns
that list to the main program for further processing
'''
def fib(n):
    fib_list = [0,1]
    for i in range (n+1):
        if i == fib_list[-2] + fib_list[-1]:
            fib_list.append(i)
    return fib_list
'''
In main program we set up for  while loop asking the user if they want to continue searching 
for prime fibonacci numbers until they enter n for No. After that we create a list of all prime numbers
using list comprehension and another list from those fibonacci list numbers that also belong to prime numbers
list. The resulting list is printed to the screen.
If user enters n for No , a Thank you message is displayed and program terminates
'''
def main():
    flag = 'y'
    while flag != 'n':
        num = int(input("Please enter a range to check for prime fibonacci numbers: "))
        prime_list = [x for x in range(num+1) if is_prime(x)]
        prime_fib = [ x for x in fib(num) if x in prime_list]
        print(prime_fib)
        flag = input("Do you want to try different range? 'y' for Yes or 'n' for No:")
    print("Thank you! Goodbye!")
    exit()
    
if __name__ == "__main__":               # This ensures that program will run only if called from this file. Not if imported 
    main()                          