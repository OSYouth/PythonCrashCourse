likes = ["wuyue", "ChangJiang", "China", "ChangSha", "Python"]
print(likes)
print(likes[1])
print(likes[-1])

likes[-1] = "Java"
print(likes)

likes.append("NZT")
print(likes)

likes.insert(3,"Swimming")
print(likes)

del likes[3]
print(likes)

likes.pop()
print(likes)

likes.pop(3)
print(likes)

likes.remove("ChangJiang")
print(likes)

likes.sort()
print(likes)

likes.sort(reverse = True)
print(likes)

print(sorted(likes))
print(likes)

likes.reverse()
print(likes)

print(len(likes))