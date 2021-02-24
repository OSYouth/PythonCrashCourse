from collections import OrderedDict

dictionary = OrderedDict()

dictionary['soup'] = "汤"
dictionary['beatifulSoup'] = "美味汤？"
dictionary['if'] = "如果"
dictionary['else'] = "其他"
dictionary['elif'] = "其他如果？哈哈哈哈"

for index, interpretation in dictionary.items():
    print(index.title() + ": " + interpretation + "." )