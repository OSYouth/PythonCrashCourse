names = ['Leo','Eric','Kobe','HYF','ZF','CMS']

print(names)

message = names[0] + ", may I have dinner with you together?"
print(message)

message = names[1] + ", may I have dinner with you together?"
print(message)

message = names[2] + ", may I have dinner with you together?"
print(message)

message = names[3] + ", may I have dinner with you together?"
print(message)

message = names[4] + ", may I have dinner with you together?"
print(message)

message = names[5] + ", may I have dinner with you together?"
print(message)

print("\n" + names[2] + " can't join the dinner.")
names[2] = 'LX'
print(names)

message = names[0] + ", may I have dinner with you together?"
print(message)

message = names[1] + ", may I have dinner with you together?"
print(message)

message = names[2] + ", may I have dinner with you together?"
print(message)

message = names[3] + ", may I have dinner with you together?"
print(message)

message = names[4] + ", may I have dinner with you together?"
print(message)

message = names[5] + ", may I have dinner with you together?"
print(message)

print("\nI've find another bigger dinner table.")
names.insert(0, 'PYY')
names.insert(3, 'JJF')
names.append('LHR')

message = names[0] + ", may I have dinner with you together?"
print(message)

message = names[1] + ", may I have dinner with you together?"
print(message)

message = names[2] + ", may I have dinner with you together?"
print(message)

message = names[3] + ", may I have dinner with you together?"
print(message)

message = names[4] + ", may I have dinner with you together?"
print(message)

message = names[5] + ", may I have dinner with you together?"
print(message)

message = names[6] + ", may I have dinner with you together?"
print(message)

message = names[7] + ", may I have dinner with you together?"
print(message)

message = names[8] + ", may I have dinner with you together?"
print(message)

print("\n I can only inviter two person to have dinner with me together.")

popped_person = names.pop()
print(popped_person + ", sorry, I can't invite you have dinner with me together.")
popped_person = names.pop()
print(popped_person + ", sorry, I can't invite you have dinner with me together.")
popped_person = names.pop()
print(popped_person + ", sorry, I can't invite you have dinner with me together.")
popped_person = names.pop()
print(popped_person + ", sorry, I can't invite you have dinner with me together.")
popped_person = names.pop()
print(popped_person + ", sorry, I can't invite you have dinner with me together.")
popped_person = names.pop()
print(popped_person + ", sorry, I can't invite you have dinner with me together.")
popped_person = names.pop()
print(popped_person + ", sorry, I can't invite you have dinner with me together.")

print(names[0] + ", " + names[1] + ", you're still in my list.")

del names[0]
del names[0]
print(names)