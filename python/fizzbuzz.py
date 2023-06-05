
def fizzbuzz(arg1):
    
    if(arg1 % 3 == 0 and arg1 % 5 == 0):
        print ('FizzBuzz', '-', arg1)

    if(arg1 % 3 == 0):
        print ('Fizz', '-', arg1)

    if(arg1 % 5 == 0):
        print ('Buzz', '-', arg1)



    
    
    
nums = [9921, 10505, 999, 775, 779, 900, 333, 69, 3, 99, 600, 750, 6030120, 70, 72, 102, 96]

for x in nums:
    fizzbuzz(x)


