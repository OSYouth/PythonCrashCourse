filename = "love_programming_reasons.txt"

message = "Please input the reason why you love programming "
message += "(enter n if you want to end it): "
while True:

    reason = input(message)
    if reason == 'n':
        break
    with open(filename, 'a') as file_object:
        file_object.write(reason + "\n")

