#The Collatz Sequence: The Simplest impossible Math problem


def collatz(number):
    status = number % 2

    if status == 0:
        num = number // 2
        print(num)
        return num
    if status == 1:
        num = 3 * number+1
        print(num)  
        return num
   


print("\t\t\t\t\t******************************\n\t\t\tThe Collatz Sequence: The Simplest Impossible Math Problem\n\t\t\t\t\t******************************")

print("Please enter a name: ")
name = input()

print('\n')

try:
    print(name + ", welcome please enter an integer: ")
    collatzNum = input()

    #Prints out Sequence
    
    output = collatz(int(collatzNum))

    while output != 1:
        output = collatz(output)

    print("\nThat's your Collatz Sequence, see you next time\n")
except ValueError:
    print("That's not an integer, enter an integer\n")


