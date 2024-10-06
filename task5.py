#1 What is the expected output of the following python code given below:
data = [10,501,22,37,100,999,87,351]
result = filter (lambda x: x>4,data)
print(list(result))
OUTPUT — [10, 501, 22, 37, 100, 999, 87, 351]

# 2 Write a Python code using Lambda function to check every element of a List
# is an Integer or string?
from functools import reduce

test_list = [[5,6,3],[“Gfg”, 3, “is”],[9, “best”, 4]]

print(“The original list : “ + str(test_list))

res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])

print(“The string instances : “ + str(res))

res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])

print(“The string instances : “ + str(res1))


                                                                                                   

#3) Using a python Lambda function create a fibonacci series from 1 to 50 elements?

def fibonacci(count):
fib_list = [0, 1]

any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
range(2, count)))

return fib_list[:count]

print(fibonacci(50))




#3) Using a python Lambda function create a fibonacci series from 1 to 50 elements?

def fibonacci(count):
fib_list = [0, 1]

any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
range(2, count)))

return fib_list[:count]

print(fibonacci(50))



