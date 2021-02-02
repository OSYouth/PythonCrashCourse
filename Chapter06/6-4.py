dictionary = {
    'Python' : "Python is a programming language that lets you work more quickly and integrate your systems more effectively.",
    'Loop' : "循环",
    'program' : "程序",
    'design' : "设计",
    'data' : "数据",
}

dictionary['soup'] = "汤"
dictionary['beatifulSoup'] = "美味汤？"
dictionary['if'] = "如果"
dictionary['else'] = "其他"
dictionary['elif'] = "其他如果？哈哈哈哈"

for index, interpretation in dictionary.items():
    print(index.title() + ": " + interpretation + "." )