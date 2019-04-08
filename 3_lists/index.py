animals = ["dog", "cat", "mouse"]

print(animals)
print(animals[1])

animals[1] = "supercat"

print(animals)

users = list(["John", "Carl"])
print(users)

count = [1, 2, 3, 4, 5]

print(5 in count)
print(1 not in count)
print(len(count))
print(sum(count))

count2 = [6]
count.extend(count2)
print(count)


count.sort()
print(count)

count.reverse()
print(count)

count.append(7)
print(count)

count.remove(1)
print(count)