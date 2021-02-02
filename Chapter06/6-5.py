riverCountries ={
    'nile': 'egypt',
    'nile': 'ethiopia',
    'nile': 'sudan',
    'amazon': 'brazil',
    'amazon': 'peru',
    'amazon': 'bolivia',
    'amazon': 'columbia',
    'amazon': 'ecuador',
    'amazon': 'venezuela',
    'amazon': 'guyana',
    'nile': 'uganda',
    'nile': 'nan sudan',
    'yangtse': 'china',
    'nile': 'tanzania',
    'nile': 'rwanda',
    'nile': 'burundi',
    'nile': 'congo',
    'nile': 'kenya',
    'nile': 'eritrea',
}

for river, country in riverCountries.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print()
for river in set(riverCountries):
    print(river.title())
print()
for country in riverCountries.values():
    print(country.title())

# 从该示例的运行结果也可以看出，键的重复只会有一组键值对生效
# 没运行之前，自己还傻傻地搜索三大河流流经的每一个国家，真的是……不过也可以尝试把键和值换过来进行遍历