def count_words_the(filename):
    """计算一个文件大致包含多少个单词the"""

    try:
        with open(filename, encoding='UTF-8') as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词the
        the_words = 0
        for line in lines:
            temp = line.lower().find('the')
            the_words = the_words + temp
        print("The file " + filename + " has about " + str(the_words) + " 'the' words.")

filenames = ['Harvesting_Ants_and_Trap-Door_Spiders.txt']
for filename in filenames:
    count_words_the(filename)