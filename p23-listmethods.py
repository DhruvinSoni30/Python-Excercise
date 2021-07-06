numbers = [5, 2, 5, 1, 7, 4]
numbers.append(9)
print(numbers)

numbers.insert(3,8)
print(numbers)


numbers.pop()
print(numbers)

print(numbers.index(7))

print(5 in numbers)

#In Place Sort
print(numbers.sort())
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

numbers.append(10)
print(numbers)
print(numbers2)