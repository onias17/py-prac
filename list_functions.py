# LIST FUNCTIONS

tribes = ["judah", "benjamin", "levi", "ephraim", "issachar"]
prophets = ["isaiah", "jeremaih", "ezekiel", "daniel"]
numbers = [7, 144000, 12, 10, 3, .67, .33]
num = numbers.copy()

print(prophets)
prophets.append("hosea")
print(prophets)
prophets.extend(tribes)
print(prophets)
prophets.insert(0, "solomon")
print(prophets)
prophets.remove("hosea")
print(prophets)
prophets.pop()
print(prophets)
print(prophets.index("benjamin"))
print(prophets.count("ezekiel"))
prophets.sort()
print(prophets)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(num)

prophets.clear()
print(prophets)
