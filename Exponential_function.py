#!/usr/bin/env python3

def fact(n):
    #Return factorial: n!  
    if(n <= 1):
        return 1
    else:
        return n*fact(n-1)

def iter(x, n):
    #Return iterative adding term of sum: (x^n)/n!
    return exp(x,n)/fact(abs(n))

def exp(x,n):
    #Return exponent: x^n
    if(n <= 1): #End of recursive function
        return x
    else:
        return x * exp(x,n-1) 
    

def e_func(x, n):
    #Return exponential function approximation: e^x
    if(n == 0):
        return 1
    else:
        return iter(x,n) + e_func(x,n-1)

if __name__ == '__main__':
    # Main Function
    print("Welcome!")
    print("Calculating e^1 with 9 decimals equals: ")
    print(e_func(1,9))
    menu = ""

    while(menu!="q"):

        print("If you desire to test exponential function approximation input x and n following:")

        #Input values
        x = int(input("Choose x exponente value: "))
        n = int(input("Choose n approximation terms number: "))

        #Output exponential approximation function result
        if(n <= 0):
            print("Value of n must be greater than 0!")
        else:
            print("The exponential approximation of e^" + str(x) +" with n="+ str(n) +" terms is:")
            print(e_func(x,n))

            #Menu option
            menu = input("Enter q to exit or any other value to try again.")
