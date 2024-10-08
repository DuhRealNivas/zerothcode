# Python program that takes a number n as input and returns the function f(n),
# ...defined as the sum of odd numbers between 1 and n/2, and the sum of even numbers between (n/2) + 1 and n.

# Let us take a whole number n as input.
n = int(input("Enter a whole number: "))

# Defining a variable 'half' which is half of the in-putted whole number.
half = n/2

# Defining a function to convert 'half' to an integer if 'half' is a float and whole number, else leave 'half' as float itself.
def convert_whole_to_integer(half):
    if isinstance(half, float) and half.is_integer():
        return int(half)
    return half

# 'con_half' is the converted 'half' if it was a float and whole number using the defined function 'convert_whole_to_integer()'.
con_half = convert_whole_to_integer(half)

# Introducing four 'if' loops (2+1+1) and any one of these will get executed:
    #   (1a) when the converted half is float and will become odd if 0.5 is added to it.
    #   (1b) when the converted half is float and will become even if 0.5 is added to it.
    #   (2)  when the converted half is odd.
    #   (3)  when the converted half is even.

if isinstance(con_half, float): # loop runs if the converted half is float
    
    if (con_half+0.5) % 2 == 1: # sub-loop (1a) will run if the converted half is an odd number after adding 0.5 to it
        numbers = list(range(int(1), int(n))) # taking out all the numbers in the range 1 to n as an array
        odd = list(range(int(1),int(con_half),2)) # taking out all the odd numbers in the range 1 to the converted half
        even = list(range(int(con_half+1.5),int(n),2)) # taking out all the even numbers in the range converted half + 1.5 and n
        # Note: Added 1.5 (not 0.5) to the converted half because the even list should be in the range n/2 + 1 and n. (question)
   
    else: # sub-loop (1b) will run if the converted half is an even number after adding 0.5 to it
        numbers = list(range(int(1), int(n))) # taking out all the numbers in the range 1 to n as an array
        odd = list(range(int(1),int(con_half+0.5),2)) # taking out all the odd numbers in the range 1 to the converted half + 0.5
        # Note: Added 0.5 to the converted half so that it will take the last odd number just before the half into account.
        even = list(range(int(con_half+0.5),int(n),2)) # taking out all the even numbers in the range converted half + 0.5 and n
        # Note: Added 0.5 to the converted half so that it takes a list of even numbers from converted half + 0.5 to n

elif con_half % 2 == 1: # loop (2) runs if the converted half is a whole number and odd
    numbers = list(range(int(1), int(n))) # taking out all the numbers in the range 1 to n as an array
    odd = list(range(int(1),int(con_half+1),2)) # taking out all the odd numbers in the range 1 to the converted half + 2
    # Note: Added 1 to the converted half so that it includes the half to the odd number array 
    even = list(range(int(con_half+1),int(n+1),2)) # taking out all the even numbers in the range (converted half + 1) to (n + 2) 
    # Note: Added 1 to the converted half so that it takes a list of even numbers from (converted half + 1) to (n + 1) 
    # PS: (n + 1) is used because in  Python, the last number in the range will not be included.
    
else: # loop (3) runs if the converted half is a whole number and even
    numbers = list(range(int(1), int(n))) # taking out all the numbers in the range 1 to n as an array
    odd = list(range(int(1),int(con_half),2)) # taking out all the odd numbers in the range 1 to the converted half
    even = list(range(int(con_half+2),int(n+2),2)) # taking out all the even numbers in the range (converted half + 2) and (n + 2)
    # Note: (converted half + 2) is used to exclude the even half
    # Note: (n+2) is used to include the last even number 

oddsum = sum(odd) # adding all the elements in the odd numbers array
evensum = sum(even) # adding all the elements in the even numbers array
final_list = odd + even # making a final list from the odd and even numbers arrays
final_list_w_plus = ' + '.join(map(str, final_list)) # removing the ',' and '[ ]', and replacing with + between each elements

print("f({}) = {} = {}".format(n, final_list_w_plus, oddsum + evensum))
# Displaying the output in the mentioned format.