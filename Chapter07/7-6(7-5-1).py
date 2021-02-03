prompt = "\nPlease enter your age! "
prompt += "\nYou could enter 'quit' if you want to end this program: "

age = ""
while age != 'quit':
    age = input(prompt)
    # 事实上这个条件很不严谨，输入小数或者字符串都能使得该程序报错
    # 因为使用了int()，所以可以加类型判断或者其他以避免该问题
    if age != 'quit':
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        else:
            price = 15
        print("\nThe price is " + str(price) + " dollars.")