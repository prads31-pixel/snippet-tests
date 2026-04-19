
nums = [4,2,2,1,3,3]

for x in sorted(set(nums)):
    print(x)    

animals = ["cat", "dog", "bird", "fish", "hamster"]
print(animals[0])  # Output: cat
print(animals.__len__())  # Output: 5
animals.insert(1, "rabbit")
animals.append("turtle")
print(animals)  # Output: ['cat', 'rabbit', 'dog', 'bird', 'fish', 'hamster', 'turtle']