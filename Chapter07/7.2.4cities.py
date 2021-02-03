prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' to end the program. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    # else:
    #     print("I'd love to go to " + city.title() + "!")

# 在该程序中如下语句也可以实现如上两句的功能
    print("I'd love to go to " + city.title() + "!")