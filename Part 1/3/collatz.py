import sys

def collatz(x):
     if x % 2 == 0:
        #Even number 
        result = x // 2 
        print(result)
        return result
     else:
        #Odd number
        result = 3 * x + 1
        print(result)
        return result
try:
    print("enter number:")
    current_number = int(input())

    while current_number != 1:
        current_number = collatz(current_number) 

    print("Sequence finished.")

except ValueError:
    print("Error: You must enter a valid integer.")
except KeyboardInterrupt:
    sys.exit()