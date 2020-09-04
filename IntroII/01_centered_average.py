# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array (list). 


# Understand
# what do we do if smallest or largest is duplicated
# - we only consider 1 of smallest and 1 of largest to be valid

# what data type are we expecting to return?
# int / float?
# return an int

# centered_average([1, 2, 3, 4, 100]) → 3 >>> [2, 3, 4, 100] -> [2, 3, 4] -> 2 + 3 + 4 => 9 / 3 => 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5 >>> [1, 5, 5, 10, 8, 7] -> [1, 5, 5, 8, 7] -> 1 + 5 + 5 + 8 + 7 => 26 / 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3 >>> [-4, -2, -4, -2, 0] -> [-4, -2, -4, -2]  => -4 + -2 + -4 + -2 => -12 / 4 => -3

# centered_average([1, 2, 3, 4, 100]) -> 3 >>> [1, 2, 3, 4, 100] -> 1 + 2 + 3 + 4 + 100 => 110 => 110 - max => 10 - min => 9 / 3 => 3
# max = 100
# min = 1


#Plan
# get the smallest number from list 
# get largest number from list

# sum up everything in the list
# subtract smallest from the sum
# subtract largest from the sum
# floor divide the sum by the length of the list minus 2
# return the final number


# Execute
def centered_avg(ints):
    # get the smallest number from list
    smallest = min(ints) 
    # get largest number from list
    largest = max(ints)

    # sum up everything in the list
    # set a sum variable to zero
    sum = 0

    # subtract largest from the sum
    # floor divide the sum by the length of the list minus 2
    # return the final number


# testing

numbers = [1, 2, 3, 4, 100]
# print(centered_avg1(numbers))
import time

start = time.time()
# for i in range(1000):
    # centered_avg(numbers)
end = time.time()

print(end - start)

print("-----------------------")

start = time.time()
# for i in range(1000):
    # centered_avg2(numbers)
end = time.time()

print(end - start)